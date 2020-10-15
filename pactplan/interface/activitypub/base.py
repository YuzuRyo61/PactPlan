from typing import Union

from pydantic import BaseModel, Field

http_regex = r"^https?://.+"


class APBase(BaseModel):
    context: Union[str, list] = Field([
        "https://www.w3.org/ns/activitystreams",
        "https://w3id.org/security/v1"
    ],
        alias="@context")
    type: str
