"""Tests for Sitelinks MCP tools."""

import json
import pytest
from unittest.mock import patch
from mcp.shared.memory import create_connected_server_and_client_session
from mcp_server_yandex_direct.server import mcp


@pytest.mark.anyio
async def test_yd_sitelinks_get():
    with patch("mcp_server_yandex_direct.server.YandexDirectAPI") as M:
        M.return_value.sitelinks_get.return_value = {"SitelinksSets": [{"Id": 50}]}
        async with create_connected_server_and_client_session(mcp._mcp_server) as s:
            r = await s.call_tool("yd_sitelinks_get", {"params_json": '{"SelectionCriteria": {}, "FieldNames": ["Id"]}'})
            assert not r.isError


@pytest.mark.anyio
async def test_yd_sitelinks_add():
    with patch("mcp_server_yandex_direct.server.YandexDirectAPI") as M:
        M.return_value.sitelinks_add.return_value = {"AddResults": [{"Id": 51}]}
        async with create_connected_server_and_client_session(mcp._mcp_server) as s:
            r = await s.call_tool("yd_sitelinks_add", {"params_json": '{}'})
            assert not r.isError


@pytest.mark.anyio
async def test_yd_sitelinks_delete():
    with patch("mcp_server_yandex_direct.server.YandexDirectAPI") as M:
        M.return_value.sitelinks_delete.return_value = {"DeleteResults": [{"Id": 50}]}
        async with create_connected_server_and_client_session(mcp._mcp_server) as s:
            r = await s.call_tool("yd_sitelinks_delete", {"ids": "50"})
            assert not r.isError
