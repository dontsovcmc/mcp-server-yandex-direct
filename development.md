# Правила разработки MCP-серверов

## Безопасность

- **Валидация путей** — через `_safe_output_path()`. Никогда не принимать произвольные пути от LLM без проверки. Кроссплатформенная (Windows/Linux/macOS):
  - Разрешены только домашняя директория и системный temp (`tempfile.gettempdir()`, `/tmp`).
  - Запись в dotfiles/dotdirs под home запрещена (`~/.ssh`, `~/.bashrc`, `~/.config/...`) — проверка через `os.sep + "." in relative_path`.
  - Пути разворачиваются через `os.path.realpath()` (защита от `..` и симлинков).

```python
# Правильно
def _safe_output_path(path: str) -> str:
    resolved = os.path.realpath(path)
    home = os.path.realpath(os.path.expanduser("~"))
    tmp_dirs = {os.path.realpath(tempfile.gettempdir())}
    if os.path.isdir("/tmp"):
        tmp_dirs.add(os.path.realpath("/tmp"))
    is_under_home = resolved.startswith(home + os.sep)
    is_under_tmp = any(resolved.startswith(d + os.sep) for d in tmp_dirs)
    if not (is_under_home or is_under_tmp):
        raise ValueError(f"Output path must be under home or temp directory: {path}")
    if is_under_home and os.sep + "." in resolved[len(home):]:
        raise ValueError(f"Writing to hidden files/directories is not allowed: {path}")
    return resolved

# Неправильно
with open(path, "wb") as f:  # путь не проверен
    ...
```

- **Парсинг JSON от пользователя** — всегда через `_parse_json(text, label)`, не через голый `json.loads()`. Пользователь должен получить понятное сообщение об ошибке, а не стектрейс `JSONDecodeError`.

```python
# Правильно
_parse_json(items_json, "items_json")

# Неправильно
json.loads(items_json)
```

- **Секреты** — только через переменные окружения (`os.getenv`). Не хардкодить токены в коде или тестах. В тестах использовать вымышленные данные (`test-fake-token`, ИНН `7700000000`, счёт `40702810100000000001`).
- **Загрузка переменных окружения** — CLI и MCP-сервер должны поддерживать аргумент `--env <path>`. Если передан — загрузить переменные из указанного файла (формат `KEY=VALUE`, по одной на строку, `#`-комментарии). Если не передан — использовать стандартные переменные окружения. Реализация: `python-dotenv` (`load_dotenv(path)`). Аргумент `--env` добавляется в `cli.py` (argparse) и в `__init__.py` (для MCP-режима).
- **stdout зарезервирован** для JSON-RPC. Весь логгинг — только через `logging` в stderr.
- **HTTP-ответы в исключениях** — НИКОГДА не включать `resp.text` в `RuntimeError`. Тело ответа API может содержать персональные данные (ИНН, счета, имена), которые утекут в логи Claude, MCP-ответ или скриншоты. В исключение — только метод, путь и статус-код. Полный ответ логировать только на уровне `log.debug()`.

```python
# Правильно
log.debug("GET %s error body: %s", path, resp.text)
raise RuntimeError(f"GET {path} -> {resp.status_code}")

# Неправильно
raise RuntimeError(f"GET {path} -> {resp.status_code}: {resp.text}")
```

- **Проверка персональных данных перед коммитом** — grep на токены, ИНН, имена, email в коде, тестах и документации. Заменять на вымышленные.

## Обработка ошибок

- **Никогда не глотать исключения молча.** `except Exception:` без логирования запрещён. Всегда логировать через `log.warning()` или `log.error()` с контекстом (что делали, для какого объекта).
- **HTTP-ошибки** — API-клиент бросает `RuntimeError` с методом, путём и статус-кодом (без тела ответа). Не перехватывать эти ошибки в tool-функциях — FastMCP сам вернёт ошибку клиенту.
- **Ошибки валидации** — бросать `ValueError` / `RuntimeError` с понятным сообщением. Пример: `raise ValueError(f"Invalid JSON in {label}: {e}")`.

