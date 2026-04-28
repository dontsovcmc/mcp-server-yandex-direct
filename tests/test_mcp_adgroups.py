"""Tests for AdGroups MCP tools."""

import json
import pytest
from unittest.mock import patch
from mcp.shared.memory import create_connected_server_and_client_session
from mcp_server_yandex_direct.server import mcp


@pytest.mark.anyio
async def test_yd_adgroups_get():
    with patch("mcp_server_yandex_direct.server.YandexDirectAPI") as M:
        M.return_value.adgroups_get.return_value = {"AdGroups": [{"Id": 10, "Name": "G1"}]}
        async with create_connected_server_and_client_session(mcp._mcp_server) as s:
            r = await s.call_tool("yd_adgroups_get", {"params_json": '{"SelectionCriteria": {"CampaignIds": [1]}, "FieldNames": ["Id"]}'})
            assert not r.isError
            assert json.loads(r.content[0].text)["AdGroups"][0]["Id"] == 10


@pytest.mark.anyio
async def test_yd_adgroups_add():
    with patch("mcp_server_yandex_direct.server.YandexDirectAPI") as M:
        M.return_value.adgroups_add.return_value = {"AddResults": [{"Id": 20}]}
        async with create_connected_server_and_client_session(mcp._mcp_server) as s:
            r = await s.call_tool("yd_adgroups_add", {"params_json": '{}'})
            assert not r.isError


@pytest.mark.anyio
async def test_yd_adgroups_update():
    with patch("mcp_server_yandex_direct.server.YandexDirectAPI") as M:
        M.return_value.adgroups_update.return_value = {"UpdateResults": [{"Id": 10}]}
        async with create_connected_server_and_client_session(mcp._mcp_server) as s:
            r = await s.call_tool("yd_adgroups_update", {"params_json": '{}'})
            assert not r.isError


@pytest.mark.anyio
async def test_yd_adgroups_delete():
    with patch("mcp_server_yandex_direct.server.YandexDirectAPI") as M:
        M.return_value.adgroups_delete.return_value = {"DeleteResults": [{"Id": 10}]}
        async with create_connected_server_and_client_session(mcp._mcp_server) as s:
            r = await s.call_tool("yd_adgroups_delete", {"ids": "10,20"})
            assert not r.isError
