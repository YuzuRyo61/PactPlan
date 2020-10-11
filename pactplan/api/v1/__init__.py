from fastapi import APIRouter

from .plot import PP_AR_PLOT
from .user import PP_AR_USER

PP_AR_V1 = APIRouter()

PP_AR_V1.include_router(
    PP_AR_PLOT,
    prefix="/plot",
    tags=["v1", "plot"]
)

PP_AR_V1.include_router(
    PP_AR_USER,
    prefix="/user",
    tags=["v1", "user"]
)

__all__ = [
    "PP_AR_PLOT",
    "PP_AR_USER",
    "PP_AR_V1"
]
