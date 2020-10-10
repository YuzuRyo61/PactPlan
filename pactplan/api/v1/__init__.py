from fastapi import APIRouter

PP_AR_V1 = APIRouter()

from .plot import PP_AR_PLOT

PP_AR_V1.include_router(
    PP_AR_PLOT,
    prefix="/plot",
    tags=["v1", "plot"]
)

__all__ = [
    "PP_AR_PLOT",
    "PP_AR_V1"
]