## Стиль кода

- **Именование** — функции-хелперы с префиксом `_`. Имена должны быть читаемыми: `_to_json`, `_parse_json`, `_safe_output_path`, а не `_j`, `_p`, `_s`.
- **Дублирование** — каждая tool-функция самодостаточна (вызывает `_get_api()`). Это допустимое повторение, а не дублирование. Не выносить в декораторы/контекстные менеджеры.
- **Типы** — аннотировать параметры и возвращаемые значения. `dict`, `list`, `str` — не `Dict`, `List`, `Str` (используем встроенные типы Python 3.10+).
- **Импорты** — стандартная библиотека → сторонние пакеты → локальные модули, разделённые пустой строкой. Не импортировать неиспользуемые имена.
- **Линтер** — `ruff check src/ tests/` должен проходить без ошибок перед коммитом. Правила: E (стиль), F (ошибки), W (предупреждения), I (импорты). Максимальная длина строки — 120 символов.

## Архитектура

- **Singleton API-клиент.** Кэшировать экземпляр HTTP-клиента в `server._api_instance` (один экземпляр на процесс). Не создавать новый API-клиент на каждый вызов.
- **Таймауты** — 30 секунд на обычные запросы, 120 секунд на отчёты. Настраиваемы через env-переменные (`YD_TIMEOUT`, `YD_FILE_TIMEOUT`). В коде использовать `self.timeout` и `self.file_timeout`, не хардкодить числа.
- **Tool-функции самодостаточны** — каждая вызывает `_get_api()` сама. Это допустимое повторение, а не дублирование. Не выносить в декораторы/контекстные менеджеры.
- **Server instructions.** Передавать `instructions=` в FastMCP, чтобы LLM знал как использовать сервер (какие инструменты вызывать первыми, как искать действия).

## Pydantic-модели

- **Модели в `models/`** — используются и для тестов, и в runtime.
- **`extra="allow"`** для forward compatibility с API.
- **`Field(description=...)`** для каждого поля — LLM видит полную JSON Schema.
- Не дублировать модели с одинаковыми полями.

## Логирование

- **`logging.basicConfig()`** вызывается **только один раз** — в `server.py`.
- В других модулях — только `log = logging.getLogger(__name__)` без `basicConfig`.
- Никогда не логировать токены, заголовки авторизации, персональные данные.

## Тесты

- **Мокаем API-клиент** на уровне класса: `@patch("mcp_server_yandex_direct.server.YandexDirectAPI")`. Кэш API сбрасывается автоматически через фикстуру в `conftest.py`.
- **Пути в тестах** — использовать `os.path.realpath()` для сравнения путей (на macOS `/tmp` → `/private/tmp`). Temp-файлы создавать в `/tmp` явно: `NamedTemporaryFile(dir="/tmp")`.
- **Тестовые данные** — вымышленные ИНН, счета, имена, токены. Никаких реальных персональных данных.
- **Обязательное покрытие** для каждого нового инструмента:
  1. **Happy path** — штатный вызов с корректными данными.
  2. **Невалидный JSON** — если инструмент принимает `*_json` параметр.
  3. **Ошибка API** — мок бросает `RuntimeError`, инструмент возвращает `isError=True`.
  4. **Path traversal** — если инструмент принимает `output_path` или `file_path`.

## Именование

- **CLI — kebab-case** (`campaigns-get`, `ads-add`). Стандартная конвенция CLI-инструментов.
- **MCP tools — snake_case с префиксом** сервиса (`yd_campaigns_get`, `yd_ads_add`). Префикс нужен для уникальности — у клиента может быть много MCP-серверов, имена не должны конфликтовать.
- **Паритет CLI и MCP.** Каждый MCP-инструмент должен иметь CLI-аналог. При добавлении нового tool — добавлять CLI-команду одновременно.

