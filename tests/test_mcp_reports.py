"""Tests for Reports MCP tool."""

import pytest
from unittest.mock import patch
from mcp.shared.memory import create_connected_server_and_client_session
from mcp_server_yandex_direct.server import mcp


@pytest.mark.anyio
async def test_yd_reports_get():
    with patch("mcp_server_yandex_direct.server.YandexDirectAPI") as M:
        M.return_value.reports_get.return_value = "Date\tCampaignId\tClicks\n2026-01-01\t123\t100"
        async with create_connected_server_and_client_session(mcp._mcp_server) as s:
            r = await s.call_tool("yd_reports_get", {"params_json": '{"params": {"SelectionCriteria": {}, "FieldNames": ["Date"]}}'})
            assert not r.isError
            assert "Date" in r.content[0].text
