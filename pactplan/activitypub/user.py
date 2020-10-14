import uuid
from typing import Optional

from fastapi import APIRouter, Depends, HTTPException, Header

from .template import ap_context
from ..config import PP_CONFIG
from ..depends import is_activitypub, db_session
from ..models import User
from ..response import activity_response

PP_AR_APUSER = APIRouter()


@PP_AR_APUSER.get(
    "/user/{user_uuid}",
    include_in_schema=False
)
def ap_user(
        user_uuid: uuid.UUID,
        is_ap=Depends(is_activitypub),
        db=Depends(db_session),
        accept: Optional[str] = Header(
            "application/activity+json; charset=utf-8")
):
    query = db.query(User).get(user_uuid)
    if query is None:
        raise HTTPException(status_code=404, detail="Unknown user")

    if not is_ap:
        # TODO: AcceptがActivityPub系じゃなかったらウェブクライアントにに飛ばす
        return

    ap_user_base_url = (
        f"{PP_CONFIG['core']['url']['protocol']}://"
        f"{PP_CONFIG['core']['url']['fqdn']}"
        f"/activity/user/{query.id}"
    )
    ap_shared_inbox = (
        f"{PP_CONFIG['core']['url']['protocol']}://"
        f"{PP_CONFIG['core']['url']['fqdn']}"
        f"/activity/inbox"
    )

    response = {
        "@context": ap_context,
        "type": "Service" if query.is_bot else "Person",
        "id": ap_user_base_url,
        "inbox": f"{ap_user_base_url}/inbox",
        # TODO: 以下の内容も実装する
        # "outbox": f"{ap_user_base_url}/outbox",
        # "followers": f"{ap_user_base_url}/followers",
        # "following": f"{ap_user_base_url}/following",
        # "featured": f"{ap_user_base_url}/featured",
        "sharedInbox": ap_shared_inbox,
        "endpoints": {
            "sharedInbox": ap_shared_inbox
        },
        "url": f"{PP_CONFIG['core']['url']['protocol']}://"
               f"{PP_CONFIG['core']['url']['fqdn']}"
               f"/web/user/{query.username}",
        "preferredUsername": query.username,
        "name": query.display_name,
        "summary": query.description,
        "icon": None,  # TODO: アイコン設定
        "image": None,  # TODO: ヘッダー設定
        "tag": [],  # TODO: 説明文から抽出
        "manuallyApprovesFollowers": query.is_manual_follow,
        "publicKey": {
            "id": f"{ap_user_base_url}#main-key",
            "type": "Key",
            "owner": ap_user_base_url,
            "publicKeyPem": query.public_key
        }
    }

    return activity_response(
        response,
        accept
    )
