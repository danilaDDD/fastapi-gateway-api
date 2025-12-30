import datetime

import aiohttp
import pytest
from fastapi import HTTPException
from mock import AsyncMock, Mock
from pydantic_core import ValidationError

from app.clients.user_client import UserClient
from app.schemas.requests.user_requests import CreateUserRequest
from app.schemas.responses.error_responses import ErrorResponse
from app.schemas.responses.user_responses import CreateUserResponse
from app.schemas.schemas import Token
from test.clients.mocks import ClientResponseMock
from test.utils.response_utils import UserResponseUtils


@pytest.mark.unit
@pytest.mark.asyncio
class TestUserClientCreateUser:
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, session_mock: aiohttp.ClientSession, domain: str):
        self.session_mock = session_mock
        self.url = domain + "/users/"
        self.valid_request = Mock(spec=CreateUserRequest)
        self.user_client = UserClient(self.session_mock, self.url)
        yield

    async def test_with_success_response_should_return_user_response_entity(self):
        returned_resp = UserResponseUtils.create_user_response()

        self.set_response(201, returned_resp)

        real_resp_obj = await self.user_client.create_user(self.valid_request)
        expected_resp_obj = CreateUserResponse(**returned_resp)
        assert real_resp_obj == expected_resp_obj


    def set_response(self, status_code: int = 200, returned_resp: dict | None = None):
        self.session_mock.post = Mock(return_value=ClientResponseMock(status_code=status_code, json_data=returned_resp))













