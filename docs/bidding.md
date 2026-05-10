# Ставки и корректировки

7 действий в домене `bidding`.

| Команда | Описание | Параметры |
|---------|----------|-----------|
| `bids-get` | Получить ставки для ключевых слов | `SelectionCriteria` (dict) \*, `FieldNames` (list[str]) \*, `Page` (dict) |
| `bids-set` | Установить ставки для ключевых слов | `Bids` (list[dict]) \* |
| `bids-set-auto` | Установить автоматические ставки для ключевых слов | `Bids` (list[dict]) \* |
| `bidmodifiers-get` | Получить корректировки ставок | `SelectionCriteria` (dict) \*, `FieldNames` (list[str]) \*, `Page` (dict) |
| `bidmodifiers-add` | Добавить корректировки ставок | `BidModifiers` (list[dict]) \* |
| `bidmodifiers-delete` :warning: | Удалить корректировки ставок | `SelectionCriteria` (dict) \* |
| `bidmodifiers-set` | Установить корректировки ставок | `BidModifiers` (list[dict]) \* |

\* — обязательный параметр

:warning: — деструктивное действие
