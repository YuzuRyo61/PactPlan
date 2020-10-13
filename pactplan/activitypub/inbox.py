from fastapi import APIRouter, Depends

from ..depends import strict_activitypub

PP_AR_INBOX = APIRouter()


@PP_AR_INBOX.post(
    "/inbox",
    include_in_schema=False
)
def ap_public_inbox(
        is_ap=Depends(strict_activitypub)
):
    return {"is_activity_header": is_ap}
