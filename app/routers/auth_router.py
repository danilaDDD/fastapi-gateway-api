from fastapi import APIRouter, status, Response, Depends, HTTPException
from jwt import DecodeError

from app.schemas.requests.auth_requests import TokensRequest, RefreshTokensRequest
from app.schemas.responses.token_responses import TokensResponse
from app.schemas.schemas import Token

auth_router = APIRouter(
    prefix="/tokens",
    tags=["auth"],
)

@auth_router.post("/",
                  responses={
                      status.HTTP_200_OK: {
                          "model": TokensRequest,
                          "description": "Access token generated successfully.",
                      },
                  }
)
async def get_token_access(request: TokensRequest, response: Response) -> TokensResponse:
    raise NotImplementedError("This endpoint is not implemented yet.")


@auth_router.post("/refresh",
                  responses={
                      status.HTTP_200_OK: {
                          "model": Token,
                          "description": "Tokens refreshed successfully.",
                      },
                  }
)
async def refresh_tokens(request: RefreshTokensRequest,
                         response: Response) -> Token:
    raise NotImplementedError("This endpoint is not implemented yet.")
