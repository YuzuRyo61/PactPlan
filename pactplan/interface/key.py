from typing import Optional
from pydantic import BaseModel


class IKey(BaseModel):
    public_key: str
    private_key: Optional[str]
