"""Tests for search+execute pattern (yd_search, yd_execute tools)."""

import json
from unittest.mock import patch

import pytest
from mcp.shared.memory import create_connected_server_and_client_session

from mcp_server_yandex_direct.server import mcp


# ── yd_search tests ────────────────────────────────────────────────────────────

@pytest.mark.anyio
async def test_search_campaigns_by_russian_query():
    async with create_connected_server_and_client_session(mcp._mcp_server) as s:
        r = await s.call_tool("yd_search", {"query": "кампании", "domain": "campaigns"})
    assert not r.isError
    results = json.loads(r.content[0].text)
    ids = [a["id"] for a in results]
    assert "campaigns-get" in ids
    assert "campaigns-suspend" in ids


@pytest.mark.anyio
async def test_search_returns_params_schema():
    async with create_connected_server_and_client_session(mcp._mcp_server) as s:
        r = await s.call_tool("yd_search", {"query": "campaigns-get"})
    assert not r.isError
    results = json.loads(r.content[0].text)
    get_action = next(a for a in results if a["id"] == "campaigns-get")
    assert get_action["params_schema"] is not None
    assert "SelectionCriteria" in get_action["params_schema"]["properties"]


@pytest.mark.anyio
async def test_search_domain_filter():
    async with create_connected_server_and_client_session(mcp._mcp_server) as s:
        r = await s.call_tool("yd_search", {"query": "get", "domain": "reports"})
    assert not r.isError
    results = json.loads(r.content[0].text)
    assert all(a["domain"] == "reports" for a in results)
    assert any(a["id"] == "reports-get" for a in results)


@pytest.mark.anyio
async def test_search_unknown_domain_returns_empty():
    async with create_connected_server_and_client_session(mcp._mcp_server) as s:
        r = await s.call_tool("yd_search", {"query": "get", "domain": "nonexistent"})
    assert not r.isError
    results = json.loads(r.content[0].text)
    assert results == []


@pytest.mark.anyio
async def test_search_limit():
    async with create_connected_server_and_client_session(mcp._mcp_server) as s:
        r = await s.call_tool("yd_search", {"query": "get", "limit": 3})
    assert not r.isError
    results = json.loads(r.content[0].text)
    assert len(results) <= 3


@pytest.mark.anyio
async def test_search_changes_check_dictionaries_has_no_schema():
    async with create_connected_server_and_client_session(mcp._mcp_server) as s:
        r = await s.call_tool("yd_search", {"query": "changes-check-dictionaries"})
    assert not r.isError
    results = json.loads(r.content[0].text)
    action = next((a for a in results if a["id"] == "changes-check-dictionaries"), None)
    assert action is not None
    assert action["params_schema"] is None


# ── yd_execute happy path ──────────────────────────────────────────────────────

@pytest.mark.anyio
async def test_execute_campaigns_get():
    with patch("mcp_server_yandex_direct.server.YandexDirectAPI") as M:
        M.return_value.campaigns_get.return_value = {"Campaigns": [{"Id": 1}]}
        async with create_connected_server_and_client_session(mcp._mcp_server) as s:
            r = await s.call_tool("yd_execute", {
                "action": "campaigns-get",
                "params_json": '{"SelectionCriteria": {}, "FieldNames": ["Id"]}',
            })
    assert not r.isError
    data = json.loads(r.content[0].text)
    assert data["Campaigns"][0]["Id"] == 1


@pytest.mark.anyio
async def test_execute_campaigns_suspend_with_ids():
    with patch("mcp_server_yandex_direct.server.YandexDirectAPI") as M:
        M.return_value.campaigns_suspend.return_value = {"SuspendResults": [{"Id": 42}]}
        async with create_connected_server_and_client_session(mcp._mcp_server) as s:
            r = await s.call_tool("yd_execute", {
                "action": "campaigns-suspend",
                "params_json": '{"SelectionCriteria": {"Ids": [42]}}',
            })
    assert not r.isError
    data = json.loads(r.content[0].text)
    assert data["SuspendResults"][0]["Id"] == 42


@pytest.mark.anyio
async def test_execute_ads_delete():
    with patch("mcp_server_yandex_direct.server.YandexDirectAPI") as M:
        M.return_value.ads_delete.return_value = {"DeleteResults": [{"Id": 10}]}
        async with create_connected_server_and_client_session(mcp._mcp_server) as s:
            r = await s.call_tool("yd_execute", {
                "action": "ads-delete",
                "params_json": '{"SelectionCriteria": {"Ids": [10]}}',
            })
    assert not r.isError
    data = json.loads(r.content[0].text)
    assert data["DeleteResults"][0]["Id"] == 10


