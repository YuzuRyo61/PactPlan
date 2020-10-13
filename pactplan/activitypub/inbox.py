import uuid

from fastapi import APIRouter, Depends, HTTPException

from ..depends import strict_activitypub, db_session
from ..models import User

PP_AR_APINBOX = APIRouter()


@PP_AR_APINBOX.post(
    "/inbox",
    include_in_schema=False,
    status_code=202
)
def ap_public_inbox(
        _=Depends(strict_activitypub)
):
    # TODO: Inbox系の処理を書く。HTTP Signatureの検証も忘れずに
    pass


@PP_AR_APINBOX.post(
    "/user/{user_uuid}/inbox",
    include_in_schema=False,
    status_code=202
)
def ap_user_inbox(
        user_uuid: uuid.UUID,
        _=Depends(strict_activitypub),
        db=Depends(db_session)
):
    query = db.query(User).get(user_uuid)
    if query is None:
        raise HTTPException(status_code=404, detail="Unknown user")
    pass
