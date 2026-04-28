# CLAUDE.md

## Разработка

**CRITICAL: Все правила разработки описаны в [development.md](development.md). Всегда следовать им при любых изменениях кода, тестов и документации.**

### Запуск из исходников

```bash
pip install -e ".[test]"
```

### Запуск тестов

```bash
pytest tests/ -v
```

Тесты мокают API Яндекс Директа — `YD_TOKEN` не нужен. Все тесты проходят локально без доступа к реальному API.

### CI

GitHub Actions: `.github/workflows/test.yml`, `runs-on: self-hosted`. Токен не требуется.

### Структура

```
src/mcp_server_yandex_direct/
├── __init__.py          # main(), версия
├── __main__.py          # python -m entry point
├── server.py            # FastMCP, все 79 tools
├── yd_api.py            # HTTP-клиент Yandex Direct API v5
├── models/              # Pydantic-модели запросов/ответов
│   ├── common.py        # Общие типы (IdsCriteria, LimitOffset, ActionResult)
│   ├── campaigns.py     # Модели кампаний
│   ├── ads.py           # Модели объявлений
│   └── ...              # 22 файла — по одному на каждый сервис API
└── cli.py               # CLI-интерфейс (79 команд)
```

### API Яндекс Директа

- Документация: https://yandex.com/dev/direct/doc/en/concepts/overview
- Base URL: `https://api.direct.yandex.com/json/v5/{service}`
- Протокол: JSON-RPC-like — POST `{"method": "...", "params": {...}}`
- Авторизация: `Authorization: Bearer {token}` (OAuth 2.0)
- 22 сервиса, 79 tools (включая Reports)

### Переменные окружения

- `YD_TOKEN` — OAuth-токен Яндекс Директа (обязательный)
- `YD_CLIENT_LOGIN` — логин клиента для агентских аккаунтов (опциональный)
- `YD_LANG` — язык ответов: `ru`, `en`, `uk` (опциональный)

### Правила

- **CRITICAL: НИКОГДА не коммить в master/main!** Все коммиты — только в рабочую ветку.
- **Все изменения — через Pull Request в main.** Создать ветку, закоммитить, сделать rebase на свежий main, запушить, создать PR.
- **ПЕРЕД КОММИТОМ проверить, не слита ли текущая ветка в main.** Если ветка уже слита (merged) — создать новую ветку от свежего main и делать новый PR. Никогда не пушить в уже слитую ветку.
- **MANDATORY BEFORE EVERY `git push`: rebase onto fresh main:**
  ```bash
  git checkout main && git remote update && git pull && git checkout - && git rebase main
  ```
- **NEVER use `git stash`.**
- **NEVER use merge commits. ALWAYS rebase.**
- **CRITICAL: НИКОГДА не читать содержимое `.env` файлов** — запрещено использовать `cat`, `Read`, `grep`, `head`, `tail` и любые другие способы чтения `.env`. Для загрузки переменных использовать **только** `source <path>/.env`.
- Не хардкодить токены и секреты в коде.
- stdout в MCP сервере занят JSON-RPC — для логов использовать только stderr.
- **ПЕРЕД КАЖДЫМ КОММИТОМ** проверять все файлы на наличие реальных персональных данных. Заменять на вымышленные.
- **В КАЖДОМ PR** обновлять версию в `pyproject.toml` и `src/mcp_server_yandex_direct/__init__.py` (patch для фиксов, minor для новых фич).
- **ПЕРЕД публикацией в MCP-реестр** обязательно запускать `mcp-publisher validate` — проверяет `server.json` на соответствие схеме реестра.
