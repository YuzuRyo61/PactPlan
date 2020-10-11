import uuid

from fastapi import APIRouter, Depends, HTTPException

from pactplan.depends import db_session
from pactplan.models import User

PP_AR_USER = APIRouter()


@PP_AR_USER.get(
    "/"
)
def get_users(db=Depends(db_session)):
    query = db.query(User).all()
    if query is None:
        return []


@PP_AR_USER.get(
    "/uuid/{user_id}",
    summary="Get user via UUID"
)
def get_user_uuid(user_id: uuid.UUID):
    query = db.query(User).get(user_id)
    if query is None:
        raise HTTPException(status_code=404, detail="User not found")


@PP_AR_USER.get(
    "/username/{username}",
    summary="Get user via username"
)
def get_user_username(username: str, db=Depends(db_session)):
    query = db.query(User)
