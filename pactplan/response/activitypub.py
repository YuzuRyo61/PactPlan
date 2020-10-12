from starlette.responses import JSONResponse


class ActivityPubResponse(JSONResponse):
    media_type = "application/ld+json; profile=\"https://www.w3.org/ns/activitystreams\""
