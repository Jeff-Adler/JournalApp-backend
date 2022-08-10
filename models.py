from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from .database import Base

class User(Base):
	__tablename__ = "users"

	id = Column(Integer, primary_key=True, index=True)
	email = Column(String, unique=True, index=True)
	hashed_password = Column(String)
	is_active = Column(Boolean, default=True)

	items = relationship("Task", back_populates="owner")

class Task(Base)
	__tablename__ = "tasks"

	id = Column(Integer, primary_key=True, index=True)
	task = Column(String)
	is_done = Column(Boolean, default=False)

	owner = relationship("User", back_populates="tasks")