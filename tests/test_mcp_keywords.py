"""Tests for Keywords MCP tools."""

import json
import pytest
from unittest.mock import patch
from mcp.shared.memory import create_connected_server_and_client_session
from mcp_server_yandex_direct.server import mcp


@pytest.mark.anyio
async def test_yd_keywords_get():
    with patch("mcp_server_yandex_direct.server.YandexDirectAPI") as M:
        M.return_value.keywords_get.return_value = {"Keywords": [{"Id": 30, "Keyword": "test"}]}
        async with create_connected_server_and_client_session(mcp._mcp_server) as s:
            r = await s.call_tool("yd_keywords_get", {"params_json": '{"SelectionCriteria": {}, "FieldNames": ["Id"]}'})
            assert not r.isError
            assert json.loads(r.content[0].text)["Keywords"][0]["Keyword"] == "test"


@pytest.mark.anyio
async def test_yd_keywords_add():
    with patch("mcp_server_yandex_direct.server.YandexDirectAPI") as M:
        M.return_value.keywords_add.return_value = {"AddResults": [{"Id": 31}]}
        async with create_connected_server_and_client_session(mcp._mcp_server) as s:
            r = await s.call_tool("yd_keywords_add", {"params_json": '{}'})
            assert not r.isError


@pytest.mark.anyio
async def test_yd_keywords_update():
    with patch("mcp_server_yandex_direct.server.YandexDirectAPI") as M:
        M.return_value.keywords_update.return_value = {"UpdateResults": [{"Id": 30}]}
        async with create_connected_server_and_client_session(mcp._mcp_server) as s:
            r = await s.call_tool("yd_keywords_update", {"params_json": '{}'})
            assert not r.isError


@pytest.mark.anyio
async def test_yd_keywords_delete():
    with patch("mcp_server_yandex_direct.server.YandexDirectAPI") as M:
        M.return_value.keywords_delete.return_value = {"DeleteResults": [{"Id": 30}]}
        async with create_connected_server_and_client_session(mcp._mcp_server) as s:
            r = await s.call_tool("yd_keywords_delete", {"ids": "30"})
            assert not r.isError


@pytest.mark.anyio
async def test_yd_keywords_suspend():
    with patch("mcp_server_yandex_direct.server.YandexDirectAPI") as M:
        M.return_value.keywords_suspend.return_value = {"SuspendResults": [{"Id": 30}]}
        async with create_connected_server_and_client_session(mcp._mcp_server) as s:
            r = await s.call_tool("yd_keywords_suspend", {"ids": "30"})
            assert not r.isError


@pytest.mark.anyio
async def test_yd_keywords_resume():
    with patch("mcp_server_yandex_direct.server.YandexDirectAPI") as M:
        M.return_value.keywords_resume.return_value = {"ResumeResults": [{"Id": 30}]}
        async with create_connected_server_and_client_session(mcp._mcp_server) as s:
            r = await s.call_tool("yd_keywords_resume", {"ids": "30"})
            assert not r.isError
