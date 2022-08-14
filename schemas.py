from pydantic import BaseModel

# Defines attributes that all schemas will inherit for all actions (reading/writing, etc.)
class UserBase(BaseModel):
	email: str

# Used for creating items
class UserCreate(UserBase):
	pass

# Used for reading items
class User(UserBase):
	pass

class TodoBase(BaseModel):
	task: str

class TodoCreate(TodoBase):
	pass

class Todo(TodoBase):
	pass