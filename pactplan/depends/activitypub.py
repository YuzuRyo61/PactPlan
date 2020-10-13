from typing import Optional

from fastapi import Header, HTTPException, Body


def strict_activitypub(
        content_type: Optional[str] = Header(None),
        accept: Optional[str] = Header(None),
        body=Body({})
):
    ap_headers = [
        "application/activity+json",
        "application/activity+json;",
        "application/activity+json; charset=utf-8",
        "application/ld+json",
        "application/ld+json;",
        "application/ld+json; profile=\"https://www.w3.org/ns/activitystreams\""
    ]
    if content_type is None:
        if accept.lower() in ap_headers:
            yield True
            return
        else:
            raise HTTPException(status_code=400, detail="Not ActivityPub Header")
    else:
        if content_type.lower() in ap_headers:
            ap_context = "https://www.w3.org/ns/activitystreams"
            if type(body.get("@context")) == list:
                for context in body.get("@context"):
                    if context == ap_context:
                        yield True
                        return
                raise HTTPException(status_code=400, detail="Not ActivityPub context")
            elif type(body.get("@context")) == str and \
                    body.get("@context") == ap_context:
                yield True
                return
            else:
                raise HTTPException(status_code=400, detail="Not ActivityPub context")
        else:
            raise HTTPException(status_code=400, detail="Not ActivityPub Header")


def is_activitypub(
        content_type: Optional[str] = Header(None),
        accept: Optional[str] = Header(None),
        body=Body({})
):
    try:
        return strict_activitypub(
            content_type,
            accept,
            body
        )
    except HTTPException:
        return False
