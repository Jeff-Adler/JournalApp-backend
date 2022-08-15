from sqlalchemy.orm import Session

from . import models, schemas

def get_user(db: Session, user_id: int):
	return db.query(models.User).filter(models.User.id == user_id).first()

def get_user_by_email(db: Session, email: str):
	pass

def get_users():
	pass

def create_user():
	pass

def get_task():
	pass

def get_tasks_by_user_id():
	pass

def create_task():
	pass

def edit_task():
	pass

def mark_task_done():
	pass

def delete_task():
	pass


# - GET user
# - GET user by email
# - GET all user
# - POST user
# - GET particular task by id
# - GET a user's tasks
# - POST new task
# - PATCH task: task
# - PATCH task: mark as done
# - DELETE task by id