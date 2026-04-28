# Разработка и диагностика

## Язык документации

Целевая аудитория — русскоязычные пользователи. README, документация и комментарии к коммитам — на русском языке.
Документация Яндекс API: https://yandex.ru/dev/direct/doc/concepts/about.html

## Как Claude запускает MCP-сервер

Claude Code запускает MCP-сервер как **дочерний процесс** (subprocess) и общается с ним по **stdin/stdout** через JSON-RPC 2.0:

```
Claude Code                          MCP-сервер
    │                                    │
    │── spawn subprocess ──────────────►│  (command + args из конфига)
    │                                    │
    │── stdin: {"method":"initialize"} ─►│  handshake (таймаут 10 сек)
    │◄─ stdout: {"capabilities":...} ───│
    │                                    │
    │── stdin: {"method":"tools/list"} ─►│  получить список инструментов
    │◄─ stdout: [tools...] ─────────────│
    │                                    │
    │        ✓ Connected                 │
```

**Важно:**
- Сервер **не запускается в login shell** — `~/.bashrc`, `~/.zshrc` не выполняются
- **PATH может быть урезан** — команда может не находиться, хотя в обычном терминале работает
- **stdout зарезервирован** для протокола — любой `print()` в stdout ломает соединение (используйте stderr)

## `✗ Failed to connect` — что делать

**1. Запустить сервер вручную:**

```bash
uvx mcp-server-yandex-direct
# или
mcp-server-yandex-direct
```

**2. Проверить что команда доступна:**

```bash
which mcp-server-yandex-direct
```

**3. Использовать абсолютный путь** (если PATH урезан):

```bash
which mcp-server-yandex-direct
# Использовать полный путь в конфиге
```

**4. Посмотреть логи Claude Code:**

```bash
# macOS:
tail -f ~/Library/Logs/Claude/mcp*.log
# Linux:
ls ~/.config/Claude/logs/
```

**5. Включить debug-режим:**

```bash
claude --mcp-debug
```

## Частые проблемы

| Симптом | Причина | Решение |
|---------|---------|---------|
| `command not found` | Пакет не установлен | `pip install mcp-server-yandex-direct` |
| `Failed to connect` | PATH урезан | Используйте абсолютный путь |
| `401 Unauthorized` | Неверный OAuth-токен | Проверьте `YD_TOKEN` |
| `403 Forbidden` | Недостаточно прав | Проверьте права токена в ЛК Директа |
| `No module named` | Другой Python | Используйте entry point вместо `python -m` |
