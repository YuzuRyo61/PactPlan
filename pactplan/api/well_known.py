import logging
import re

from fastapi import APIRouter, HTTPException, Depends, Response
from sqlalchemy import and_, func
from sqlalchemy.orm import Session
from starlette.responses import JSONResponse

from pactplan.config import PP_CONFIG
from pactplan.depends import db_session
from pactplan.models import Users

PP_AR_WK = APIRouter()


class WebFingerResponse(JSONResponse):
    media_type = "application/jrd+json"


@PP_AR_WK.get("/host-meta")
def wk_hostmeta():
    hostmeta = """<?xml version="1.0" encoding="UTF-8"?>
<XRD xmlns="http://docs.oasis-open.org/ns/xri/xrd-1.0">
  <Link
    type="application/xrd+xml"
    template="https://""" + PP_CONFIG["core"]["url"]["fqdn"] + """/.well-known/webfinger?resource={uri}"
  />
</XRD>
    """.replace("\n", "")
    return Response(
        content=hostmeta,
        media_type="application/xrd+xml"
    )


@PP_AR_WK.get("/host-meta.json")
def wk_hostmeta_json():
    return {
        "links": [
            {
                "rel": "lrdd",
                "type": "application/jrd+json",
                "template": "https://" + PP_CONFIG["core"]["url"]["fqdn"] + "/.well-known/webfinger?resource={uri}"
            }
        ]
    }


@PP_AR_WK.get("/webfinger", response_class=WebFingerResponse)
def wk_webfinger(resource: str = None, db: Session = Depends(db_session)):
    if resource is None:
        raise HTTPException(
            status_code=400
        )
    reg_fqdn = PP_CONFIG["core"]["url"]["fqdn"].replace(".", r"\.")
    if not re.search(rf"(acct:)?(.*)@({reg_fqdn})", resource.lower()):
        raise HTTPException(
            status_code=400
        )
    parsed_resource = str(re.sub(r"^acct:", "", resource, count=1)).lower().split("@")
    logging.info(f"Fetching webfinger: {resource}")
    query = db.query(Users).filter(and_(
        func.lower(Users.username) == parsed_resource[0],
        func.lower(Users.remote_host) == None,
        Users.is_remote_user == False
    )).first()

    if query is None:
        logging.warning(f"Webfinger failed: {resource}")
        raise HTTPException(
            status_code=400
        )

    return {
        "subject": f"acct:{query.acct}",
        "links": [
            {
                "rel": "self",
                "type": "application/activity+json",
                "href": f"{PP_CONFIG['core']['url']['protocol']}://{PP_CONFIG['core']['url']['fqdn']}"
                        f"/activity/users/{query.id}"
            },
            {
                "rel": "http://webfinger.net/rel/profile-page",
                "type": "text/html",
                "href": f"{PP_CONFIG['core']['url']['protocol']}://{PP_CONFIG['core']['url']['fqdn']}"
                        f"/web/user/{query.username}"
            }
        ]
    }
