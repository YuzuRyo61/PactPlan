import uuid

from sqlalchemy import Column, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.sql.functions import current_timestamp
from sqlalchemy.types import String, Text, DateTime, Boolean
from sqlalchemy_utils import UUIDType

from ..database import PP_DB_BASE


class Plot(PP_DB_BASE):
    __tablename__ = "plots"

    id = Column(
        UUIDType(binary=False),
        primary_key=True,
        default=uuid.uuid4
    )
    text = Column(
        Text(),
        nullable=True
    )
    cw = Column(
        String(512),
        nullable=True
    )
    local_only = Column(
        Boolean(),
        default=False
    )
    uri = Column(
        String(512),
        nullable=True
    )
    url = Column(
        String(512),
        nullable=True
    )
    created_by_id = Column(
        UUIDType(binary=False),
        ForeignKey("users.id")
    )
    created_by = relationship(
        "User",
        back_populates="plots"
    )
    created_at = Column(
        DateTime,
        server_default=current_timestamp(),
        nullable=False
    )
