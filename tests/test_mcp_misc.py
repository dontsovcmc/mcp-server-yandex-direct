"""Tests for misc MCP tools, invalid JSON, and API errors."""

import pytest
from unittest.mock import patch
from mcp.shared.memory import create_connected_server_and_client_session
from mcp_server_yandex_direct.server import mcp


# ── Creatives ──

@pytest.mark.anyio
async def test_yd_creatives_get():
    with patch("mcp_server_yandex_direct.server.YandexDirectAPI") as M:
        M.return_value.creatives_get.return_value = {"Creatives": [{"Id": 120}]}
        async with create_connected_server_and_client_session(mcp._mcp_server) as s:
            r = await s.call_tool("yd_creatives_get", {"params_json": '{"SelectionCriteria": {}, "FieldNames": ["Id"]}'})
            assert not r.isError


@pytest.mark.anyio
async def test_yd_creatives_add():
    with patch("mcp_server_yandex_direct.server.YandexDirectAPI") as M:
        M.return_value.creatives_add.return_value = {"AddResults": [{"Id": 121}]}
        async with create_connected_server_and_client_session(mcp._mcp_server) as s:
            r = await s.call_tool("yd_creatives_add", {"params_json": '{}'})
            assert not r.isError


# ── KeywordsResearch ──

@pytest.mark.anyio
async def test_yd_keywordsresearch_deduplicate():
    with patch("mcp_server_yandex_direct.server.YandexDirectAPI") as M:
        M.return_value.keywordsresearch_deduplicate.return_value = {"DeduplicateResults": []}
        async with create_connected_server_and_client_session(mcp._mcp_server) as s:
            r = await s.call_tool("yd_keywordsresearch_deduplicate", {"params_json": '{"Keywords": ["test"]}'})
            assert not r.isError


@pytest.mark.anyio
async def test_yd_keywordsresearch_has_search_volume():
    with patch("mcp_server_yandex_direct.server.YandexDirectAPI") as M:
        M.return_value.keywordsresearch_has_search_volume.return_value = {"HasSearchVolumeResults": []}
        async with create_connected_server_and_client_session(mcp._mcp_server) as s:
            r = await s.call_tool("yd_keywordsresearch_has_search_volume", {"params_json": '{"Keywords": [{"Keyword": "test"}]}'})
            assert not r.isError


# ── Leads ──

@pytest.mark.anyio
async def test_yd_leads_get():
    with patch("mcp_server_yandex_direct.server.YandexDirectAPI") as M:
        M.return_value.leads_get.return_value = {"Leads": [{"Id": 130}]}
        async with create_connected_server_and_client_session(mcp._mcp_server) as s:
            r = await s.call_tool("yd_leads_get", {"params_json": '{"SelectionCriteria": {}, "FieldNames": ["Id"]}'})
            assert not r.isError


# ── Dictionaries ──

@pytest.mark.anyio
async def test_yd_dictionaries_get():
    with patch("mcp_server_yandex_direct.server.YandexDirectAPI") as M:
        M.return_value.dictionaries_get.return_value = {"Currencies": [{"Currency": "RUB"}]}
        async with create_connected_server_and_client_session(mcp._mcp_server) as s:
            r = await s.call_tool("yd_dictionaries_get", {"names": "Currencies"})
            assert not r.isError


# ── TurboPages ──

@pytest.mark.anyio
async def test_yd_turbopages_get():
    with patch("mcp_server_yandex_direct.server.YandexDirectAPI") as M:
        M.return_value.turbopages_get.return_value = {"TurboPages": [{"Id": 140}]}
        async with create_connected_server_and_client_session(mcp._mcp_server) as s:
            r = await s.call_tool("yd_turbopages_get", {"params_json": '{"SelectionCriteria": {}, "FieldNames": ["Id"]}'})
            assert not r.isError


# ── Clients ──

@pytest.mark.anyio
async def test_yd_clients_get():
    with patch("mcp_server_yandex_direct.server.YandexDirectAPI") as M:
        M.return_value.clients_get.return_value = {"Clients": [{"Login": "user1"}]}
        async with create_connected_server_and_client_session(mcp._mcp_server) as s:
            r = await s.call_tool("yd_clients_get", {"params_json": '{"FieldNames": ["Login"]}'})
            assert not r.isError


@pytest.mark.anyio
async def test_yd_clients_update():
    with patch("mcp_server_yandex_direct.server.YandexDirectAPI") as M:
        M.return_value.clients_update.return_value = {"UpdateResults": [{"Id": 1}]}
        async with create_connected_server_and_client_session(mcp._mcp_server) as s:
            r = await s.call_tool("yd_clients_update", {"params_json": '{}'})
            assert not r.isError


