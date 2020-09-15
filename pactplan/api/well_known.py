import logging
import re

from fastapi import APIRouter, HTTPException, Depends, Response
from sqlalchemy import and_, func
from sqlalchemy.orm import Session

from pactplan.config import PP_CONFIG
from pactplan.depends import db_session
from pactplan.models import User
from pactplan.response import NodeinfoResponse, WebFingerResponse

PP_AR_WK = APIRouter()


@PP_AR_WK.get(
    "/nodeinfo",
    response_class=NodeinfoResponse,
    include_in_schema=False)
def wk_nodeinfo():
    return {
        "links": [
            {
                "rel": "http://nodeinfo.diaspora.software/ns/schema/2.0",
                "href": f"{PP_CONFIG['core']['url']['protocol']}://{PP_CONFIG['core']['url']['fqdn']}/nodeinfo/2.0"
            }
        ]
    }


@PP_AR_WK.get(
    "/host-meta",
    include_in_schema=False)
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


@PP_AR_WK.get(
    "/host-meta.json",
    include_in_schema=False)
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


@PP_AR_WK.get(
    "/webfinger",
    response_class=WebFingerResponse,
    include_in_schema=False)
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
    query = db.query(User).filter(and_(
        func.lower(User.username) == parsed_resource[0],
        func.lower(User.remote_host) == None,
        User.is_remote_user == False
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
