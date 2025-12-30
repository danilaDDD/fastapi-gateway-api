import aiohttp
from fastapi import HTTPException

from app.schemas.requests.user_requests import CreateUserRequest
from app.schemas.responses.error_responses import ErrorResponse
from app.schemas.responses.user_responses import UserResponseEntity, CreateUserResponse


class UserClient:
    def __init__(self, session: aiohttp.ClientSession, base_url: str):
        self.session = session
        self.base_url = base_url

    async def create_user(self, request: CreateUserRequest, headers: dict = None) -> CreateUserResponse | ErrorResponse:
        async with self.session.post(self.base_url, json=request.model_dump(), headers=headers) as response:
            response_data = await response.json()
            if response.status in (200, 201):
                return CreateUserResponse(**response_data)
            else:
                raise HTTPException(status_code=response.status, detail=response_data.get("detail", "Unknown error"))