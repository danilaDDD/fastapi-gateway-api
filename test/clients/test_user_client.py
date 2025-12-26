import datetime

import aiohttp
import pytest
from mock import AsyncMock, Mock

from app.clients.user_client import UserClient
from app.schemas.requests.user_requests import CreateUserRequest
from app.schemas.responses.user_responses import CreateUserResponse
from app.schemas.schemas import Token
from test.clients.mocks import ClientResponseMock


@pytest.mark.unit
class TestUserClientCreateUser:
    @pytest.mark.asyncio
    async def test_with_valid_request_should_return_user_response_entity(self, session_mock: aiohttp.ClientSession):
        returned_resp = {
            "id": 1,
            "login": "test",
            "password": "<PASSWORD>",
            "first_name": "first",
            "last_name": "last",
            "second_name": "second",
            "access_token": Token(token="access.token.value", expired_at=datetime.datetime.utcnow()),
            "refresh_token": Token(token="refresh.token.value", expired_at=datetime.datetime.utcnow()),
        }
        kwargs = returned_resp.copy()
        kwargs.pop("id")
        request = CreateUserRequest(**kwargs)

        session_mock.post = Mock(return_value=ClientResponseMock(201, returned_resp))

        user_client = UserClient(session_mock, "http://testserver/users/")
        real_resp_obj = await user_client.create_user(request)
        expected_resp_obj = CreateUserResponse(**returned_resp)
        assert real_resp_obj == expected_resp_obj












