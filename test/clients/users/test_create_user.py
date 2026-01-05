import datetime

import aiohttp
import pytest
from fastapi import HTTPException
from mock import Mock
from pydantic import ValidationError

from app.clients.user_client import UserClient
from app.schemas.requests.user_requests import CreateUserRequest
from app.schemas.responses.user_responses import CreateUserResponse
from test.clients.mocks import ClientResponseMock
from test.utils.response_utils import create_user_response


@pytest.mark.unit
@pytest.mark.asyncio
class TestUserClientCreateUser:
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, session_mock: aiohttp.ClientSession, domain: str):
        self.session_mock = session_mock
        self.url = domain + "/users/"
        self.any_request = Mock(spec=CreateUserRequest)
        self.user_client = UserClient(self.session_mock, self.url)
        yield


    def set_response(self, status_code: int = 200, returned_resp: dict | None = None):
        self.session_mock.post = Mock(return_value=ClientResponseMock(status_code=status_code, json_data=returned_resp))


    async def est_with_valid_response_should_return_entity(self):
        returned_resp = create_user_response()

        self.set_response(201, returned_resp)

        real_resp_obj = await self.user_client.create_user(self.any_request)
        expected_resp_obj = CreateUserResponse(**returned_resp)
        assert real_resp_obj == expected_resp_obj


    async def test_with_invalid_response_200_should_raise_validation_error(self):
        self.set_response(201, {"invalid_field": "value"})

        with pytest.raises(ValidationError):
            await self.user_client.create_user(self.any_request)


    async def test_with_not_201_response_should_raise_http_exception(self):
        self.set_response(404, {"detail": "error"})
        with pytest.raises(HTTPException):
            await self.user_client.create_user(self.any_request)












