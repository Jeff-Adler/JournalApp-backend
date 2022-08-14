from pydantic import BaseModel

# Defines attributes that all schemas will inherit for all actions (reading/writing, etc.)
class UserBase(BaseModel):
	email: str

# Used for creating items
class UserCreate(UserBase):
	password: str

# Used for reading items
class User(UserBase):
	id: int
	is_active: bool

	tasks: List[Task] = []

	# This allows you to set certain config options with Pydantic
    class Config:
    	# allows you to do e.q. current_user.items as a shorthand for data.id or relationship attributes like current_user.items
    	orm_mode = True

class TaskBase(BaseModel):
	task: str

class TaskCreate(TaskBase):
	pass

class Task(TaskBase):
	id: int
	is_done: bool
	owner_id: int

	class Config:
		orm_mode = true
