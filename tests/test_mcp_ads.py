"""Tests for Ads MCP tools."""

import json
import pytest
from unittest.mock import patch
from mcp.shared.memory import create_connected_server_and_client_session
from mcp_server_yandex_direct.server import mcp


@pytest.mark.anyio
async def test_yd_ads_get():
    with patch("mcp_server_yandex_direct.server.YandexDirectAPI") as M:
        M.return_value.ads_get.return_value = {"Ads": [{"Id": 100, "Type": "TEXT_AD"}]}
        async with create_connected_server_and_client_session(mcp._mcp_server) as s:
            r = await s.call_tool("yd_ads_get", {"params_json": '{"SelectionCriteria": {}, "FieldNames": ["Id"]}'})
            assert not r.isError
            assert json.loads(r.content[0].text)["Ads"][0]["Type"] == "TEXT_AD"


@pytest.mark.anyio
async def test_yd_ads_add():
    with patch("mcp_server_yandex_direct.server.YandexDirectAPI") as M:
        M.return_value.ads_add.return_value = {"AddResults": [{"Id": 101}]}
        async with create_connected_server_and_client_session(mcp._mcp_server) as s:
            r = await s.call_tool("yd_ads_add", {"params_json": '{}'})
            assert not r.isError


@pytest.mark.anyio
async def test_yd_ads_update():
    with patch("mcp_server_yandex_direct.server.YandexDirectAPI") as M:
        M.return_value.ads_update.return_value = {"UpdateResults": [{"Id": 100}]}
        async with create_connected_server_and_client_session(mcp._mcp_server) as s:
            r = await s.call_tool("yd_ads_update", {"params_json": '{}'})
            assert not r.isError


@pytest.mark.anyio
async def test_yd_ads_delete():
    with patch("mcp_server_yandex_direct.server.YandexDirectAPI") as M:
        M.return_value.ads_delete.return_value = {"DeleteResults": [{"Id": 100}]}
        async with create_connected_server_and_client_session(mcp._mcp_server) as s:
            r = await s.call_tool("yd_ads_delete", {"ids": "100"})
            assert not r.isError


@pytest.mark.anyio
async def test_yd_ads_suspend():
    with patch("mcp_server_yandex_direct.server.YandexDirectAPI") as M:
        M.return_value.ads_suspend.return_value = {"SuspendResults": [{"Id": 100}]}
        async with create_connected_server_and_client_session(mcp._mcp_server) as s:
            r = await s.call_tool("yd_ads_suspend", {"ids": "100"})
            assert not r.isError


@pytest.mark.anyio
async def test_yd_ads_resume():
    with patch("mcp_server_yandex_direct.server.YandexDirectAPI") as M:
        M.return_value.ads_resume.return_value = {"ResumeResults": [{"Id": 100}]}
        async with create_connected_server_and_client_session(mcp._mcp_server) as s:
            r = await s.call_tool("yd_ads_resume", {"ids": "100"})
            assert not r.isError


@pytest.mark.anyio
async def test_yd_ads_archive():
    with patch("mcp_server_yandex_direct.server.YandexDirectAPI") as M:
        M.return_value.ads_archive.return_value = {"ArchiveResults": [{"Id": 100}]}
        async with create_connected_server_and_client_session(mcp._mcp_server) as s:
            r = await s.call_tool("yd_ads_archive", {"ids": "100"})
            assert not r.isError


@pytest.mark.anyio
async def test_yd_ads_unarchive():
    with patch("mcp_server_yandex_direct.server.YandexDirectAPI") as M:
        M.return_value.ads_unarchive.return_value = {"UnarchiveResults": [{"Id": 100}]}
        async with create_connected_server_and_client_session(mcp._mcp_server) as s:
            r = await s.call_tool("yd_ads_unarchive", {"ids": "100"})
            assert not r.isError


@pytest.mark.anyio
async def test_yd_ads_moderate():
    with patch("mcp_server_yandex_direct.server.YandexDirectAPI") as M:
        M.return_value.ads_moderate.return_value = {"ModerateResults": [{"Id": 100}]}
        async with create_connected_server_and_client_session(mcp._mcp_server) as s:
            r = await s.call_tool("yd_ads_moderate", {"ids": "100"})
            assert not r.isError
