import os
import sys
from datetime import datetime

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# from db.models.user import User
from db.session import Base
from sqlalchemy import Boolean, Column, Date, ForeignKey, Integer, String
from sqlalchemy.orm import relationship


class Job(Base):
    __tablename__ = "job"
    __table_args__ = {"extend_existing": True}

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    company = Column(String, nullable=False)
    company_url = Column(String)
    location = Column(String, nullable=False)
    description = Column(String, nullable=False)
    date_posted = Column(Date, nullable=False, default=datetime.utcnow())
    is_active = Column(Boolean, default=True)

    owner_id = Column(Integer, ForeignKey("user.id"))
    # owner = relationship("User", back_populates="jobs")
