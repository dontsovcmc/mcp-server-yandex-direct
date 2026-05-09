import os

import pytest

os.environ.setdefault("YD_TOKEN", "test-fake-token")
os.environ.setdefault("YD_CLIENT_LOGIN", "")
os.environ.setdefault("YD_LANG", "")


@pytest.fixture(autouse=True)
def _reset_api_singleton():
    """Reset cached API instance between tests."""
    import mcp_server_yandex_direct.server as srv
    srv._api_instance = None
    yield
    srv._api_instance = None