# ── AgencyClients ──

@pytest.mark.anyio
async def test_yd_agencyclients_get():
    with patch("mcp_server_yandex_direct.server.YandexDirectAPI") as M:
        M.return_value.agencyclients_get.return_value = {"Clients": [{"Login": "client1"}]}
        async with create_connected_server_and_client_session(mcp._mcp_server) as s:
            r = await s.call_tool("yd_agencyclients_get", {"params_json": '{"SelectionCriteria": {}, "FieldNames": ["Login"]}'})
            assert not r.isError


@pytest.mark.anyio
async def test_yd_agencyclients_add():
    with patch("mcp_server_yandex_direct.server.YandexDirectAPI") as M:
        M.return_value.agencyclients_add.return_value = {"AddResults": [{"Id": 1}]}
        async with create_connected_server_and_client_session(mcp._mcp_server) as s:
            r = await s.call_tool("yd_agencyclients_add", {"params_json": '{}'})
            assert not r.isError


@pytest.mark.anyio
async def test_yd_agencyclients_update():
    with patch("mcp_server_yandex_direct.server.YandexDirectAPI") as M:
        M.return_value.agencyclients_update.return_value = {"UpdateResults": [{"Id": 1}]}
        async with create_connected_server_and_client_session(mcp._mcp_server) as s:
            r = await s.call_tool("yd_agencyclients_update", {"params_json": '{}'})
            assert not r.isError


# ── Security: invalid JSON ─────────────────────────────────────────


@pytest.mark.anyio
async def test_campaigns_get_invalid_json():
    with patch("mcp_server_yandex_direct.server.YandexDirectAPI"):
        async with create_connected_server_and_client_session(mcp._mcp_server) as s:
            r = await s.call_tool("yd_campaigns_get", {"params_json": "not-json"})
            assert r.isError
            assert "Invalid JSON" in r.content[0].text


@pytest.mark.anyio
async def test_ads_add_invalid_json():
    with patch("mcp_server_yandex_direct.server.YandexDirectAPI"):
        async with create_connected_server_and_client_session(mcp._mcp_server) as s:
            r = await s.call_tool("yd_ads_add", {"params_json": "{{bad"})
            assert r.isError
            assert "Invalid JSON" in r.content[0].text


@pytest.mark.anyio
async def test_reports_get_invalid_json():
    with patch("mcp_server_yandex_direct.server.YandexDirectAPI"):
        async with create_connected_server_and_client_session(mcp._mcp_server) as s:
            r = await s.call_tool("yd_reports_get", {"params_json": "[invalid"})
            assert r.isError
            assert "Invalid JSON" in r.content[0].text


@pytest.mark.anyio
async def test_reports_get_invalid_headers_json():
    with patch("mcp_server_yandex_direct.server.YandexDirectAPI"):
        async with create_connected_server_and_client_session(mcp._mcp_server) as s:
            r = await s.call_tool("yd_reports_get", {
                "params_json": "{}",
                "headers_json": "not-json",
            })
            assert r.isError
            assert "Invalid JSON" in r.content[0].text


# ── API errors ──────────────────────────────────────────────────────


@pytest.mark.anyio
async def test_campaigns_get_api_error():
    with patch("mcp_server_yandex_direct.server.YandexDirectAPI") as M:
        M.return_value.campaigns_get.side_effect = RuntimeError("campaigns.get -> HTTP 500")
        async with create_connected_server_and_client_session(mcp._mcp_server) as s:
            r = await s.call_tool("yd_campaigns_get", {"params_json": '{"SelectionCriteria": {}, "FieldNames": ["Id"]}'})
            assert r.isError
            assert "500" in r.content[0].text


@pytest.mark.anyio
async def test_ads_get_api_error():
    with patch("mcp_server_yandex_direct.server.YandexDirectAPI") as M:
        M.return_value.ads_get.side_effect = RuntimeError("ads.get -> HTTP 403")
        async with create_connected_server_and_client_session(mcp._mcp_server) as s:
            r = await s.call_tool("yd_ads_get", {"params_json": '{"SelectionCriteria": {}, "FieldNames": ["Id"]}'})
            assert r.isError
            assert "403" in r.content[0].text


@pytest.mark.anyio
async def test_reports_get_api_error():
    with patch("mcp_server_yandex_direct.server.YandexDirectAPI") as M:
        M.return_value.reports_get.side_effect = RuntimeError("reports -> HTTP 401")
        async with create_connected_server_and_client_session(mcp._mcp_server) as s:
            r = await s.call_tool("yd_reports_get", {"params_json": '{"params": {}}'})
            assert r.isError
            assert "401" in r.content[0].text
