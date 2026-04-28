"""Tests for AudienceTargets MCP tools."""

import json
import pytest
from unittest.mock import patch
from mcp.shared.memory import create_connected_server_and_client_session
from mcp_server_yandex_direct.server import mcp


@pytest.mark.anyio
async def test_yd_audiencetargets_get():
    with patch("mcp_server_yandex_direct.server.YandexDirectAPI") as M:
        M.return_value.audiencetargets_get.return_value = {"AudienceTargets": [{"Id": 80}]}
        async with create_connected_server_and_client_session(mcp._mcp_server) as s:
            r = await s.call_tool("yd_audiencetargets_get", {"params_json": '{"SelectionCriteria": {}, "FieldNames": ["Id"]}'})
            assert not r.isError


@pytest.mark.anyio
async def test_yd_audiencetargets_add():
    with patch("mcp_server_yandex_direct.server.YandexDirectAPI") as M:
        M.return_value.audiencetargets_add.return_value = {"AddResults": [{"Id": 81}]}
        async with create_connected_server_and_client_session(mcp._mcp_server) as s:
            r = await s.call_tool("yd_audiencetargets_add", {"params_json": '{}'})
            assert not r.isError


@pytest.mark.anyio
async def test_yd_audiencetargets_delete():
    with patch("mcp_server_yandex_direct.server.YandexDirectAPI") as M:
        M.return_value.audiencetargets_delete.return_value = {"DeleteResults": [{"Id": 80}]}
        async with create_connected_server_and_client_session(mcp._mcp_server) as s:
            r = await s.call_tool("yd_audiencetargets_delete", {"ids": "80"})
            assert not r.isError


@pytest.mark.anyio
async def test_yd_audiencetargets_suspend():
    with patch("mcp_server_yandex_direct.server.YandexDirectAPI") as M:
        M.return_value.audiencetargets_suspend.return_value = {"SuspendResults": [{"Id": 80}]}
        async with create_connected_server_and_client_session(mcp._mcp_server) as s:
            r = await s.call_tool("yd_audiencetargets_suspend", {"ids": "80"})
            assert not r.isError


@pytest.mark.anyio
async def test_yd_audiencetargets_resume():
    with patch("mcp_server_yandex_direct.server.YandexDirectAPI") as M:
        M.return_value.audiencetargets_resume.return_value = {"ResumeResults": [{"Id": 80}]}
        async with create_connected_server_and_client_session(mcp._mcp_server) as s:
            r = await s.call_tool("yd_audiencetargets_resume", {"ids": "80"})
            assert not r.isError


@pytest.mark.anyio
async def test_yd_audiencetargets_set_bids():
    with patch("mcp_server_yandex_direct.server.YandexDirectAPI") as M:
        M.return_value.audiencetargets_set_bids.return_value = {"SetBidsResults": [{"Id": 80}]}
        async with create_connected_server_and_client_session(mcp._mcp_server) as s:
            r = await s.call_tool("yd_audiencetargets_set_bids", {"params_json": '{}'})
            assert not r.isError
