from sqlalchemy import Column, Integer, ForeignKey, Date, Computed, String

from database import Base


class Users(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    email = Column(String, nullable=False)
    hashed_password = Column(String, nullable=False)
