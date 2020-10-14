import json
from typing import Union

from fastapi import Response


def activity_response(
        response: Union[str, dict],
        ap_header: str
):
    return Response(
        content=json.dumps(response) if type(response) == dict else response,
        media_type=ap_header
    )
