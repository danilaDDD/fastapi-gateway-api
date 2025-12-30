import datetime

from app.schemas.schemas import Token


class UserResponseUtils:
    @classmethod
    def create_user_response(cls) -> dict:
        return {
            "id": 1,
            "login": "test",
            "first_name": "first",
            "last_name": "last",
            "second_name": "second",
            "access_token": {
                "token": "access.token.value",
                "expired_at": str(datetime.datetime.now())
            },
            "refresh_token": {
                "token": "access.token.value",
                "expired_at": str(datetime.datetime.now())
            }
        }

    @classmethod
    def create_user_request(cls):
        return {
            "login": "test",
            "password": "testpassword",
            "first_name": "first",
            "last_name": "last",
            "second_name": "second"
        }