<!-- mcp-name: io.github.dontsovcmc/yandex-direct -->

# mcp-server-yandex-direct

[![Version](https://img.shields.io/badge/version-0.2.0-blue)](https://github.com/dontsovcmc/mcp-server-yandex-direct)

MCP-сервер для работы с [Yandex Direct API v5](https://yandex.ru/dev/direct/doc/concepts/about.html) через Claude Code, Claude Desktop и другие MCP-совместимые клиенты.

## Возможности

- 79 MCP-инструментов для всех 22 сервисов Yandex Direct API v5 + Reports
- CLI-интерфейс с 79 командами
- Pydantic-модели для валидации запросов/ответов
- Поддержка агентского режима (заголовок `Client-Login`)

## Установка

```bash
pip install mcp-server-yandex-direct
```

## Настройка

### Переменные окружения

| Переменная | Обязательная | По умолчанию | Описание |
|------------|:------------:|:------------:|----------|
| `YD_TOKEN` | Да | — | OAuth-токен Yandex Direct API |
| `YD_CLIENT_LOGIN` | Нет | — | Логин клиента для агентских аккаунтов |
| `YD_LANG` | Нет | — | Язык ответов: `ru`, `en`, `uk` |
| `YD_TIMEOUT` | Нет | `30` | Таймаут HTTP-запросов (секунды) |
| `YD_FILE_TIMEOUT` | Нет | `120` | Таймаут отчётов Reports API (секунды) |

Переменные можно загрузить из файла:

```bash
mcp-server-yandex-direct --env /path/to/.env
```

### Claude Code

Добавьте в настройки MCP:

```json
{
  "mcpServers": {
    "yandex-direct": {
      "command": "uvx",
      "args": ["mcp-server-yandex-direct"],
      "env": {
        "YD_TOKEN": "your-oauth-token"
      }
    }
  }
}
```

## Использование CLI

```bash
# Получить кампании
mcp-server-yandex-direct campaigns-get '{"SelectionCriteria": {}, "FieldNames": ["Id", "Name", "State"]}'

# Остановить кампании
mcp-server-yandex-direct campaigns-suspend 123,456

# Получить объявления кампании
mcp-server-yandex-direct ads-get '{"SelectionCriteria": {"CampaignIds": [123]}, "FieldNames": ["Id", "Type", "State"]}'

# Получить справочники
mcp-server-yandex-direct dictionaries-get Currencies,Regions

# Получить отчёт
mcp-server-yandex-direct reports-get '{"params": {"SelectionCriteria": {"DateFrom": "2026-01-01", "DateTo": "2026-04-28"}, "FieldNames": ["Date", "CampaignId", "Clicks", "Cost"], "ReportName": "My Report", "ReportType": "CAMPAIGN_PERFORMANCE_REPORT", "DateRangeType": "CUSTOM_DATE", "Format": "TSV"}}'
```

## Сервисы API

| Сервис | Описание | Методы | Кол-во |
|--------|----------|--------|:------:|
| Campaigns | Управление рекламными кампаниями | get, add, update, delete, suspend, resume, archive, unarchive | 8 |
| AdGroups | Управление группами объявлений | get, add, update, delete | 4 |
| Ads | Управление объявлениями | get, add, update, delete, suspend, resume, archive, unarchive, moderate | 9 |
| Keywords | Управление ключевыми фразами | get, add, update, delete, suspend, resume | 6 |
| Bids | Управление ставками | get, set, setAuto | 3 |
| BidModifiers | Корректировки ставок | get, add, delete, set | 4 |
| Sitelinks | Быстрые ссылки | get, add, delete | 3 |
| AdImages | Изображения для объявлений | get, add, delete | 3 |
| AdVideos | Видео для объявлений | get, add | 2 |
| AdExtensions | Расширения объявлений (уточнения) | get, add, delete | 3 |
| AudienceTargets | Условия нацеливания на аудиторию | get, add, delete, suspend, resume, setBids | 6 |
| RetargetingLists | Условия ретаргетинга и подбора аудитории | get, add, update, delete | 4 |
| NegativeKeywordSharedSets | Наборы минус-фраз | get, add, update, delete | 4 |
| Feeds | Фиды (товарные каталоги) | get, add, update, delete | 4 |
| Creatives | Креативы (видео, баннеры) | get, add | 2 |
| KeywordsResearch | Исследование ключевых фраз | deduplicate, hasSearchVolume | 2 |
| Leads | Заявки с Турбо-страниц | get | 1 |
| Changes | Отслеживание изменений | check, checkDictionaries, checkCampaigns | 3 |
| Dictionaries | Справочники (регионы, валюты, часовые пояса) | get | 1 |
| Clients | Управление параметрами клиента | get, update | 2 |
| AgencyClients | Управление клиентами агентства | get, add, update | 3 |
| TurboPages | Турбо-страницы | get | 1 |
| Reports | Отчёты (TSV/CSV) | get | 1 |
| **Итого** | | | **79** |

## Разработка

```bash
pip install -e ".[test]"
pytest tests/ -v
```

## Лицензия

MIT
