from ..services.auth_service import AuthService as AuthService
from enum import Enum
from fastapi import APIRouter, params as params
from typing import Sequence

class AuthRouter(APIRouter):
    def __init__(self, *, prefix: str, tags: list[str | Enum] | None = None, dependencies: Sequence[params.Depends] | None = None) -> None: ...
