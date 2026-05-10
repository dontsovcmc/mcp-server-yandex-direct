# Ключевые слова

6 действий в домене `keywords`.

| Команда | Описание | Параметры |
|---------|----------|-----------|
| `keywords-get` | Получить список ключевых слов | `SelectionCriteria` (dict) \*, `FieldNames` (list[str]) \*, `Page` (dict) |
| `keywords-add` | Добавить ключевые слова | `Keywords` (list[dict]) \* |
| `keywords-update` | Обновить ключевые слова | `Keywords` (list[dict]) \* |
| `keywords-delete` :warning: | Удалить ключевые слова | `SelectionCriteria` (dict) \* |
| `keywords-suspend` | Остановить ключевые слова | `SelectionCriteria` (dict) \* |
| `keywords-resume` | Возобновить ключевые слова | `SelectionCriteria` (dict) \* |

\* — обязательный параметр

:warning: — деструктивное действие
