import uuid

from sqlalchemy import Column
from sqlalchemy.ext.hybrid import hybrid_property
from sqlalchemy.orm import relationship
from sqlalchemy.sql.functions import current_timestamp
from sqlalchemy.types import String, Boolean, Text, DateTime
from sqlalchemy_utils import UUIDType

from ..config import PP_CONFIG
from ..database import PP_DB_BASE


class User(PP_DB_BASE):
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
    plots = relationship(
        "Plot",
        back_populates="created_by"
    )

    @hybrid_property
    def acct(self):
        if self.is_manual_follow is True:
            return f"{self.username}@{self.remote_host}"
        else:
            return f"{self.username}@{PP_CONFIG['core']['url']['fqdn']}"
