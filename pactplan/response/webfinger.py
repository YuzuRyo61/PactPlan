from starlette.responses import JSONResponse


class WebFingerResponse(JSONResponse):
    media_type = "application/jrd+json"
