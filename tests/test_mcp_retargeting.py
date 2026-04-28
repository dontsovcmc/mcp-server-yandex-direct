"""Tests for RetargetingLists MCP tools."""

import json
import pytest
from unittest.mock import patch
from mcp.shared.memory import create_connected_server_and_client_session
from mcp_server_yandex_direct.server import mcp


@pytest.mark.anyio
async def test_yd_retargetinglists_get():
    with patch("mcp_server_yandex_direct.server.YandexDirectAPI") as M:
        M.return_value.retargetinglists_get.return_value = {"RetargetingLists": [{"Id": 90}]}
        async with create_connected_server_and_client_session(mcp._mcp_server) as s:
            r = await s.call_tool("yd_retargetinglists_get", {"params_json": '{"SelectionCriteria": {}, "FieldNames": ["Id"]}'})
            assert not r.isError


@pytest.mark.anyio
async def test_yd_retargetinglists_add():
    with patch("mcp_server_yandex_direct.server.YandexDirectAPI") as M:
        M.return_value.retargetinglists_add.return_value = {"AddResults": [{"Id": 91}]}
        async with create_connected_server_and_client_session(mcp._mcp_server) as s:
            r = await s.call_tool("yd_retargetinglists_add", {"params_json": '{}'})
            assert not r.isError


@pytest.mark.anyio
async def test_yd_retargetinglists_update():
    with patch("mcp_server_yandex_direct.server.YandexDirectAPI") as M:
        M.return_value.retargetinglists_update.return_value = {"UpdateResults": [{"Id": 90}]}
        async with create_connected_server_and_client_session(mcp._mcp_server) as s:
            r = await s.call_tool("yd_retargetinglists_update", {"params_json": '{}'})
            assert not r.isError


@pytest.mark.anyio
async def test_yd_retargetinglists_delete():
    with patch("mcp_server_yandex_direct.server.YandexDirectAPI") as M:
        M.return_value.retargetinglists_delete.return_value = {"DeleteResults": [{"Id": 90}]}
        async with create_connected_server_and_client_session(mcp._mcp_server) as s:
            r = await s.call_tool("yd_retargetinglists_delete", {"ids": "90"})
            assert not r.isError
