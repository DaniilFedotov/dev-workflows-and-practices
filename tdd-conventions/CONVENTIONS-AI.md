# Конвенции unit-тестов (контекст для ИИ)

Краткая выжимка для генерации и ревью кода. Полные пояснения: `tests-README.md`, TDD-цикл: `TDD-инструкция.md`.

---

## Стек

- pytest, `unittest.mock`, `pytest-asyncio` (если async), `pytest-cov` в dev
- Poetry: pytest только в `[tool.poetry.group.dev.dependencies]`
- `[tool.pytest.ini_options]`: `testpaths = ["tests"]`, `pythonpath = ["src"]`, при async — `asyncio_mode = "auto"`

---

## Куда класть тесты

- `tests/` зеркалит `src/<package>/`
- Один модуль продакшена → один `test_<module>.py`
- Домены: `src/pkg/billing/x.py` → `tests/billing/test_x.py`
- Не один огромный файл на весь домен

---

## Стиль теста

- Функции `def test_<поведение>_<условие>()`, не `TestCase` (если не legacy)
- **AAA**: Arrange → Act (один вызов) → Assert; фазы через пустую строку
- Один тест — одно поведение
- Подготовка: литералы в тесте → `_Fake*` в файле → `tests/<domain>/_fakes.py` → `tests/helpers.py`
- Assert по наблюдаемому результату (ТЗ, эталон), не копия формулы из продакшена
- DI: зависимости в конструктор/аргументы + заглушка; `patch` — если DI нет

---

## TDD при новом коде

1. Узкий тест первым → Red (`ImportError` или assert diff)
2. Минимальная реализация → Green (хардкод допустим)
3. Второй тест с другими входами → обобщить код
4. Refactor, `pytest` зелёный
5. Края и `pytest.raises` — отдельными тестами

---

## Опционально (сложные модули)

| Механизм | Когда |
|----------|--------|
| `@pytest.fixture`, `conftest.py` | Тяжёлый общий Arrange в 5+ тестах; предпочитать `tests/<domain>/conftest.py` |
| `@pytest.mark.parametrize` | Таблица вход/выход без дублирования тела |
| `unittest.TestCase` | Только legacy / чужой базовый класс |
| `@pytest.mark.integration` | Реальная БД, брокер, внешние сервисы |
| `patch` | Синглтоны, frozen imports без DI |

---

## Команды

```bash
poetry install              # локально / CI
poetry install --only main  # prod-образ
poetry run pytest
poetry run pytest --cov=src --cov-report=term-missing
```

---

## При генерации кода ИИ должен

- Добавлять/обновлять тест в зеркальном пути под `tests/`
- Следовать AAA и именованию `test_*`
- Не тянуть pytest в prod-зависимости
- Не создавать глобальный `conftest` ради одного файла
- Предлагать фикстуры только при явном повторе тяжёлого Arrange
