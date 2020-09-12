from fastapi import APIRouter

import pactplan
from pactplan.response import NodeinfoResponse

PP_AR_NI = APIRouter()


@PP_AR_NI.get("/2.0", response_class=NodeinfoResponse)
def nodeinfo_20():
    return {
        "version": "2.0",
        "software": {
            "name": "pactplan",
            "version": str(pactplan.__version__)
        },
        "protocols": [
            "activitypub"
        ],
        "services": {
            "inbound": [],
            "outbound": []
        },
        "openRegistrations": True,  # TODO: インスタンス情報から登録できるようにしておく
        "usage": {
            "users": {}
        },
        "metadata": {
            # TODO: ここにインスタンス情報など
        }
    }
