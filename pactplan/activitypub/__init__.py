from fastapi import APIRouter
from .tasks import send_activity


PP_AR_ACTIVITYPUB = APIRouter()

__all__ = [
    "PP_AR_ACTIVITYPUB",
    "send_activity"
]
