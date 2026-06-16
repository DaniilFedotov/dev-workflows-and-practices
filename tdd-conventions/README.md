# Шаблоны TDD и unit-тестов (Python)

| Файл | Куда | Содержание |
|------|------|------------|
| **tests-README.md** | `tests/README.md` в сервисе | Poetry dev/prod, запуск, CI, структура, AAA |
| **TDD-инструкция.md** | Wiki / личные заметки | Цикл TDD, гарантии, стек + опциональные инструменты |
| **CONVENTIONS-AI.md** | Контекст Cursor/ИИ | Короткая выжимка правил для генерации тестов |
| **gitlab-ci.tests.example.yml** | `.gitlab-ci.yml` | Job тестов + Cobertura/JUnit |
| **github-actions.tests.example.yml** | `.github/workflows/` | Job тестов + артефакты coverage |
| **example_test_module.py** | Справочно | Пример `test_*.py` |

**Новый сервис:** `tests-README.md` → `tests/README.md`; TDD — по `TDD-инструкция.md`.  
**ИИ:** в контекст класть **`CONVENTIONS-AI.md`**; при необходимости — `tests-README.md`. Всю папку целиком — только если нужны CI-примеры или полный TDD-цикл в одной сессии.
