from typing import Optional

from fastapi import Header, HTTPException, Body, Depends


def is_activitypub(
        content_type: Optional[str] = Header(None),
        accept: Optional[str] = Header(None),
        body=Body({})
):
    ap_headers = (
        "application/activity+json",
        "application/activity+json;",
        "application/activity+json; charset=utf-8",
        "application/ld+json",
        "application/ld+json;",
        "application/ld+json; "
        "profile=\"https://www.w3.org/ns/activitystreams\""
    )
    if content_type is None:
        if accept.lower() in ap_headers:
            return True
        else:
            return False
    else:
        if content_type.lower() in ap_headers:
            ap_context = "https://www.w3.org/ns/activitystreams"
            if type(body.get("@context")) == list:
                for context in body.get("@context"):
                    if context == ap_context:
                        return True
                return False
            elif type(body.get("@context")) == str and \
                    body.get("@context") == ap_context:
                return True
            else:
                return False
        else:
            return False


def strict_activitypub(
        is_ap=Depends(is_activitypub)
):
    if is_ap:
        return True
    else:
        raise HTTPException(
            status_code=400, detail="Not ActivityPub")
