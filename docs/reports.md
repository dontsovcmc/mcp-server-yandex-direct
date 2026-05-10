# Отчёты

1 действие в домене `reports`.

| Команда | Описание | Параметры |
|---------|----------|-----------|
| `reports-get` | Получить отчёт Яндекс Директа (TSV/CSV) по заданным полям и критериям | `body` (dict) \*, `extra_headers` (dict) |

`body` содержит параметры отчёта: `SelectionCriteria`, `FieldNames`, `ReportName`, `ReportType`, `DateRangeType`, `Format` и другие.

\* — обязательный параметр
