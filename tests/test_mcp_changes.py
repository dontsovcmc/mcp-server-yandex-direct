"""Tests for Changes MCP tools."""

import pytest
from unittest.mock import patch
from mcp.shared.memory import create_connected_server_and_client_session
from mcp_server_yandex_direct.server import mcp


@pytest.mark.anyio
async def test_yd_changes_check():
    with patch("mcp_server_yandex_direct.server.YandexDirectAPI") as M:
        M.return_value.changes_check.return_value = {"Timestamp": "2026-01-01T00:00:00Z"}
        async with create_connected_server_and_client_session(mcp._mcp_server) as s:
            r = await s.call_tool("yd_changes_check", {"params_json": '{"FieldNames": ["CampaignIds"]}'})
            assert not r.isError


@pytest.mark.anyio
async def test_yd_changes_check_dictionaries():
    with patch("mcp_server_yandex_direct.server.YandexDirectAPI") as M:
        M.return_value.changes_check_dictionaries.return_value = {"Timestamp": "2026-01-01T00:00:00Z"}
        async with create_connected_server_and_client_session(mcp._mcp_server) as s:
            r = await s.call_tool("yd_changes_check_dictionaries", {})
            assert not r.isError


@pytest.mark.anyio
async def test_yd_changes_check_campaigns():
    with patch("mcp_server_yandex_direct.server.YandexDirectAPI") as M:
        M.return_value.changes_check_campaigns.return_value = {"Timestamp": "2026-01-01T00:00:00Z"}
        async with create_connected_server_and_client_session(mcp._mcp_server) as s:
            r = await s.call_tool("yd_changes_check_campaigns", {"params_json": '{"Timestamp": "2026-01-01T00:00:00Z"}'})
            assert not r.isError
