# Группы объявлений

4 действия в домене `adgroups`.

| Команда | Описание | Параметры |
|---------|----------|-----------|
| `adgroups-get` | Получить список групп объявлений | `SelectionCriteria` (dict) \*, `FieldNames` (list[str]) \*, `Page` (dict) |
| `adgroups-add` | Создать группы объявлений | `AdGroups` (list[dict]) \* |
| `adgroups-update` | Обновить группы объявлений | `AdGroups` (list[dict]) \* |
| `adgroups-delete` :warning: | Удалить группы объявлений | `SelectionCriteria` (dict) \* |

\* — обязательный параметр

:warning: — деструктивное действие
