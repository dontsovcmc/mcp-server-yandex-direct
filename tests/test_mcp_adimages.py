"""Tests for AdImages and AdVideos MCP tools."""

import json
import pytest
from unittest.mock import patch
from mcp.shared.memory import create_connected_server_and_client_session
from mcp_server_yandex_direct.server import mcp


# ── AdImages ──

@pytest.mark.anyio
async def test_yd_adimages_get():
    with patch("mcp_server_yandex_direct.server.YandexDirectAPI") as M:
        M.return_value.adimages_get.return_value = {"AdImages": [{"AdImageHash": "abc"}]}
        async with create_connected_server_and_client_session(mcp._mcp_server) as s:
            r = await s.call_tool("yd_adimages_get", {"params_json": '{"SelectionCriteria": {}, "FieldNames": ["AdImageHash"]}'})
            assert not r.isError


@pytest.mark.anyio
async def test_yd_adimages_add():
    with patch("mcp_server_yandex_direct.server.YandexDirectAPI") as M:
        M.return_value.adimages_add.return_value = {"AddResults": [{"Id": 1}]}
        async with create_connected_server_and_client_session(mcp._mcp_server) as s:
            r = await s.call_tool("yd_adimages_add", {"params_json": '{}'})
            assert not r.isError


@pytest.mark.anyio
async def test_yd_adimages_delete():
    with patch("mcp_server_yandex_direct.server.YandexDirectAPI") as M:
        M.return_value.adimages_delete.return_value = {"DeleteResults": [{"Id": 1}]}
        async with create_connected_server_and_client_session(mcp._mcp_server) as s:
            r = await s.call_tool("yd_adimages_delete", {"params_json": '{"SelectionCriteria": {"AdImageHashes": ["abc"]}}'})
            assert not r.isError


# ── AdVideos ──

@pytest.mark.anyio
async def test_yd_advideos_get():
    with patch("mcp_server_yandex_direct.server.YandexDirectAPI") as M:
        M.return_value.advideos_get.return_value = {"AdVideos": [{"Id": 60}]}
        async with create_connected_server_and_client_session(mcp._mcp_server) as s:
            r = await s.call_tool("yd_advideos_get", {"params_json": '{"SelectionCriteria": {}, "FieldNames": ["Id"]}'})
            assert not r.isError


@pytest.mark.anyio
async def test_yd_advideos_add():
    with patch("mcp_server_yandex_direct.server.YandexDirectAPI") as M:
        M.return_value.advideos_add.return_value = {"AddResults": [{"Id": 61}]}
        async with create_connected_server_and_client_session(mcp._mcp_server) as s:
            r = await s.call_tool("yd_advideos_add", {"params_json": '{}'})
            assert not r.isError
