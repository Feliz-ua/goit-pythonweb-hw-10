from fastapi import APIRouter

from app.dependencies import CurrentUser
from app.schemas import UserResponse
from fastapi import Request
from app.limiter import limiter

router = APIRouter(
    prefix="/users",
    tags=["users"],
)


@router.get("/me", response_model=UserResponse)
@limiter.limit("10/minute")
def read_current_user(
    request: Request,
    current_user: CurrentUser,
):
    return current_user