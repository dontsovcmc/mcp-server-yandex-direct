"""Tests for AdExtensions MCP tools."""

import json
import pytest
from unittest.mock import patch
from mcp.shared.memory import create_connected_server_and_client_session
from mcp_server_yandex_direct.server import mcp


@pytest.mark.anyio
async def test_yd_adextensions_get():
    with patch("mcp_server_yandex_direct.server.YandexDirectAPI") as M:
        M.return_value.adextensions_get.return_value = {"AdExtensions": [{"Id": 70}]}
        async with create_connected_server_and_client_session(mcp._mcp_server) as s:
            r = await s.call_tool("yd_adextensions_get", {"params_json": '{"SelectionCriteria": {}, "FieldNames": ["Id"]}'})
            assert not r.isError


@pytest.mark.anyio
async def test_yd_adextensions_add():
    with patch("mcp_server_yandex_direct.server.YandexDirectAPI") as M:
        M.return_value.adextensions_add.return_value = {"AddResults": [{"Id": 71}]}
        async with create_connected_server_and_client_session(mcp._mcp_server) as s:
            r = await s.call_tool("yd_adextensions_add", {"params_json": '{}'})
            assert not r.isError


@pytest.mark.anyio
async def test_yd_adextensions_delete():
    with patch("mcp_server_yandex_direct.server.YandexDirectAPI") as M:
        M.return_value.adextensions_delete.return_value = {"DeleteResults": [{"Id": 70}]}
        async with create_connected_server_and_client_session(mcp._mcp_server) as s:
            r = await s.call_tool("yd_adextensions_delete", {"ids": "70"})
            assert not r.isError
