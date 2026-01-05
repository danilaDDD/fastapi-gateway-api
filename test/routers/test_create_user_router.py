import pytest
from fastapi import HTTPException
from mock.mock import patch, AsyncMock

from app.schemas.responses.user_responses import CreateUserResponse
from test.utils.response_utils import create_user_request, create_user_response


@pytest.mark.unit
class TestCreateUserRequest:
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, client):
        self.client = client
        self.url = "/users/"
        yield

    def test_with_valid_response_should_success(self):
        with self.patch() as mock_create_user:
            expected_resp_dict = create_user_response()
            mock_create_user.return_value = CreateUserResponse.model_validate(expected_resp_dict)

            response = self.do_request()

            assert response.status_code == 201

            real_resp_dict = response.json()
            assert real_resp_dict.pop("access_token") is not None
            assert real_resp_dict.pop("refresh_token") is not None
            expected_resp_dict.pop("access_token")
            expected_resp_dict.pop("refresh_token")
            assert real_resp_dict == expected_resp_dict


    def test_with_raise_http_exception_should_return_error_response(self):
        detail = "error"
        status_code = 400

        with self.patch() as mock_create_user:
            mock_create_user.side_effect = HTTPException(detail=detail, status_code=400)

            resp = self.do_request()

            assert resp.status_code == status_code
            assert resp.json() == {"detail": detail}


    def test_with_raise_any_exception_should_return_error_response(self):
        with self.patch() as mock_create_user:
            mock_create_user.side_effect = RuntimeError("error")
            resp = self.do_request()

            assert resp.status_code == 500
            resp_json = resp.json()
            assert "detail" in resp_json


    @classmethod
    def patch(cls):
        return patch("app.clients.user_client.UserClient.create_user",
                     new_callable=AsyncMock)

    def do_request(self):
        request = create_user_request()
        return self.client.post(self.url, json=request)


