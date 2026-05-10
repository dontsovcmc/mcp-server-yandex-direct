# Фиды

4 действия в домене `feeds`.

| Команда | Описание | Параметры |
|---------|----------|-----------|
| `feeds-get` | Получить фиды (товарные фиды для динамических объявлений) | `SelectionCriteria` (dict) \*, `FieldNames` (list[str]) \*, `Page` (dict) |
| `feeds-add` | Создать фиды | `Feeds` (list[dict]) \* |
| `feeds-update` | Обновить фиды | `Feeds` (list[dict]) \* |
| `feeds-delete` :warning: | Удалить фиды | `SelectionCriteria` (dict) \* |

\* — обязательный параметр

:warning: — деструктивное действие
