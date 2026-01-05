import aiohttp
import pytest
from fastapi import HTTPException
from mock import Mock
from pydantic import ValidationError

from app.clients.user_client import UserClient
from app.schemas.requests.user_requests import PutUserRequest
from app.schemas.responses.user_responses import UserResponseEntity
from test.clients.mocks import ClientResponseMock
from test.utils.response_utils import get_user_entity


@pytest.mark.asyncio
@pytest.mark.unit
class TestPutRequest:
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, session_mock: aiohttp.ClientSession, domain: str, user_client: UserClient):
        self.url = domain + "/users/%i/"
        self.session_mock = session_mock
        self.user_client = user_client
        self.any_request = PutUserRequest()
        yield


    def set_response(self, status_code: int = 200, returned_resp: dict | None = None):
        self.session_mock.put = Mock(return_value=ClientResponseMock(status_code=status_code, json_data=returned_resp))


    async def test_with_valid_response_should_return_entity(self):
        user_id = 1
        api_resp_dict = get_user_entity(user_id)
        self.set_response(200, api_resp_dict)
        expected_resp_obj = UserResponseEntity(**api_resp_dict)

        real_resp_obj = await self.user_client.put_user(user_id, self.any_request)

        assert expected_resp_obj == real_resp_obj


    async def test_with_invalid_response_200_should_raise_validation_error(self):
        user_id = 1
        self.set_response(200, {"invalid_field": "value"})

        with pytest.raises(ValidationError):
            await self.user_client.put_user(user_id, self.any_request)


    async def test_with_not_200_response_should_raise_http_exception(self):
        user_id = 1
        self.set_response(400, {"detail": "error"})

        with pytest.raises(HTTPException):
            await self.user_client.put_user(user_id, self.any_request)








