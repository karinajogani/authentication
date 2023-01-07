from database.db_base import Base
from sqlalchemy import String, Column
from sqlalchemy.dialects.postgresql import UUID
import uuid


class User(Base):
    """create model for user table
    """
    __tablename__ = "userauth"
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = Column(String)
    password = Column(String)
