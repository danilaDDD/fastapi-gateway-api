import aiohttp
import pytest
from mock import AsyncMock, Mock

from app.clients.user_client import UserClient


@pytest.fixture(scope="function")
def session_mock() -> aiohttp.ClientSession:
    return Mock(spec=aiohttp.ClientSession)


@pytest.fixture(scope="function")
def user_client(session_mock: aiohttp.ClientSession) -> UserClient:
    from app.clients.user_client import UserClient
    return UserClient(session_mock, "")