from pydantic import BaseModel

class UserBase(BaseModel):
	email: str

class UserCreate(UserBase):
	pass

class User(UserBase):
	pass

class TodoBase(BaseModel):
	task: str

class TodoCreate(TodoBase):
	pass

class Todo(TodoBase):
	pass