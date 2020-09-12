import logging
import pyfiglet
from fastapi import FastAPI
from fastapi_login import LoginManager

from .api import PP_AR_WK, PP_AR_NI
from .activitypub import PP_AR_ACTIVITYPUB
from .config import PP_CONFIG

__version__ = "0.1.0"


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
    prefix="/.well-known",
    tags=["well-known"]
)

PP_APP.include_router(
    PP_AR_NI,
    prefix="/nodeinfo",
    tags=["nodeinfo"]
)


@PP_APP.on_event("startup")
def startup():
    logging.info("\n" + pyfiglet.figlet_format("PactPlan"))
    logging.info("Social Networking Service for ActivityPub")


@PP_APP.on_event("shutdown")
def shutdown():
    logging.info("PactPlan is now shutting down... Bye!")
