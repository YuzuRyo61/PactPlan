from starlette.responses import JSONResponse


class ActivityPubResponse(JSONResponse):
    media_type = "application/activity+json; charset=utf-8"
