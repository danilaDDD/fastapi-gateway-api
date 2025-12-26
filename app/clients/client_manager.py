from contextlib import asynccontextmanager

import aiohttp
from fastapi import Depends

from app.clients.user_client import UserClient
from settings.settings import Settings, load_settings


class ClientManager:
    def __init__(self, session_factory: aiohttp.ClientSession, base_url: str):
        self._session_factory = session_factory
        self._session = None
        self._base_url = base_url

    @asynccontextmanager
    async def start(self):
        async with self._session_factory as session:
            self._session = session
            try:
                yield self
            finally:
                self._session = None

    @property
    def users(self) -> UserClient:
        url = f"{self._base_url}/users/"
        return UserClient(self._session, url)

    @property
    def base_url(self) -> str:
        return self._base_url

    @property
    def session(self) -> aiohttp.ClientSession:
        return self._session


def get_client_manager(settings: Settings = Depends(load_settings)) -> ClientManager:
    session_factory = aiohttp.ClientSession()
    base_url = settings.BASE_URL

    return ClientManager(session_factory, base_url)