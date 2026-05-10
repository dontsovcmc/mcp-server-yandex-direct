"""MCP server for Yandex Direct API v5."""

import inspect
import json
import logging
import os
import sys

from mcp.server.fastmcp import FastMCP

from .yd_api import YandexDirectAPI

logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s", stream=sys.stderr)
log = logging.getLogger(__name__)

mcp = FastMCP(
    "yandex-direct",
    instructions=(
        "Yandex Direct API v5 server. "
        "Используй yd_search для поиска нужного действия и получения схемы параметров. "
        "Используй yd_execute для выполнения действия по ID. "
        "Доступные домены: campaigns, adgroups, ads, keywords, bidding, assets, audience, "
        "negkeywords, feeds, creatives, research, changes, account, leads, turbopages, reports."
    ),
)

_api_instance: YandexDirectAPI | None = None


def _get_api() -> YandexDirectAPI:
    global _api_instance
    if _api_instance is None:
        token = os.getenv("YD_TOKEN")
        if not token:
            raise RuntimeError("YD_TOKEN environment variable is required")
        client_login = os.getenv("YD_CLIENT_LOGIN", "")
        lang = os.getenv("YD_LANG", "")
        timeout = int(os.getenv("YD_TIMEOUT", "30"))
        file_timeout = int(os.getenv("YD_FILE_TIMEOUT", "120"))
        _api_instance = YandexDirectAPI(
            token, client_login=client_login, lang=lang,
            timeout=timeout, file_timeout=file_timeout,
        )
    return _api_instance


def _to_json(data) -> str:
    return json.dumps(data, ensure_ascii=False)


def _parse_json(s: str, label: str = "input"):
    """Parse JSON string with a clear error message."""
    try:
        return json.loads(s)
    except json.JSONDecodeError as e:
        raise ValueError(f"Invalid JSON in {label}: {e}") from e


def _search_actions(query: str, domain: str = "", limit: int = 10) -> list[dict]:
    from .actions import ACTIONS

    tokens = query.lower().split()
    results = []
    for action in ACTIONS.values():
        if domain and action.domain != domain:
            continue
        score = 0
        id_lower = action.id.lower()
        desc_lower = action.description.lower()
        for token in tokens:
            if action.id == query.lower():
                score += 1000
            if token in id_lower:
                score += 10
            if token in desc_lower:
                score += 5
            if any(token in kw.lower() for kw in action.keywords):
                score += 8
            if token in action.domain:
                score += 3
        if score > 0:
            results.append((score, action))
    results.sort(key=lambda x: -x[0])
    return [
        {
            "id": a.id,
            "domain": a.domain,
            "description": a.description,
            "is_destructive": a.is_destructive,
            "params_schema": a.params_model.model_json_schema() if a.params_model else None,
        }
        for _, a in results[:limit]
    ]


def _dispatch(action, api: YandexDirectAPI, params: dict):
    method = getattr(api, action.api_method)
    if action.params_model is None:
        return method()
    validated = action.params_model.model_validate(params)
    data = validated.model_dump(exclude_none=True)
    sig = inspect.signature(method)
    param_names = list(sig.parameters.keys())
    if len(param_names) == 1 and param_names[0] == "params":
        result = method(data)
    else:
        result = method(**data)
    if isinstance(result, str):
        return {"result": result}
    return result


@mcp.tool(annotations={"readOnlyHint": True})
def yd_search(query: str, domain: str = "", limit: int = 10) -> str:
    """Найти действия Yandex Direct API по намерению. Вызывай первым.

    Args:
        query: что нужно сделать (на русском или английском)
        domain: фильтр домена (campaigns, adgroups, ads, keywords, bidding, assets,
                audience, negkeywords, feeds, creatives, research, changes,
                account, leads, turbopages, reports)
        limit: максимум результатов (по умолчанию 10)
    """
    return _to_json(_search_actions(query, domain, limit))


@mcp.tool(annotations={"readOnlyHint": False})
def yd_execute(action: str, params_json: str = "{}") -> str:
    """Выполнить действие Yandex Direct API по ID.

    Используй yd_search для получения ID и схемы параметров.

    Args:
        action: ID действия из yd_search (например "campaigns-get", "ads-suspend")
        params_json: JSON-объект с параметрами согласно params_schema из yd_search
    """
    from .actions import ACTIONS

    if action not in ACTIONS:
        return _to_json({"error": f"Unknown action: {action}. Use yd_search to find valid actions."})
    act = ACTIONS[action]
    params = _parse_json(params_json, "params_json")
    result = _dispatch(act, _get_api(), params)
    return _to_json(result)
