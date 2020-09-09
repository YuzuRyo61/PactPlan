import uuid
from datetime import datetime
from typing import Optional
from pydantic import BaseModel, Field


class IUsers(BaseModel):
    """
    ローカルユーザ、リモートユーザ共通のインターフェース。
    通常は使用しません
    """
    id: uuid.UUID = Field(default_factory=uuid.uuid4)
    username: str
    display_name: Optional[str]
    description: Optional[str]
    is_admin: bool = False
    is_moderator: bool = False
    is_silence: bool = False
    is_suspend: bool = False
    is_bot: bool = False
    is_manual_follow: bool = False
    public_key: str
    created_at: datetime = Field(default_factory=datetime.now)
    updated_at: Optional[datetime]


class ILocalUsers(IUsers):
    """
    ローカルユーザ用インターフェース。
    """
    is_remote_user = False
    private_key: str


class IRemoteUsers(IUsers):
    """
    リモートユーザ専用インターフェース。
    """
    is_admin = False
    is_moderator = False
    is_remote_user = True
    remote_host: str
    remote_inbox: str
    remote_featured: Optional[str]
    remote_uri: str
    remote_key_id: str

