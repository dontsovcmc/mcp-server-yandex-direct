# Аудитории и ретаргетинг

10 действий в домене `audience` (условия нацеливания и списки ретаргетинга).

| Команда | Описание | Параметры |
|---------|----------|-----------|
| `audiencetargets-get` | Получить условия нацеливания на аудиторию | `SelectionCriteria` (dict) \*, `FieldNames` (list[str]) \*, `Page` (dict) |
| `audiencetargets-add` | Добавить условия нацеливания на аудиторию | `AudienceTargets` (list[dict]) \* |
| `audiencetargets-delete` :warning: | Удалить условия нацеливания на аудиторию | `SelectionCriteria` (dict) \* |
| `audiencetargets-suspend` | Остановить условия нацеливания на аудиторию | `SelectionCriteria` (dict) \* |
| `audiencetargets-resume` | Возобновить условия нацеливания на аудиторию | `SelectionCriteria` (dict) \* |
| `audiencetargets-set-bids` | Установить ставки для условий нацеливания | `Bids` (list[dict]) \* |
| `retargetinglists-get` | Получить списки ретаргетинга и аудиторий | `SelectionCriteria` (dict) \*, `FieldNames` (list[str]) \*, `Page` (dict) |
| `retargetinglists-add` | Создать списки ретаргетинга и аудиторий | `RetargetingLists` (list[dict]) \* |
| `retargetinglists-update` | Обновить списки ретаргетинга и аудиторий | `RetargetingLists` (list[dict]) \* |
| `retargetinglists-delete` :warning: | Удалить списки ретаргетинга и аудиторий | `SelectionCriteria` (dict) \* |

\* — обязательный параметр

:warning: — деструктивное действие
