import datetime
import uuid
from typing import Optional, Union

from pydantic import BaseModel, Field

from .users import ILocalUsers, IRemoteUsers


class IPlot(BaseModel):
    id: uuid.UUID = Field(default_factory=uuid.uuid4)
    text: Optional[str]
    cw: Optional[str]
    local_only: bool = False
    uri: Optional[str]
    url: Optional[str]
    created_by_id: uuid.UUID
    created_by: Optional[Union[ILocalUsers, IRemoteUsers]]
    created_at: datetime.datetime = Field(
        default_factory=datetime.datetime.now)

    class Config:
        orm_mode = True
