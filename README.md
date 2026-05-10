<!-- mcp-name: io.github.dontsovcmc/yandex-direct -->

# mcp-server-yandex-direct

[![Version](https://img.shields.io/badge/version-0.2.0-blue)](https://github.com/dontsovcmc/mcp-server-yandex-direct)

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

79 инструментов для всех 22 сервисов Yandex Direct API v5 + Reports.

### Кампании

| Инструмент | CLI | Описание |
|------------|-----|----------|
| `yd_campaigns_get` | `campaigns-get` | Получить список кампаний |
| `yd_campaigns_add` | `campaigns-add` | Создать кампании |
| `yd_campaigns_update` | `campaigns-update` | Обновить кампании |
| `yd_campaigns_delete` | `campaigns-delete` | Удалить кампании |
| `yd_campaigns_suspend` | `campaigns-suspend` | Остановить кампании |
| `yd_campaigns_resume` | `campaigns-resume` | Возобновить кампании |
| `yd_campaigns_archive` | `campaigns-archive` | Архивировать кампании |
| `yd_campaigns_unarchive` | `campaigns-unarchive` | Разархивировать кампании |

### Группы объявлений

| Инструмент | CLI | Описание |
|------------|-----|----------|
| `yd_adgroups_get` | `adgroups-get` | Получить группы объявлений |
| `yd_adgroups_add` | `adgroups-add` | Создать группы объявлений |
| `yd_adgroups_update` | `adgroups-update` | Обновить группы объявлений |
| `yd_adgroups_delete` | `adgroups-delete` | Удалить группы объявлений |

### Объявления

| Инструмент | CLI | Описание |
|------------|-----|----------|
| `yd_ads_get` | `ads-get` | Получить объявления |
| `yd_ads_add` | `ads-add` | Создать объявления |
| `yd_ads_update` | `ads-update` | Обновить объявления |
| `yd_ads_delete` | `ads-delete` | Удалить объявления |
| `yd_ads_suspend` | `ads-suspend` | Остановить объявления |
| `yd_ads_resume` | `ads-resume` | Возобновить объявления |
| `yd_ads_archive` | `ads-archive` | Архивировать объявления |
| `yd_ads_unarchive` | `ads-unarchive` | Разархивировать объявления |
| `yd_ads_moderate` | `ads-moderate` | Отправить объявления на модерацию |

### Ключевые фразы

| Инструмент | CLI | Описание |
|------------|-----|----------|
| `yd_keywords_get` | `keywords-get` | Получить ключевые фразы |
| `yd_keywords_add` | `keywords-add` | Добавить ключевые фразы |
| `yd_keywords_update` | `keywords-update` | Обновить ключевые фразы |
| `yd_keywords_delete` | `keywords-delete` | Удалить ключевые фразы |
| `yd_keywords_suspend` | `keywords-suspend` | Остановить ключевые фразы |
| `yd_keywords_resume` | `keywords-resume` | Возобновить ключевые фразы |

### Ставки

| Инструмент | CLI | Описание |
|------------|-----|----------|
| `yd_bids_get` | `bids-get` | Получить ставки |
| `yd_bids_set` | `bids-set` | Назначить ставки |
| `yd_bids_set_auto` | `bids-set-auto` | Назначить автоматические ставки |

### Корректировки ставок

| Инструмент | CLI | Описание |
|------------|-----|----------|
| `yd_bidmodifiers_get` | `bidmodifiers-get` | Получить корректировки ставок |
| `yd_bidmodifiers_add` | `bidmodifiers-add` | Добавить корректировки ставок |
| `yd_bidmodifiers_delete` | `bidmodifiers-delete` | Удалить корректировки ставок |
| `yd_bidmodifiers_set` | `bidmodifiers-set` | Установить корректировки ставок |

### Быстрые ссылки

| Инструмент | CLI | Описание |
|------------|-----|----------|
| `yd_sitelinks_get` | `sitelinks-get` | Получить наборы быстрых ссылок |
| `yd_sitelinks_add` | `sitelinks-add` | Добавить наборы быстрых ссылок |
| `yd_sitelinks_delete` | `sitelinks-delete` | Удалить наборы быстрых ссылок |

### Изображения

| Инструмент | CLI | Описание |
|------------|-----|----------|
| `yd_adimages_get` | `adimages-get` | Получить изображения |
| `yd_adimages_add` | `adimages-add` | Добавить изображения |
| `yd_adimages_delete` | `adimages-delete` | Удалить изображения |

### Видео

| Инструмент | CLI | Описание |
|------------|-----|----------|
| `yd_advideos_get` | `advideos-get` | Получить видео |
| `yd_advideos_add` | `advideos-add` | Добавить видео |

### Расширения объявлений

| Инструмент | CLI | Описание |
|------------|-----|----------|
| `yd_adextensions_get` | `adextensions-get` | Получить расширения (уточнения) |
| `yd_adextensions_add` | `adextensions-add` | Добавить расширения (уточнения) |
| `yd_adextensions_delete` | `adextensions-delete` | Удалить расширения (уточнения) |

### Условия нацеливания на аудиторию

| Инструмент | CLI | Описание |
|------------|-----|----------|
| `yd_audiencetargets_get` | `audiencetargets-get` | Получить условия нацеливания |
| `yd_audiencetargets_add` | `audiencetargets-add` | Добавить условия нацеливания |
| `yd_audiencetargets_delete` | `audiencetargets-delete` | Удалить условия нацеливания |
| `yd_audiencetargets_suspend` | `audiencetargets-suspend` | Остановить условия нацеливания |
| `yd_audiencetargets_resume` | `audiencetargets-resume` | Возобновить условия нацеливания |
| `yd_audiencetargets_set_bids` | `audiencetargets-set-bids` | Назначить ставки для условий нацеливания |

### Условия ретаргетинга

| Инструмент | CLI | Описание |
|------------|-----|----------|
| `yd_retargetinglists_get` | `retargetinglists-get` | Получить условия ретаргетинга |
| `yd_retargetinglists_add` | `retargetinglists-add` | Добавить условия ретаргетинга |
| `yd_retargetinglists_update` | `retargetinglists-update` | Обновить условия ретаргетинга |
| `yd_retargetinglists_delete` | `retargetinglists-delete` | Удалить условия ретаргетинга |

### Наборы минус-фраз

| Инструмент | CLI | Описание |
|------------|-----|----------|
| `yd_negkeywordsets_get` | `negkeywordsets-get` | Получить наборы минус-фраз |
| `yd_negkeywordsets_add` | `negkeywordsets-add` | Добавить наборы минус-фраз |
| `yd_negkeywordsets_update` | `negkeywordsets-update` | Обновить наборы минус-фраз |
| `yd_negkeywordsets_delete` | `negkeywordsets-delete` | Удалить наборы минус-фраз |

### Фиды

| Инструмент | CLI | Описание |
|------------|-----|----------|
| `yd_feeds_get` | `feeds-get` | Получить фиды (товарные каталоги) |
| `yd_feeds_add` | `feeds-add` | Добавить фиды |
| `yd_feeds_update` | `feeds-update` | Обновить фиды |
| `yd_feeds_delete` | `feeds-delete` | Удалить фиды |

### Креативы

| Инструмент | CLI | Описание |
|------------|-----|----------|
| `yd_creatives_get` | `creatives-get` | Получить креативы |
| `yd_creatives_add` | `creatives-add` | Добавить креативы |

### Исследование ключевых фраз

| Инструмент | CLI | Описание |
|------------|-----|----------|
| `yd_keywordsresearch_deduplicate` | `keywordsresearch-deduplicate` | Удалить дубли ключевых фраз |
| `yd_keywordsresearch_has_search_volume` | `keywordsresearch-has-search-volume` | Проверить частотность ключевых фраз |

### Заявки

| Инструмент | CLI | Описание |
|------------|-----|----------|
| `yd_leads_get` | `leads-get` | Получить заявки с Турбо-страниц |

### Отслеживание изменений

| Инструмент | CLI | Описание |
|------------|-----|----------|
| `yd_changes_check` | `changes-check` | Проверить изменения объектов |
| `yd_changes_check_dictionaries` | `changes-check-dictionaries` | Проверить изменения справочников |
| `yd_changes_check_campaigns` | `changes-check-campaigns` | Проверить изменения кампаний |

### Справочники

| Инструмент | CLI | Описание |
|------------|-----|----------|
| `yd_dictionaries_get` | `dictionaries-get` | Получить справочники (регионы, валюты, часовые пояса) |

### Клиенты

| Инструмент | CLI | Описание |
|------------|-----|----------|
| `yd_clients_get` | `clients-get` | Получить информацию о клиенте |
| `yd_clients_update` | `clients-update` | Обновить настройки клиента |

### Клиенты агентства

| Инструмент | CLI | Описание |
|------------|-----|----------|
| `yd_agencyclients_get` | `agencyclients-get` | Получить клиентов агентства |
| `yd_agencyclients_add` | `agencyclients-add` | Добавить клиентов агентства |
| `yd_agencyclients_update` | `agencyclients-update` | Обновить клиентов агентства |

### Турбо-страницы

| Инструмент | CLI | Описание |
|------------|-----|----------|
| `yd_turbopages_get` | `turbopages-get` | Получить Турбо-страницы |

### Отчёты

| Инструмент | CLI | Описание |
|------------|-----|----------|
| `yd_reports_get` | `reports-get` | Получить отчёт (TSV/CSV) |

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

Попросите Claude: *«Покажи список кампаний»* — он вызовет `yd_campaigns_get`.

### Примеры (MCP)

- «Покажи все активные кампании» → `yd_campaigns_get`
- «Останови кампании 123, 456» → `yd_campaigns_suspend`
- «Покажи объявления кампании 789» → `yd_ads_get`
- «Добавь ключевую фразу "купить телефон" в группу 111» → `yd_keywords_add`
- «Получи справочник регионов» → `yd_dictionaries_get`
- «Сделай отчёт по кампаниям за январь» → `yd_reports_get`

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
