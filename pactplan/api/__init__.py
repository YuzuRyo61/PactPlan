from fastapi import APIRouter

from .nodeinfo import PP_AR_NI
from .plot import PP_AR_PLOT
from .well_known import PP_AR_WK

PP_API_ROOT = APIRouter()

PP_API_ROOT.include_router(
    PP_AR_PLOT,
    prefix="/plot",
    tags=["plot"]
)

__all__ = [
    "PP_AR_WK",
    "PP_AR_NI",
    "PP_AR_PLOT",
    "PP_API_ROOT"
]
