"""Tests for Bids and BidModifiers MCP tools."""

import pytest
from unittest.mock import patch
from mcp.shared.memory import create_connected_server_and_client_session
from mcp_server_yandex_direct.server import mcp


# ── Bids ──

@pytest.mark.anyio
async def test_yd_bids_get():
    with patch("mcp_server_yandex_direct.server.YandexDirectAPI") as M:
        M.return_value.bids_get.return_value = {"Bids": [{"KeywordId": 1, "Bid": 1000}]}
        async with create_connected_server_and_client_session(mcp._mcp_server) as s:
            r = await s.call_tool("yd_bids_get", {"params_json": '{"SelectionCriteria": {}, "FieldNames": ["KeywordId"]}'})
            assert not r.isError


@pytest.mark.anyio
async def test_yd_bids_set():
    with patch("mcp_server_yandex_direct.server.YandexDirectAPI") as M:
        M.return_value.bids_set.return_value = {"SetResults": [{"Id": 1}]}
        async with create_connected_server_and_client_session(mcp._mcp_server) as s:
            r = await s.call_tool("yd_bids_set", {"params_json": '{}'})
            assert not r.isError


@pytest.mark.anyio
async def test_yd_bids_set_auto():
    with patch("mcp_server_yandex_direct.server.YandexDirectAPI") as M:
        M.return_value.bids_set_auto.return_value = {"SetAutoResults": [{"Id": 1}]}
        async with create_connected_server_and_client_session(mcp._mcp_server) as s:
            r = await s.call_tool("yd_bids_set_auto", {"params_json": '{}'})
            assert not r.isError


# ── BidModifiers ──

@pytest.mark.anyio
async def test_yd_bidmodifiers_get():
    with patch("mcp_server_yandex_direct.server.YandexDirectAPI") as M:
        M.return_value.bidmodifiers_get.return_value = {"BidModifiers": [{"Id": 40}]}
        async with create_connected_server_and_client_session(mcp._mcp_server) as s:
            r = await s.call_tool("yd_bidmodifiers_get", {"params_json": '{"SelectionCriteria": {}, "FieldNames": ["Id"]}'})
            assert not r.isError


@pytest.mark.anyio
async def test_yd_bidmodifiers_add():
    with patch("mcp_server_yandex_direct.server.YandexDirectAPI") as M:
        M.return_value.bidmodifiers_add.return_value = {"AddResults": [{"Id": 41}]}
        async with create_connected_server_and_client_session(mcp._mcp_server) as s:
            r = await s.call_tool("yd_bidmodifiers_add", {"params_json": '{}'})
            assert not r.isError


@pytest.mark.anyio
async def test_yd_bidmodifiers_delete():
    with patch("mcp_server_yandex_direct.server.YandexDirectAPI") as M:
        M.return_value.bidmodifiers_delete.return_value = {"DeleteResults": [{"Id": 40}]}
        async with create_connected_server_and_client_session(mcp._mcp_server) as s:
            r = await s.call_tool("yd_bidmodifiers_delete", {"params_json": '{"SelectionCriteria": {"Ids": [40]}}'})
            assert not r.isError


@pytest.mark.anyio
async def test_yd_bidmodifiers_set():
    with patch("mcp_server_yandex_direct.server.YandexDirectAPI") as M:
        M.return_value.bidmodifiers_set.return_value = {"SetResults": [{"Id": 40}]}
        async with create_connected_server_and_client_session(mcp._mcp_server) as s:
            r = await s.call_tool("yd_bidmodifiers_set", {"params_json": '{}'})
            assert not r.isError
