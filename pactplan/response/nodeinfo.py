from starlette.responses import JSONResponse


class NodeinfoResponse(JSONResponse):
    media_type = "application/json; " \
                 "profile=http://nodeinfo.diaspora.software/ns/schema/2.0#"
