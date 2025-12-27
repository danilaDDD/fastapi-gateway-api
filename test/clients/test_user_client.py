import datetime

import aiohttp
import pytest
from mock import AsyncMock, Mock
from pydantic_core import ValidationError

from app.clients.user_client import UserClient
from app.schemas.requests.user_requests import CreateUserRequest
from app.schemas.responses.error_responses import ErrorResponse
from app.schemas.responses.user_responses import CreateUserResponse
from app.schemas.schemas import Token
from test.clients.mocks import ClientResponseMock


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
        returned_resp = {
            "id": 1,
            "login": "test",
            "password": "<PASSWORD>",
            "first_name": "first",
            "last_name": "last",
            "second_name": "second",
            "access_token": Token(token="access.token.value", expired_at=datetime.datetime.now()),
            "refresh_token": Token(token="refresh.token.value", expired_at=datetime.datetime.now()),
        }

        self.session_mock.post = Mock(return_value=ClientResponseMock(status_code=201, json_data=returned_resp))

        real_resp_obj = await self.user_client.create_user(self.valid_request)
        expected_resp_obj = CreateUserResponse(**returned_resp)
        assert real_resp_obj == expected_resp_obj


    async def test_with_error_response_should_return_error_response(self):
        returned_resp = {
            "detail": "error"
        }


        self.session_mock.post = Mock(return_value=ClientResponseMock(status_code=400, json_data=returned_resp))
        real_resp_obj = await self.user_client.create_user(self.valid_request)

        expected_resp_obj = ErrorResponse(**returned_resp)
        assert real_resp_obj == expected_resp_obj


    async def test_with_unexpected_response_should_raise_validation_error(self):
        returned_resp = {
            "unexpected": "data"
        }

        self.session_mock.post = Mock(return_value=ClientResponseMock(status_code=500, json_data=returned_resp))
        with pytest.raises(ValidationError):
            await self.user_client.create_user(self.valid_request)













