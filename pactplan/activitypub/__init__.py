from fastapi import APIRouter

from .inbox import PP_AR_INBOX
from .tasks import send_activity

PP_AR_ACTIVITYPUB = APIRouter()

PP_AR_ACTIVITYPUB.include_router(
    PP_AR_INBOX
)

__all__ = [
    "PP_AR_ACTIVITYPUB",
    "send_activity"
]
