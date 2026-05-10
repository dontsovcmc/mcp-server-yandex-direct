# Кампании

8 действий в домене `campaigns`.

| Команда | Описание | Параметры |
|---------|----------|-----------|
| `campaigns-get` | Получить список кампаний с фильтрацией по критериям | `SelectionCriteria` (dict) \*, `FieldNames` (list[str]) \*, `Page` (dict) |
| `campaigns-add` | Создать новые кампании | `Campaigns` (list[dict]) \* |
| `campaigns-update` | Обновить параметры кампаний | `Campaigns` (list[dict]) \* |
| `campaigns-delete` :warning: | Удалить кампании | `SelectionCriteria` (dict) \* |
| `campaigns-suspend` | Остановить (приостановить) кампании | `SelectionCriteria` (dict) \* |
| `campaigns-resume` | Возобновить (запустить) кампании | `SelectionCriteria` (dict) \* |
| `campaigns-archive` | Архивировать кампании | `SelectionCriteria` (dict) \* |
| `campaigns-unarchive` | Разархивировать кампании | `SelectionCriteria` (dict) \* |

\* — обязательный параметр

:warning: — деструктивное действие
