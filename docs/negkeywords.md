# Минус-слова

4 действия в домене `negkeywords`.

| Команда | Описание | Параметры |
|---------|----------|-----------|
| `negkeywordsets-get` | Получить общие списки минус-слов | `SelectionCriteria` (dict) \*, `FieldNames` (list[str]) \*, `Page` (dict) |
| `negkeywordsets-add` | Создать общие списки минус-слов | `NegativeKeywordSharedSets` (list[dict]) \* |
| `negkeywordsets-update` | Обновить общие списки минус-слов | `NegativeKeywordSharedSets` (list[dict]) \* |
| `negkeywordsets-delete` :warning: | Удалить общие списки минус-слов | `SelectionCriteria` (dict) \* |

\* — обязательный параметр

:warning: — деструктивное действие
