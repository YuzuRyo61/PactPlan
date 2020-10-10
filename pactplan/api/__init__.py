from fastapi import APIRouter

# V1
from pactplan.api.v1 import PP_AR_V1
from .nodeinfo import PP_AR_NI
from .well_known import PP_AR_WK

PP_API_ROOT = APIRouter()

PP_API_ROOT.include_router(
    PP_AR_V1,
    prefix="/v1",
    tags=["v1"]
)

__all__ = [
    "PP_AR_WK",
    "PP_AR_NI",
    "PP_AR_V1",
    "PP_API_ROOT"
]
