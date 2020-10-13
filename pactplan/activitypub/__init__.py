from fastapi import APIRouter

from .inbox import PP_AR_APINBOX
from .tasks import send_activity
from .user import PP_AR_APUSER

PP_AR_ACTIVITYPUB = APIRouter()

PP_AR_ACTIVITYPUB.include_router(
    PP_AR_APINBOX
)

PP_AR_ACTIVITYPUB.include_router(
    PP_AR_APUSER
)

__all__ = [
    "PP_AR_ACTIVITYPUB",
    "send_activity"
]
