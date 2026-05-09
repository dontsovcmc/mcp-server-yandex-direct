"""Tests for NegativeKeywordSharedSets MCP tools."""

import pytest
from unittest.mock import patch
from mcp.shared.memory import create_connected_server_and_client_session
from mcp_server_yandex_direct.server import mcp


@pytest.mark.anyio
async def test_yd_negkeywordsets_get():
    with patch("mcp_server_yandex_direct.server.YandexDirectAPI") as M:
        M.return_value.negkeywordsets_get.return_value = {"NegativeKeywordSharedSets": [{"Id": 100}]}
        async with create_connected_server_and_client_session(mcp._mcp_server) as s:
            r = await s.call_tool("yd_negkeywordsets_get", {"params_json": '{"SelectionCriteria": {}, "FieldNames": ["Id"]}'})
            assert not r.isError


@pytest.mark.anyio
async def test_yd_negkeywordsets_add():
    with patch("mcp_server_yandex_direct.server.YandexDirectAPI") as M:
        M.return_value.negkeywordsets_add.return_value = {"AddResults": [{"Id": 101}]}
        async with create_connected_server_and_client_session(mcp._mcp_server) as s:
            r = await s.call_tool("yd_negkeywordsets_add", {"params_json": '{}'})
            assert not r.isError


@pytest.mark.anyio
async def test_yd_negkeywordsets_update():
    with patch("mcp_server_yandex_direct.server.YandexDirectAPI") as M:
        M.return_value.negkeywordsets_update.return_value = {"UpdateResults": [{"Id": 100}]}
        async with create_connected_server_and_client_session(mcp._mcp_server) as s:
            r = await s.call_tool("yd_negkeywordsets_update", {"params_json": '{}'})
            assert not r.isError


@pytest.mark.anyio
async def test_yd_negkeywordsets_delete():
    with patch("mcp_server_yandex_direct.server.YandexDirectAPI") as M:
        M.return_value.negkeywordsets_delete.return_value = {"DeleteResults": [{"Id": 100}]}
        async with create_connected_server_and_client_session(mcp._mcp_server) as s:
            r = await s.call_tool("yd_negkeywordsets_delete", {"ids": "100"})
            assert not r.isError
