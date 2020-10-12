from typing import Optional

from fastapi import Header


def is_activity_header(
        content_type: Optional[str] = Header(None),
        accept: Optional[str] = Header(None)
):
    ap_headers = [
        "application/activity+json",
        "application/activity+json;",
        "application/ld+json",
        "application/ld+json;",
        "application/ld+json; profile=\"https://www.w3.org/ns/activitystreams\""
    ]
    if content_type is None:
        if accept.lower() in ap_headers:
            yield True
        else:
            yield False
    else:
        if content_type.lower() in ap_headers:
            yield True
        else:
            yield False
