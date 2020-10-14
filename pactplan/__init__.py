import logging

from fastapi import FastAPI
from fastapi_login import LoginManager

from .activitypub import PP_AR_ACTIVITYPUB
from .api import PP_AR_WK, PP_AR_NI, PP_API_ROOT, PP_AR_OA
from .config import PP_CONFIG

__version__ = "0.1.0"

from .response import NodeinfoResponse

PP_APP = FastAPI(
    title="PactPlan",
    description="Social Networking Service for ActivityPub",
    version=__version__,
    openapi_url="/api/docs/openapi.json",
    docs_url="/api/docs",
    swagger_ui_oauth2_redirect_url="/api/docs/oauth2-redirect",
    redoc_url="/api/docs-redoc"
)

PP_LOGIN = LoginManager(PP_CONFIG, tokenUrl="/auth/token")


# Register router
PP_APP.include_router(
    PP_AR_WK,
    prefix="/.well-known"
)

PP_APP.include_router(
    PP_AR_NI,
    prefix="/nodeinfo",
    default_response_class=NodeinfoResponse
)

PP_APP.include_router(
    PP_AR_ACTIVITYPUB,
    prefix="/activity"
)

PP_APP.include_router(
    PP_AR_OA,
    prefix="/oauth",
    tags=["oauth", "auth"]
)

PP_APP.include_router(
    PP_API_ROOT,
    prefix="/api"
)


# on event
@PP_APP.on_event("startup")
def startup():
    logging.info("Social Networking Service for ActivityPub")


@PP_APP.on_event("shutdown")
def shutdown():
    logging.info("PactPlan is now shutting down... Bye!")
