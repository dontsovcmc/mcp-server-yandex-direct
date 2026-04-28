"""Tests for Campaigns MCP tools."""

import json
import pytest
from unittest.mock import patch
from mcp.shared.memory import create_connected_server_and_client_session
from mcp_server_yandex_direct.server import mcp


@pytest.mark.anyio
async def test_yd_campaigns_get():
    with patch("mcp_server_yandex_direct.server.YandexDirectAPI") as M:
        M.return_value.campaigns_get.return_value = {"Campaigns": [{"Id": 1, "Name": "Test"}]}
        async with create_connected_server_and_client_session(mcp._mcp_server) as s:
            r = await s.call_tool("yd_campaigns_get", {"params_json": '{"SelectionCriteria": {}, "FieldNames": ["Id"]}'})
            assert not r.isError
            assert json.loads(r.content[0].text)["Campaigns"][0]["Id"] == 1


@pytest.mark.anyio
async def test_yd_campaigns_add():
    with patch("mcp_server_yandex_direct.server.YandexDirectAPI") as M:
        M.return_value.campaigns_add.return_value = {"AddResults": [{"Id": 10}]}
        async with create_connected_server_and_client_session(mcp._mcp_server) as s:
            r = await s.call_tool("yd_campaigns_add", {"params_json": '{"Campaigns": [{"Name": "New", "StartDate": "2026-01-01"}]}'})
            assert not r.isError


@pytest.mark.anyio
async def test_yd_campaigns_update():
    with patch("mcp_server_yandex_direct.server.YandexDirectAPI") as M:
        M.return_value.campaigns_update.return_value = {"UpdateResults": [{"Id": 1}]}
        async with create_connected_server_and_client_session(mcp._mcp_server) as s:
            r = await s.call_tool("yd_campaigns_update", {"params_json": '{"Campaigns": [{"Id": 1, "Name": "Updated"}]}'})
            assert not r.isError


@pytest.mark.anyio
async def test_yd_campaigns_delete():
    with patch("mcp_server_yandex_direct.server.YandexDirectAPI") as M:
        M.return_value.campaigns_delete.return_value = {"DeleteResults": [{"Id": 1}]}
        async with create_connected_server_and_client_session(mcp._mcp_server) as s:
            r = await s.call_tool("yd_campaigns_delete", {"ids": "1,2"})
            assert not r.isError


@pytest.mark.anyio
async def test_yd_campaigns_suspend():
    with patch("mcp_server_yandex_direct.server.YandexDirectAPI") as M:
        M.return_value.campaigns_suspend.return_value = {"SuspendResults": [{"Id": 1}]}
        async with create_connected_server_and_client_session(mcp._mcp_server) as s:
            r = await s.call_tool("yd_campaigns_suspend", {"ids": "1"})
            assert not r.isError


@pytest.mark.anyio
async def test_yd_campaigns_resume():
    with patch("mcp_server_yandex_direct.server.YandexDirectAPI") as M:
        M.return_value.campaigns_resume.return_value = {"ResumeResults": [{"Id": 1}]}
        async with create_connected_server_and_client_session(mcp._mcp_server) as s:
            r = await s.call_tool("yd_campaigns_resume", {"ids": "1"})
            assert not r.isError


@pytest.mark.anyio
async def test_yd_campaigns_archive():
    with patch("mcp_server_yandex_direct.server.YandexDirectAPI") as M:
        M.return_value.campaigns_archive.return_value = {"ArchiveResults": [{"Id": 1}]}
        async with create_connected_server_and_client_session(mcp._mcp_server) as s:
            r = await s.call_tool("yd_campaigns_archive", {"ids": "1"})
            assert not r.isError


@pytest.mark.anyio
async def test_yd_campaigns_unarchive():
    with patch("mcp_server_yandex_direct.server.YandexDirectAPI") as M:
        M.return_value.campaigns_unarchive.return_value = {"UnarchiveResults": [{"Id": 1}]}
        async with create_connected_server_and_client_session(mcp._mcp_server) as s:
            r = await s.call_tool("yd_campaigns_unarchive", {"ids": "1"})
            assert not r.isError