@pytest.mark.anyio
async def test_execute_changes_check_dictionaries_no_params():
    with patch("mcp_server_yandex_direct.server.YandexDirectAPI") as M:
        M.return_value.changes_check_dictionaries.return_value = {"Timestamp": "2026-01-01T00:00:00Z"}
        async with create_connected_server_and_client_session(mcp._mcp_server) as s:
            r = await s.call_tool("yd_execute", {"action": "changes-check-dictionaries"})
    assert not r.isError
    data = json.loads(r.content[0].text)
    assert "Timestamp" in data


@pytest.mark.anyio
async def test_execute_reports_get_returns_wrapped_tsv():
    with patch("mcp_server_yandex_direct.server.YandexDirectAPI") as M:
        M.return_value.reports_get.return_value = "ReportName\tClicks\nCampaign1\t100\n"
        async with create_connected_server_and_client_session(mcp._mcp_server) as s:
            r = await s.call_tool("yd_execute", {
                "action": "reports-get",
                "params_json": json.dumps({
                    "body": {
                        "SelectionCriteria": {"DateFrom": "2026-01-01", "DateTo": "2026-01-31"},
                        "FieldNames": ["CampaignName", "Clicks"],
                        "ReportName": "TestReport",
                        "ReportType": "CAMPAIGN_PERFORMANCE_REPORT",
                        "DateRangeType": "CUSTOM_DATE",
                        "Format": "TSV",
                        "IncludeVAT": "NO",
                        "IncludeDiscount": "NO",
                    }
                }),
            })
    assert not r.isError
    data = json.loads(r.content[0].text)
    assert "result" in data
    assert "Clicks" in data["result"]


@pytest.mark.anyio
async def test_execute_default_empty_params():
    with patch("mcp_server_yandex_direct.server.YandexDirectAPI") as M:
        M.return_value.changes_check_dictionaries.return_value = {"Timestamp": "2026-01-01T00:00:00Z"}
        async with create_connected_server_and_client_session(mcp._mcp_server) as s:
            # params_json defaults to "{}"
            r = await s.call_tool("yd_execute", {"action": "changes-check-dictionaries"})
    assert not r.isError


# ── yd_execute error handling ─────────────────────────────────────────────────

@pytest.mark.anyio
async def test_execute_invalid_json_is_error():
    async with create_connected_server_and_client_session(mcp._mcp_server) as s:
        r = await s.call_tool("yd_execute", {
            "action": "campaigns-get",
            "params_json": "not valid json",
        })
    assert r.isError


@pytest.mark.anyio
async def test_execute_unknown_action_returns_error_field():
    async with create_connected_server_and_client_session(mcp._mcp_server) as s:
        r = await s.call_tool("yd_execute", {"action": "nonexistent-action"})
    assert not r.isError
    data = json.loads(r.content[0].text)
    assert "error" in data
    assert "nonexistent-action" in data["error"]


@pytest.mark.anyio
async def test_execute_api_error_is_error():
    with patch("mcp_server_yandex_direct.server.YandexDirectAPI") as M:
        M.return_value.campaigns_get.side_effect = RuntimeError("campaigns.get -> HTTP 401")
        async with create_connected_server_and_client_session(mcp._mcp_server) as s:
            r = await s.call_tool("yd_execute", {
                "action": "campaigns-get",
                "params_json": '{"SelectionCriteria": {}, "FieldNames": ["Id"]}',
            })
    assert r.isError


# ── Catalog integrity ─────────────────────────────────────────────────────────

def test_catalog_has_79_actions():
    from mcp_server_yandex_direct.actions import ACTIONS
    assert len(ACTIONS) == 79


def test_catalog_all_api_methods_exist():
    from mcp_server_yandex_direct.actions import ACTIONS
    from mcp_server_yandex_direct.yd_api import YandexDirectAPI
    for action in ACTIONS.values():
        assert hasattr(YandexDirectAPI, action.api_method), (
            f"YandexDirectAPI missing method: {action.api_method} (action: {action.id})"
        )


def test_catalog_all_params_models_importable():
    from mcp_server_yandex_direct.actions import ACTIONS
    for action in ACTIONS.values():
        if action.params_model is not None:
            assert callable(action.params_model.model_validate), (
                f"params_model for {action.id} is not a valid Pydantic model"
            )


def test_catalog_destructive_actions():
    from mcp_server_yandex_direct.actions import ACTIONS
    destructive = {a.id for a in ACTIONS.values() if a.is_destructive}
    assert "campaigns-delete" in destructive
    assert "ads-delete" in destructive
    assert "keywords-delete" in destructive
    assert "campaigns-get" not in destructive
    assert "campaigns-suspend" not in destructive
