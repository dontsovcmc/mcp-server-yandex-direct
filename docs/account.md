# Аккаунт и справочники

6 действий в домене `account` (справочники, клиенты, клиенты агентства).

| Команда | Описание | Параметры |
|---------|----------|-----------|
| `dictionaries-get` | Получить справочники Яндекс Директа (валюты, регионы, часовые пояса и др.) | `DictionaryNames` (list[str]) \* |
| `clients-get` | Получить параметры клиентского аккаунта | `FieldNames` (list[str]) \* |
| `clients-update` | Обновить параметры клиентского аккаунта | `Clients` (dict) \* |
| `agencyclients-get` | Получить список клиентов агентства | `SelectionCriteria` (dict) \*, `FieldNames` (list[str]) \*, `Page` (dict) |
| `agencyclients-add` | Создать клиентов агентства | `Clients` (list[dict]) \* |
| `agencyclients-update` | Обновить параметры клиентов агентства | `Clients` (list[dict]) \* |

\* — обязательный параметр
