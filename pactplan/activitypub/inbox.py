from fastapi import APIRouter, Depends, HTTPException

from ..depends import is_activity_header

PP_AR_INBOX = APIRouter()


@PP_AR_INBOX.post(
    "/inbox",
    include_in_schema=False
)
def ap_public_inbox(
        is_ap=Depends(is_activity_header)
):
    if not is_ap:
        raise HTTPException(status_code=400, detail="Not ActivityPub Header")
    return {"is_activity_header": is_ap}
