# Тесты сервиса `<SERVICE_NAME>`

Скопируйте в `tests/README.md`, замените `<SERVICE_NAME>` и `my_package` на имя вашего пакета в `src/`.

---

## Зависимости и Poetry

Тестовые пакеты — в **dev-группе**, не в prod:

```toml
[tool.poetry.dependencies]
python = "^3.10"
# только то, что нужно рантайму

[tool.poetry.group.dev.dependencies]
pytest = "^8.0"
pytest-asyncio = "^0.24"   # если есть async-тесты
pytest-cov = "^5.0"        # опционально, CI

[tool.pytest.ini_options]
testpaths = ["tests"]
pythonpath = ["src"]
asyncio_mode = "auto"      # уберите, если async нет
```

**Локально и в CI** (нужны pytest и прочее):

```bash
poetry install
```

**Prod-образ / установка без тестов** — dev-группа не ставится:

```bash
poetry install --only main
```

В Docker для рантайма используйте эту команду (или `poetry export` только из `[tool.poetry.dependencies]`).  
`pytest` в образ не попадёт, пока вы явно не ставите dev-группу.

Проверка: `poetry run pytest --version` после `poetry install`; после `--only main` — команда недоступна (ожидаемо).

---

## Запуск

Из корня сервиса (`pyproject.toml`):

```bash
poetry run pytest              # все
poetry run pytest -v           # подробно
poetry run pytest -x           # стоп на первой ошибке
poetry run pytest tests/billing/ -v                    # домен
poetry run pytest tests/billing/test_invoice.py -v     # файл
poetry run pytest tests/billing/test_invoice.py::test_calculates_total -v
poetry run pytest -s             # print при отладке
poetry run pytest --cov=src --cov-report=term-missing  # покрытие
```

---

## CI (тесты и coverage)

Готовые фрагменты (скопировать и подправить путь к сервису):

| Файл | Куда |
|------|------|
| `gitlab-ci.tests.example.yml` | job'ы в `.gitlab-ci.yml` |
| `github-actions.tests.example.yml` | `.github/workflows/tests.yml` |

В CI всегда **`poetry install`** (с dev), не `--only main`.  
Команда в job'е:

```bash
poetry run pytest \
  --cov=src \
  --cov-report=term-missing \
  --cov-report=xml:coverage.xml \
  --junitxml=report.xml
```

Порог (опционально): добавьте `--cov-fail-under=70`.  
Для монорепо задайте каталог сервиса: GitLab — `SERVICE_DIR`, GitHub — `defaults.run.working-directory`.

---

## Структура `tests/`

**Правило:** путь в `tests/` зеркалит `src/my_package/`; **один модуль → один `test_<module>.py`**. Не один файл на весь домен.

| Код | Тесты |
|-----|--------|
| `src/my_package/discount.py` | `tests/test_discount.py` |
| `src/my_package/billing/invoice.py` | `tests/billing/test_invoice.py` |

Несколько доменов (подпакетов в `src`):

```
src/my_package/billing/invoice.py  →  tests/billing/test_invoice.py
src/my_package/export/journal.py   →  tests/export/journal/test_journal.py
```

Импорт в тесте — как в приложении: `from my_package.billing.invoice import ...`.

Заглушки: `_Fake*` в том же `test_*.py`; общие для домена — `tests/<домен>/_fakes.py`; для всех доменов — `tests/helpers.py`. Фикстуры/`conftest` — по желанию, если одна настройка повторяется во многих тестах (см. `TDD-инструкция.md`, §1).

Имена: файлы `test_*.py`, функции `test_*`, один тест — одно поведение.

---

## Новый тест

1. Найти модуль в `src/` → создать или открыть зеркальный `tests/.../test_<module>.py`.
2. Написать тест (AAA ниже) → `poetry run pytest ...` — должен упасть понятно (`ImportError`, diff assert).
3. Минимальный код в `src/` (даже хардкод) → зелёный.
4. Второй тест с **другими** входами → убрать хардкод, обобщить → снова зелёный → рефакторинг.

### AAA (Arrange – Act – Assert)

Три блока: данные → **один** вызов → проверки. Между блоками — **пустая строка**. Комментарии `# Arrange` / `# Act` / `# Assert` — только в длинных тестах, не обязательны везде.

```python
import pytest

from my_package.billing.discount import apply_discount


def test_apply_discount_reduces_price_by_ten_percent():
    price = 100
    percent = 10

    result = apply_discount(price, percent)

    assert result == 90


def test_apply_discount_raises_on_negative_percent():
    with pytest.raises(ValueError, match="percent must be non-negative"):
        apply_discount(100, -1)
```

Async (если в `pyproject.toml` есть `asyncio_mode = "auto"`):

```python
@pytest.mark.asyncio
async def test_fetches_status_ok():
    client = _FakeClient(status=200)

    status = await fetch_status(client)

    assert status == "ok"
```

`_FakeClient` объявите в том же файле. Зависимости в код — через аргументы/конструктор; `unittest.mock` — только если DI пока нет.

---

## Отладка

```bash
poetry run pytest tests/billing/test_discount.py::test_apply_discount_reduces_price_by_ten_percent -v -s
poetry run pytest tests/billing/test_discount.py --pdb
```

Если неясно, тест или код виноват: посмотреть фактический результат после Act; временно испортить `expected` — тест должен стать красным.
