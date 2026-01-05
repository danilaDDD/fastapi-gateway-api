import datetime


def create_user_response() -> dict:
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


def create_user_request():
    return {
        "login": "test",
        "password": "testpassword",
        "first_name": "first",
        "last_name": "last",
        "second_name": "second"
    }


def get_user_entity(id: int):
    return {
            "id": id,
            "login": "test",
            "first_name": "first",
            "last_name": "last",
            "second_name": "second",
        }