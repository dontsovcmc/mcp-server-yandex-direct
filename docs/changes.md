# Отслеживание изменений

3 действия в домене `changes`.

| Команда | Описание | Параметры |
|---------|----------|-----------|
| `changes-check` | Проверить изменения в объектах аккаунта | `FieldNames` (list[str]) \*, `CampaignIds` (list[int]), `AdGroupIds` (list[int]), `AdIds` (list[int]), `Timestamp` (int) |
| `changes-check-dictionaries` | Проверить изменения в справочниках Яндекс Директа | — (без параметров) |
| `changes-check-campaigns` | Проверить изменения в кампаниях | `Timestamp` (int) |

\* — обязательный параметр
