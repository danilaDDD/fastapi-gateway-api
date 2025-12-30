import datetime
from email.header import Header
from typing import Union

from fastapi import APIRouter, Response, Depends, HTTPException
from starlette import status

from app.clients.client_manager import get_client_manager
from app.schemas.requests.user_requests import CreateUserRequest, PutUserRequest
from app.schemas.responses.error_responses import ErrorResponse
from app.schemas.responses.user_responses import CreateUserResponse, UserResponseEntity

user_router = APIRouter(
    prefix="/users",
    tags=["users"],
)
@user_router.post("/",
                  responses={
                        status.HTTP_201_CREATED: {
                            "model": CreateUserResponse,
                            "description": "User created successfully.",
                        },
                }
)
async def create_user(request_body: CreateUserRequest,
                          response: Response,
                          client_manager = Depends(get_client_manager),
                      ) -> CreateUserResponse:
    async with client_manager.start() as manager:
        response.status_code = status.HTTP_201_CREATED
        return await manager.users.create_user(request_body)

@user_router.put("/{id}/",
                 responses={
                     status.HTTP_200_OK: {
                         "model": UserResponseEntity,
                         "description": "User update successfully."
                     }
                 })
async def edit_user(request: PutUserRequest, id: int) -> UserResponseEntity:

    raise NotImplementedError("This endpoint is not implemented yet.")

@user_router.get("/{id}/",
                 responses={
                     status.HTTP_200_OK: {
                         "model": UserResponseEntity,
                         "description": "User retrieved successfully."
                     }
                 })
async def get_user(id: int) -> UserResponseEntity:
    raise NotImplementedError("This endpoint is not implemented yet.")

@user_router.get("/",
                 responses={
                     status.HTTP_200_OK: {
                         "model": list[UserResponseEntity],
                         "description": "Users retrieved successfully."
                     }
                 })
async def get_all_users() -> list[UserResponseEntity]:
    raise NotImplementedError("This endpoint is not implemented yet.")


