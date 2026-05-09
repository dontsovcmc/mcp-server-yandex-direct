"""Tests for Feeds MCP tools."""

import pytest
from unittest.mock import patch
from mcp.shared.memory import create_connected_server_and_client_session
from mcp_server_yandex_direct.server import mcp


@pytest.mark.anyio
async def test_yd_feeds_get():
    with patch("mcp_server_yandex_direct.server.YandexDirectAPI") as M:
        M.return_value.feeds_get.return_value = {"Feeds": [{"Id": 110}]}
        async with create_connected_server_and_client_session(mcp._mcp_server) as s:
            r = await s.call_tool("yd_feeds_get", {"params_json": '{"SelectionCriteria": {}, "FieldNames": ["Id"]}'})
            assert not r.isError


@pytest.mark.anyio
async def test_yd_feeds_add():
    with patch("mcp_server_yandex_direct.server.YandexDirectAPI") as M:
        M.return_value.feeds_add.return_value = {"AddResults": [{"Id": 111}]}
        async with create_connected_server_and_client_session(mcp._mcp_server) as s:
            r = await s.call_tool("yd_feeds_add", {"params_json": '{}'})
            assert not r.isError


@pytest.mark.anyio
async def test_yd_feeds_update():
    with patch("mcp_server_yandex_direct.server.YandexDirectAPI") as M:
        M.return_value.feeds_update.return_value = {"UpdateResults": [{"Id": 110}]}
        async with create_connected_server_and_client_session(mcp._mcp_server) as s:
            r = await s.call_tool("yd_feeds_update", {"params_json": '{}'})
            assert not r.isError


@pytest.mark.anyio
async def test_yd_feeds_delete():
    with patch("mcp_server_yandex_direct.server.YandexDirectAPI") as M:
        M.return_value.feeds_delete.return_value = {"DeleteResults": [{"Id": 110}]}
        async with create_connected_server_and_client_session(mcp._mcp_server) as s:
            r = await s.call_tool("yd_feeds_delete", {"ids": "110"})
            assert not r.isError
