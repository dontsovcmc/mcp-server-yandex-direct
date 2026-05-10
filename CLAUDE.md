# CLAUDE.md

## Разработка

**CRITICAL: Все правила разработки описаны в [development.md](development.md). Всегда следовать им при любых изменениях кода, тестов и документации.**

### Запуск из исходников

```bash
pip install -e ".[test]"
```

### Загрузка переменных из файла

```bash
# MCP-сервер с env-файлом
mcp-server-yandex-direct --env /path/to/.env

# CLI с env-файлом
mcp-server-yandex-direct --env /path/to/.env campaigns-get '{"SelectionCriteria": {}, "FieldNames": ["Id"]}'
```

`--env` загружает переменные через `python-dotenv` до инициализации сервера. Без `--env` — стандартные переменные окружения.

### Запуск тестов

```bash
ruff check src/ tests/
pytest tests/ -v
```

Тесты мокают API Яндекс Директа — `YD_TOKEN` не нужен. Все тесты проходят локально без доступа к реальному API.

### CI

GitHub Actions: `.github/workflows/test.yml`, `runs-on: self-hosted`. Токен не требуется.

### Структура

```
src/mcp_server_yandex_direct/
├── __init__.py          # main(), версия, --env загрузка
├── __main__.py          # python -m entry point
├── server.py            # FastMCP, 2 tools: yd_search + yd_execute
├── actions.py           # Каталог 79 действий (Action dataclass + ACTIONS dict)
├── yd_api.py            # HTTP-клиент Yandex Direct API v5
├── models/              # Pydantic-модели запросов/ответов
│   ├── common.py        # Общие типы (IdsCriteria, LimitOffset, ActionResult)
│   ├── campaigns.py     # Модели кампаний
│   ├── ads.py           # Модели объявлений
│   ├── reports.py       # ReportsGetBody (тело запроса отчёта)
│   └── ...              # 23 файла — по одному на каждый сервис API
└── cli.py               # CLI-интерфейс (79 команд)
docs/
├── campaigns.md         # 8 действий домена campaigns
├── adgroups.md          # 4 действия домена adgroups
├── ads.md               # 9 действий домена ads
├── keywords.md          # 6 действий домена keywords
├── bidding.md           # 7 действий домена bidding (bids + bidmodifiers)
├── assets.md            # 11 действий домена assets (sitelinks + images + videos + extensions)
├── audience.md          # 10 действий домена audience (audiencetargets + retargetinglists)
├── negkeywords.md       # 4 действия домена negkeywords
├── feeds.md             # 4 действия домена feeds
├── creatives.md         # 2 действия домена creatives
├── research.md          # 2 действия домена research
├── leads.md             # 1 действие домена leads
├── changes.md           # 3 действия домена changes
├── account.md           # 6 действий домена account (dictionaries + clients + agencyclients)
├── turbopages.md        # 1 действие домена turbopages
└── reports.md           # 1 действие домена reports
```

### API Яндекс Директа

- Документация: https://yandex.ru/dev/direct/doc/concepts/about.html
- Base URL: `https://api.direct.yandex.com/json/v5/{service}`
- Протокол: JSON-RPC-like — POST `{"method": "...", "params": {...}}`
- Авторизация: `Authorization: Bearer {token}` (OAuth 2.0)
- 22 сервиса, 79 действий в каталоге (search+execute паттерн)

### Переменные окружения

| Переменная | Обязательная | По умолчанию | Описание |
|------------|:------------:|:------------:|----------|
| `YD_TOKEN` | да | — | OAuth-токен Яндекс Директа |
| `YD_CLIENT_LOGIN` | нет | — | Логин клиента для агентских аккаунтов |
| `YD_LANG` | нет | — | Язык ответов: `ru`, `en`, `uk` |
| `YD_TIMEOUT` | нет | `30` | Таймаут HTTP-запросов (секунды) |
| `YD_FILE_TIMEOUT` | нет | `120` | Таймаут отчётов Reports API (секунды) |

### Обновление MCP-сервера

Когда пользователь просит "обнови mcp yandex-direct":

1. Определить способ установки:
   ```bash
   which mcp-server-yandex-direct && pip show mcp-server-yandex-direct
   ```
2. Обновить пакет:
   - **pip:** `pip install --upgrade mcp-server-yandex-direct`
   - **uvx:** `uvx --upgrade mcp-server-yandex-direct`
3. Проверить версию:
   ```bash
   mcp-server-yandex-direct --version 2>/dev/null || python -c "import mcp_server_yandex_direct; print(mcp_server_yandex_direct.__version__)"
   ```
4. Сообщить пользователю новую версию и попросить перезапустить Claude Code (MCP-серверы перезапускаются при рестарте).

### README.md

При изменениях в коде обновлять [README.md](README.md):
- **Новое действие** — добавить строку в соответствующий файл `docs/<domain>.md` и обновить счётчик в таблице «Доступные действия».
- **Новая CLI-команда** — добавить в раздел «CLI-режим» → «Команды».
- **Новая переменная окружения** — добавить в таблицу «Переменные окружения».
- **Новый релиз** — обновить версию в бейджике.

### Правила кода

**Полные правила кода — в [development.md](development.md).** Ключевое:

- JSON от пользователя — только через `_parse_json(s, label)`, не голый `json.loads()`.
- Никогда не глотать исключения молча — всегда `log.warning()` с контекстом.
- Хелперы с читаемыми именами: `_to_json`, не `_j`.
- stdout зарезервирован для JSON-RPC — логи только в stderr.
- `resp.text` НИКОГДА не включать в исключения — только `log.debug()`.

### Правила Git и workflow

- **CRITICAL: НИКОГДА не коммить в master!** Все коммиты — только в рабочую ветку.
- **Все изменения — через Pull Request в master.** Создать ветку, закоммитить, сделать rebase на свежий master, запушить, создать PR.
- **ПЕРЕД КОММИТОМ проверить, не слита ли текущая ветка в master.** Если ветка уже слита (merged) — создать новую ветку от свежего master и делать новый PR. Никогда не пушить в уже слитую ветку.
- **MANDATORY BEFORE EVERY `git push`: rebase onto fresh master:**
  ```bash
  git checkout master && git remote update && git pull && git checkout - && git rebase master
  ```
- **NEVER use `git stash`.**
- **NEVER use merge commits. ALWAYS rebase.**
- **CRITICAL: НИКОГДА не читать содержимое `.env` файлов** — запрещено использовать `cat`, `Read`, `grep`, `head`, `tail` и любые другие способы чтения `.env`. Для загрузки переменных использовать **только** `source <path>/.env`. Для проверки наличия файла — только `test -f`. Для проверки наличия переменной — `source .env && test -n "$VAR_NAME"` (без вывода значения).
- **ПЕРЕД КАЖДЫМ КОММИТОМ** проверять все исходные файлы, тесты и документацию на наличие реальных персональных данных (ИНН, номера счетов, имена, адреса, телефоны, email). Заменять на вымышленные.
- **В КАЖДОМ PR** обновлять версию в `pyproject.toml`, `src/mcp_server_yandex_direct/__init__.py` и `server.json` (patch для фиксов, minor для новых фич).
- **ПЕРЕД публикацией в MCP-реестр** обязательно запускать `mcp-publisher validate` — проверяет `server.json` на соответствие схеме реестра.
- **Публикация** (PyPI + MCP-реестр одной командой):
  ```bash
  mcp-publisher validate && python3 -m build && twine upload dist/* && rm -rf ./dist && mcp-publisher login github && mcp-publisher publish
  ```
