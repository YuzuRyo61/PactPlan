from pydantic import BaseModel, constr

from .base import http_regex


class APKey(BaseModel):
    id: str
    type: str = "Key"
    owner: constr(
        regex=http_regex
    )
    publicKeyPem: str