## Документация

- Целевая аудитория — русскоязычные пользователи. README, документация и комментарии к коммитам — на русском языке.
- Документация Яндекс API: https://yandex.ru/dev/direct/doc/concepts/about.html
- **Бейджик версии в README.** В начале README.md обязательно указывать бейджик с текущей версией: `[![Version](https://img.shields.io/badge/version-X.Y.Z-blue)](ссылка_на_репозиторий)`. Обновлять при каждом релизе.

## Как Claude запускает MCP-сервер

Claude Code запускает MCP-сервер как **дочерний процесс** (subprocess) и общается с ним по **stdin/stdout** через JSON-RPC 2.0:

```
Claude Code                          MCP-сервер
    │                                    │
    │── spawn subprocess ──────────────►│  (command + args из конфига)
    │                                    │
    │── stdin: {"method":"initialize"} ─►│  handshake (таймаут 10 сек)
    │◄─ stdout: {"capabilities":...} ───│
    │                                    │
    │── stdin: {"method":"tools/list"} ─►│  получить список инструментов
    │◄─ stdout: [tools...] ─────────────│
    │                                    │
    │        ✓ Connected                 │
```

**Важно:**
- Сервер **не запускается в login shell** — `~/.bashrc`, `~/.zshrc` не выполняются
- **PATH может быть урезан** — команда может не находиться, хотя в обычном терминале работает
- **stdout зарезервирован** для протокола — любой `print()` в stdout ломает соединение (используйте stderr)

## `✗ Failed to connect` — что делать

**1. Запустить сервер вручную** — самый быстрый способ увидеть ошибку:

```bash
# Если ставили через uvx:
uvx mcp-server-yandex-direct

# Если ставили через pip:
mcp-server-yandex-direct
```

**2. Проверить что команда доступна:**

```bash
which mcp-server-yandex-direct   # или: which uvx
```

Если `not found` — пакет не установлен или не в PATH.

**3. Использовать абсолютный путь** (если PATH урезан):

```bash
# Узнать полный путь:
which mcp-server-yandex-direct
# Использовать полный путь в конфиге
```

**4. Посмотреть логи Claude Code:**

```bash
# macOS:
ls ~/Library/Logs/Claude/
tail -f ~/Library/Logs/Claude/mcp*.log

# Windows:
dir %APPDATA%\Claude\logs\

# Linux:
ls ~/.config/Claude/logs/
```

**5. Включить debug-режим:**

```bash
claude --mcp-debug          # отладка протокола MCP
claude --verbose             # подробный вывод
CLAUDE_DEBUG=1 claude        # максимум логов
```

## Частые проблемы

| Симптом | Причина | Решение |
|---------|---------|---------|
| `command not found` | Пакет не установлен или не в PATH | `pip install mcp-server-yandex-direct` или используйте абсолютный путь |
| `Failed to connect` без ошибки | Claude не может найти команду из-за урезанного PATH | Используйте абсолютный путь к команде |
| Сервер запускается вручную, но не в Claude | PATH в Claude отличается от PATH в терминале | Используйте абсолютный путь |
| `No module named mcp_server_*` | pip установил в другой Python | Используйте entry point вместо `python -m` |
| `401 Unauthorized` | Неверный OAuth-токен | Проверьте `YD_TOKEN` в ЛК Яндекс Директа |
| `403 Forbidden` | Недостаточно прав | Проверьте права токена |
| `429 Too Many Requests` | Превышен лимит запросов | Уменьшите частоту запросов |
| Таймаут при подключении | Сервер не ответил за 10 секунд | Проверьте сеть и токен |

## Публикация версии

Валидация, сборка, загрузка в PyPI и публикация в MCP Registry — одной командой:

```bash
mcp-publisher validate && python3 -m build && twine upload dist/* && rm -rf ./dist && mcp-publisher login github && mcp-publisher publish
```
