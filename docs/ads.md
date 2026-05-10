# Объявления

9 действий в домене `ads`.

| Команда | Описание | Параметры |
|---------|----------|-----------|
| `ads-get` | Получить список объявлений | `SelectionCriteria` (dict) \*, `FieldNames` (list[str]) \*, `Page` (dict) |
| `ads-add` | Создать объявления | `Ads` (list[dict]) \* |
| `ads-update` | Обновить объявления | `Ads` (list[dict]) \* |
| `ads-delete` :warning: | Удалить объявления | `SelectionCriteria` (dict) \* |
| `ads-suspend` | Остановить (приостановить) объявления | `SelectionCriteria` (dict) \* |
| `ads-resume` | Возобновить (запустить) объявления | `SelectionCriteria` (dict) \* |
| `ads-archive` | Архивировать объявления | `SelectionCriteria` (dict) \* |
| `ads-unarchive` | Разархивировать объявления | `SelectionCriteria` (dict) \* |
| `ads-moderate` | Отправить объявления на модерацию | `SelectionCriteria` (dict) \* |

\* — обязательный параметр

:warning: — деструктивное действие
