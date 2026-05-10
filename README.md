<!-- mcp-name: io.github.dontsovcmc/yandex-direct -->

# mcp-server-yandex-direct

[![Version](https://img.shields.io/badge/version-0.3.0-blue)](https://github.com/dontsovcmc/mcp-server-yandex-direct)

MCP-сервер, CLI-утилита и библиотека Pydantic-моделей для [Yandex Direct API v5](https://yandex.ru/dev/direct/doc/concepts/about.html).

- **MCP-сервер** — интеграция с Claude Code, Claude Desktop и другими MCP-клиентами
- **CLI-утилита** — работа с API из терминала, скрипты и автоматизация
- **Pydantic-модели** — типизированные модели API для использования в своих Python-программах

Все данные остаются на вашем компьютере — токен никуда не передаётся.

## Оглавление

- [Возможности](#возможности)
- [MCP-сервер](#mcp-сервер)
  - [Установка](#установка)
  - [Подключение к Claude Code](#подключение-к-claude-code)
  - [Подключение к Claude Desktop](#подключение-к-claude-desktop)
  - [Подключение через --mcp-config](#подключение-через---mcp-config)
  - [Примеры](#примеры-mcp)
- [CLI-утилита](#cli-утилита)
  - [Установка](#установка-cli)
  - [Использование](#использование-cli)
  - [Примеры команд](#примеры-команд)
- [Pydantic-модели](#pydantic-модели)
  - [Установка](#установка-библиотеки)
  - [Использование в своих программах](#использование-в-своих-программах)
- [Переменные окружения](#переменные-окружения)
- [Разработка](#разработка)
- [Лицензия](#лицензия)

## Возможности

79 действий для всех 22 сервисов Yandex Direct API v5 + Reports. Сервер использует паттерн **search+execute**: 2 MCP-инструмента (`yd_search`, `yd_execute`) вместо 79 — AI получает полные Pydantic-схемы параметров по запросу, не загружая весь контекст сразу.

### Кампании

| Action ID | CLI | Описание |
|-----------|-----|----------|
| `campaigns-get` | `campaigns-get` | Получить список кампаний |
| `campaigns-add` | `campaigns-add` | Создать кампании |
| `campaigns-update` | `campaigns-update` | Обновить кампании |
| `campaigns-delete` | `campaigns-delete` | Удалить кампании |
| `campaigns-suspend` | `campaigns-suspend` | Остановить кампании |
| `campaigns-resume` | `campaigns-resume` | Возобновить кампании |
| `campaigns-archive` | `campaigns-archive` | Архивировать кампании |
| `campaigns-unarchive` | `campaigns-unarchive` | Разархивировать кампании |

### Группы объявлений

| Action ID | CLI | Описание |
|-----------|-----|----------|
| `adgroups-get` | `adgroups-get` | Получить группы объявлений |
| `adgroups-add` | `adgroups-add` | Создать группы объявлений |
| `adgroups-update` | `adgroups-update` | Обновить группы объявлений |
| `adgroups-delete` | `adgroups-delete` | Удалить группы объявлений |

### Объявления

| Action ID | CLI | Описание |
|-----------|-----|----------|
| `ads-get` | `ads-get` | Получить объявления |
| `ads-add` | `ads-add` | Создать объявления |
| `ads-update` | `ads-update` | Обновить объявления |
| `ads-delete` | `ads-delete` | Удалить объявления |
| `ads-suspend` | `ads-suspend` | Остановить объявления |
| `ads-resume` | `ads-resume` | Возобновить объявления |
| `ads-archive` | `ads-archive` | Архивировать объявления |
| `ads-unarchive` | `ads-unarchive` | Разархивировать объявления |
| `ads-moderate` | `ads-moderate` | Отправить объявления на модерацию |

### Ключевые фразы

| Action ID | CLI | Описание |
|-----------|-----|----------|
| `keywords-get` | `keywords-get` | Получить ключевые фразы |
| `keywords-add` | `keywords-add` | Добавить ключевые фразы |
| `keywords-update` | `keywords-update` | Обновить ключевые фразы |
| `keywords-delete` | `keywords-delete` | Удалить ключевые фразы |
| `keywords-suspend` | `keywords-suspend` | Остановить ключевые фразы |
| `keywords-resume` | `keywords-resume` | Возобновить ключевые фразы |

### Ставки

| Action ID | CLI | Описание |
|-----------|-----|----------|
| `bids-get` | `bids-get` | Получить ставки |
| `bids-set` | `bids-set` | Назначить ставки |
| `bids-set-auto` | `bids-set-auto` | Назначить автоматические ставки |

### Корректировки ставок

| Action ID | CLI | Описание |
|-----------|-----|----------|
| `bidmodifiers-get` | `bidmodifiers-get` | Получить корректировки ставок |
| `bidmodifiers-add` | `bidmodifiers-add` | Добавить корректировки ставок |
| `bidmodifiers-delete` | `bidmodifiers-delete` | Удалить корректировки ставок |
| `bidmodifiers-set` | `bidmodifiers-set` | Установить корректировки ставок |

### Быстрые ссылки

| Action ID | CLI | Описание |
|-----------|-----|----------|
| `sitelinks-get` | `sitelinks-get` | Получить наборы быстрых ссылок |
| `sitelinks-add` | `sitelinks-add` | Добавить наборы быстрых ссылок |
| `sitelinks-delete` | `sitelinks-delete` | Удалить наборы быстрых ссылок |

### Изображения

| Action ID | CLI | Описание |
|-----------|-----|----------|
| `adimages-get` | `adimages-get` | Получить изображения |
| `adimages-add` | `adimages-add` | Добавить изображения |
| `adimages-delete` | `adimages-delete` | Удалить изображения |

### Видео

| Action ID | CLI | Описание |
|-----------|-----|----------|
| `advideos-get` | `advideos-get` | Получить видео |
| `advideos-add` | `advideos-add` | Добавить видео |

### Расширения объявлений

| Action ID | CLI | Описание |
|-----------|-----|----------|
| `adextensions-get` | `adextensions-get` | Получить расширения (уточнения) |
| `adextensions-add` | `adextensions-add` | Добавить расширения (уточнения) |
| `adextensions-delete` | `adextensions-delete` | Удалить расширения (уточнения) |

### Условия нацеливания на аудиторию

| Action ID | CLI | Описание |
|-----------|-----|----------|
| `audiencetargets-get` | `audiencetargets-get` | Получить условия нацеливания |
| `audiencetargets-add` | `audiencetargets-add` | Добавить условия нацеливания |
| `audiencetargets-delete` | `audiencetargets-delete` | Удалить условия нацеливания |
| `audiencetargets-suspend` | `audiencetargets-suspend` | Остановить условия нацеливания |
| `audiencetargets-resume` | `audiencetargets-resume` | Возобновить условия нацеливания |
| `audiencetargets-set-bids` | `audiencetargets-set-bids` | Назначить ставки для условий нацеливания |

### Условия ретаргетинга

| Action ID | CLI | Описание |
|-----------|-----|----------|
| `retargetinglists-get` | `retargetinglists-get` | Получить условия ретаргетинга |
| `retargetinglists-add` | `retargetinglists-add` | Добавить условия ретаргетинга |
| `retargetinglists-update` | `retargetinglists-update` | Обновить условия ретаргетинга |
| `retargetinglists-delete` | `retargetinglists-delete` | Удалить условия ретаргетинга |

### Наборы минус-фраз

| Action ID | CLI | Описание |
|-----------|-----|----------|
| `negkeywordsets-get` | `negkeywordsets-get` | Получить наборы минус-фраз |
| `negkeywordsets-add` | `negkeywordsets-add` | Добавить наборы минус-фраз |
| `negkeywordsets-update` | `negkeywordsets-update` | Обновить наборы минус-фраз |
| `negkeywordsets-delete` | `negkeywordsets-delete` | Удалить наборы минус-фраз |

### Фиды

| Action ID | CLI | Описание |
|-----------|-----|----------|
| `feeds-get` | `feeds-get` | Получить фиды (товарные каталоги) |
| `feeds-add` | `feeds-add` | Добавить фиды |
| `feeds-update` | `feeds-update` | Обновить фиды |
| `feeds-delete` | `feeds-delete` | Удалить фиды |

### Креативы

| Action ID | CLI | Описание |
|-----------|-----|----------|
| `creatives-get` | `creatives-get` | Получить креативы |
| `creatives-add` | `creatives-add` | Добавить креативы |

### Исследование ключевых фраз

| Action ID | CLI | Описание |
|-----------|-----|----------|
| `keywordsresearch-deduplicate` | `keywordsresearch-deduplicate` | Удалить дубли ключевых фраз |
| `keywordsresearch-has-search-volume` | `keywordsresearch-has-search-volume` | Проверить частотность ключевых фраз |

### Заявки

| Action ID | CLI | Описание |
|-----------|-----|----------|
| `leads-get` | `leads-get` | Получить заявки с Турбо-страниц |

### Отслеживание изменений

| Action ID | CLI | Описание |
|-----------|-----|----------|
| `changes-check` | `changes-check` | Проверить изменения объектов |
| `changes-check-dictionaries` | `changes-check-dictionaries` | Проверить изменения справочников |
| `changes-check-campaigns` | `changes-check-campaigns` | Проверить изменения кампаний |

### Справочники

| Action ID | CLI | Описание |
|-----------|-----|----------|
| `dictionaries-get` | `dictionaries-get` | Получить справочники (регионы, валюты, часовые пояса) |

### Клиенты

| Action ID | CLI | Описание |
|-----------|-----|----------|
| `clients-get` | `clients-get` | Получить информацию о клиенте |
| `clients-update` | `clients-update` | Обновить настройки клиента |

### Клиенты агентства

| Action ID | CLI | Описание |
|-----------|-----|----------|
| `agencyclients-get` | `agencyclients-get` | Получить клиентов агентства |
| `agencyclients-add` | `agencyclients-add` | Добавить клиентов агентства |
| `agencyclients-update` | `agencyclients-update` | Обновить клиентов агентства |

### Турбо-страницы

| Action ID | CLI | Описание |
|-----------|-----|----------|
| `turbopages-get` | `turbopages-get` | Получить Турбо-страницы |

### Отчёты

| Action ID | CLI | Описание |
|-----------|-----|----------|
| `reports-get` | `reports-get` | Получить отчёт (TSV/CSV) |

---

## MCP-сервер

### Установка

#### Шаг 1. Получить OAuth-токен

1. Войдите в [Яндекс Директ](https://direct.yandex.ru/)
2. Перейдите в **Настройки** → **API**
3. Создайте OAuth-токен с нужными правами
4. Скопируйте токен

#### Шаг 2. Подключить MCP-сервер

### Подключение к Claude Code

**Способ 1: через uvx** (не требует установки пакета)

> Требуется [uv](https://docs.astral.sh/uv/) — если не установлен:
> ```bash
> curl -LsSf https://astral.sh/uv/install.sh | sh
> ```

```bash
claude mcp add yandex-direct \
  -e YD_TOKEN=ваш_токен \
  -- uvx mcp-server-yandex-direct
```

**Способ 2: через pip**

```bash
pip install mcp-server-yandex-direct

claude mcp add yandex-direct \
  -e YD_TOKEN=ваш_токен \
  -- python -m mcp_server_yandex_direct
```

Для удаления:
```bash
claude mcp remove yandex-direct
```

### Подключение к Claude Desktop

Добавьте в конфигурационный файл:

| Клиент | ОС | Путь к файлу |
|--------|----|-------------|
| Claude Code | все | `~/.claude/settings.json` (секция `mcpServers`) |
| Claude Desktop | macOS | `~/Library/Application Support/Claude/claude_desktop_config.json` |
| Claude Desktop | Windows | `%APPDATA%\Claude\claude_desktop_config.json` |
| Claude Desktop | Linux | `~/.config/Claude/claude_desktop_config.json` |

**Через uvx:**
```json
{
  "mcpServers": {
    "yandex-direct": {
      "command": "uvx",
      "args": ["mcp-server-yandex-direct"],
      "env": {
        "YD_TOKEN": "ваш_токен"
      }
    }
  }
}
```

**Через pip** (после `pip install mcp-server-yandex-direct`):
```json
{
  "mcpServers": {
    "yandex-direct": {
      "command": "python",
      "args": ["-m", "mcp_server_yandex_direct"],
      "env": {
        "YD_TOKEN": "ваш_токен"
      }
    }
  }
}
```

### Подключение через --mcp-config

Подключает сервер только на время одной сессии Claude, не сохраняя в настройки. Токен хранится в отдельном `.env.mcp` файле, а не в конфиге Claude.

Из JSON-строки:
```bash
claude --mcp-config '{"yandex-direct":{"command":"bash","args":["-c","source ~/.env.mcp && exec uvx mcp-server-yandex-direct"]}}'
```

Из файла:
```bash
claude --mcp-config ~/mcp-servers.json
```

Пример `~/mcp-servers.json`:
```json
{
  "yandex-direct": {
    "command": "bash",
    "args": ["-c", "source ~/.env.mcp && exec uvx mcp-server-yandex-direct"]
  }
}
```

Пример `~/.env.mcp`:
```
YD_TOKEN=ваш_токен
```

#### Шаг 3. Проверить

Попросите Claude: *«Покажи список кампаний»* — он вызовет `yd_search`, получит схему `campaigns-get`, затем `yd_execute`.

### Примеры (MCP)

Claude автоматически использует `yd_search` для поиска нужного действия, затем `yd_execute` для его выполнения:

- «Покажи все активные кампании» → `yd_search("кампании")` → `yd_execute("campaigns-get", ...)`
- «Останови кампании 123, 456» → `yd_search("остановить кампании")` → `yd_execute("campaigns-suspend", ...)`
- «Покажи объявления кампании 789» → `yd_search("объявления")` → `yd_execute("ads-get", ...)`
- «Добавь ключевую фразу» → `yd_search("ключевые слова добавить")` → `yd_execute("keywords-add", ...)`
- «Получи справочник регионов» → `yd_search("справочники")` → `yd_execute("dictionaries-get", ...)`
- «Сделай отчёт по кампаниям за январь» → `yd_search("отчёт")` → `yd_execute("reports-get", ...)`

---

## CLI-утилита

### Установка (CLI)

```bash
pip install mcp-server-yandex-direct
```

Переменная окружения `YD_TOKEN` должна быть установлена:

```bash
export YD_TOKEN=ваш_токен
```

Или через файл:

```bash
mcp-server-yandex-direct --env /path/to/.env <command>
```

Формат файла — `KEY=VALUE`, по одной переменной на строку, `#`-комментарии.

### Использование (CLI)

Без аргументов запускается MCP-сервер, с командой — CLI. Все команды выводят JSON.

```bash
# Версия
mcp-server-yandex-direct --version

# Справка
mcp-server-yandex-direct --help
mcp-server-yandex-direct <command> --help
```

### Примеры команд

```bash
# Кампании
mcp-server-yandex-direct campaigns-get '{"SelectionCriteria": {}, "FieldNames": ["Id", "Name", "State"]}'
mcp-server-yandex-direct campaigns-suspend 123,456

# Объявления
mcp-server-yandex-direct ads-get '{"SelectionCriteria": {"CampaignIds": [123]}, "FieldNames": ["Id", "Type", "State"]}'
mcp-server-yandex-direct ads-moderate 789,101

# Ключевые фразы
mcp-server-yandex-direct keywords-get '{"SelectionCriteria": {"AdGroupIds": [111]}, "FieldNames": ["Id", "Keyword", "State"]}'

# Справочники
mcp-server-yandex-direct dictionaries-get Currencies,Regions

# Отчёты
mcp-server-yandex-direct reports-get '{"params": {"SelectionCriteria": {"DateFrom": "2026-01-01", "DateTo": "2026-04-28"}, "FieldNames": ["Date", "CampaignId", "Clicks", "Cost"], "ReportName": "My Report", "ReportType": "CAMPAIGN_PERFORMANCE_REPORT", "DateRangeType": "CUSTOM_DATE", "Format": "TSV"}}'
```

#### Пример вывода

```bash
$ mcp-server-yandex-direct campaigns-get '{"SelectionCriteria": {"States": ["ON"]}, "FieldNames": ["Id", "Name"]}'
{"Campaigns": [{"Id": 12345, "Name": "Летняя распродажа"}]}
```

---

## Pydantic-модели

Пакет содержит типизированные Pydantic-модели всех объектов API. Модели можно использовать в своих Python-программах для валидации данных и автодополнения в IDE.

### Установка (библиотеки)

```bash
pip install mcp-server-yandex-direct
```

### Использование в своих программах

```python
from mcp_server_yandex_direct.models.campaigns import CampaignsGetParams, CampaignsSelectionCriteria

# Валидация данных из API
params = CampaignsGetParams(
    SelectionCriteria=CampaignsSelectionCriteria(States=["ON"]),
    FieldNames=["Id", "Name", "State"],
)
print(params.model_dump_json())

# Валидация ответа
from mcp_server_yandex_direct.models.campaigns import CampaignsGetResult

data = {"Campaigns": [{"Id": 12345, "Name": "Тест", "State": "ON"}]}
result = CampaignsGetResult.model_validate(data)
print(result.Campaigns[0].Name)  # type-safe доступ к полям
```

Все модели используют `extra="allow"` для forward compatibility — неизвестные поля API не вызывают ошибок.

Полный список моделей: [`models/`](src/mcp_server_yandex_direct/models/)

---

## Переменные окружения

| Переменная | Обязательная | По умолчанию | Описание |
|------------|:------------:|:------------:|----------|
| `YD_TOKEN` | да | — | OAuth-токен Yandex Direct API |
| `YD_CLIENT_LOGIN` | нет | — | Логин клиента для агентских аккаунтов |
| `YD_LANG` | нет | — | Язык ответов: `ru`, `en`, `uk` |
| `YD_TIMEOUT` | нет | `30` | Таймаут HTTP-запросов к API (секунды) |
| `YD_FILE_TIMEOUT` | нет | `120` | Таймаут отчётов Reports API (секунды) |

## Разработка

```bash
pip install -e ".[test]"
ruff check src/ tests/
pytest tests/ -v
```

## Лицензия

MIT
