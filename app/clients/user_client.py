import aiohttp

from app.schemas.requests.user_requests import CreateUserRequest
from app.schemas.responses.error_responses import ErrorResponse
from app.schemas.responses.user_responses import UserResponseEntity, CreateUserResponse


class UserClient:
    def __init__(self, session: aiohttp.ClientSession, base_url: str):
        self.session = session
        self.base_url = base_url


    async def create_user(self, request: CreateUserRequest) -> CreateUserResponse | ErrorResponse:
        async with self.session.post(self.base_url, json=request.model_dump()) as response:
            response_data = await response.json()
            if response.status in (200, 201):
                return CreateUserResponse(**response_data)
            else:
                return ErrorResponse(**response_data)