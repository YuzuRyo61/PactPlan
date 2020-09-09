import uuid

from sqlalchemy import Column, text
from sqlalchemy.sql.functions import current_timestamp
from sqlalchemy.types import String, Boolean, Text, DateTime
from sqlalchemy_utils import UUIDType

from ..database import PP_DB_BASE


class Users(PP_DB_BASE):
    __tablename__ = "users"

    # Columns
    id = Column(
        UUIDType(binary=False),
        primary_key=True,
        default=uuid.uuid4
    )
    username = Column(
        String(32)
    )
    display_name = Column(
        String(255),
        nullable=True
    )
    description = Column(
        Text(),
        nullable=True
    )
    is_admin = Column(
        Boolean(),
        default=False
    )
    is_moderator = Column(
        Boolean(),
        default=False
    )
    is_silence = Column(
        Boolean(),
        default=False
    )
    is_suspend = Column(
        Boolean(),
        default=False
    )
    is_bot = Column(
        Boolean(),
        default=False
    )
    is_manual_follow = Column(
        Boolean(),
        default=False
    )
    is_remote_user = Column(
        Boolean(),
        default=False
    )
    remote_host = Column(
        String(255),
        nullable=True
    )
    remote_inbox = Column(
        String(512),
        nullable=True
    )
    remote_share_inbox = Column(
        String(512),
        nullable=True
    )
    remote_outbox = Column(
        String(512),
        nullable=True
    )
    remote_featured = Column(
        String(512),
        nullable=True
    )
    remote_uri = Column(
        String(512),
        nullable=True
    )
    remote_key_id = Column(
        String(512),
        nullable=True
    )
    public_key = Column(
        Text()
    )
    private_key = Column(
        Text(),
        nullable=True
    )
    created_at = Column(
        DateTime,
        server_default=current_timestamp(),
        nullable=False
    )
    updated_at = Column(
        DateTime,
        nullable=True
    )

    # functions
    def username_lower(self):
        return self.username.lower()
