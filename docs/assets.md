# Материалы объявлений

11 действий в домене `assets` (быстрые ссылки, изображения, видео, расширения).

| Команда | Описание | Параметры |
|---------|----------|-----------|
| `sitelinks-get` | Получить наборы быстрых ссылок | `SelectionCriteria` (dict) \*, `FieldNames` (list[str]) \*, `Page` (dict) |
| `sitelinks-add` | Создать наборы быстрых ссылок | `SitelinksSets` (list[dict]) \* |
| `sitelinks-delete` :warning: | Удалить наборы быстрых ссылок | `SelectionCriteria` (dict) \* |
| `adimages-get` | Получить изображения для объявлений | `SelectionCriteria` (dict) \*, `FieldNames` (list[str]) \*, `Page` (dict) |
| `adimages-add` | Загрузить изображения для объявлений | `AdImages` (list[dict]) \* |
| `adimages-delete` :warning: | Удалить изображения для объявлений | `SelectionCriteria` (dict) \* |
| `advideos-get` | Получить видео для объявлений | `SelectionCriteria` (dict) \*, `FieldNames` (list[str]) \*, `Page` (dict) |
| `advideos-add` | Загрузить видео для объявлений | `AdVideos` (list[dict]) \* |
| `adextensions-get` | Получить расширения объявлений (уточнения, цены) | `SelectionCriteria` (dict) \*, `FieldNames` (list[str]) \*, `Page` (dict) |
| `adextensions-add` | Добавить расширения объявлений | `AdExtensions` (list[dict]) \* |
| `adextensions-delete` :warning: | Удалить расширения объявлений | `SelectionCriteria` (dict) \* |

\* — обязательный параметр

:warning: — деструктивное действие
