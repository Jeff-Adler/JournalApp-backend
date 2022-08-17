from sqlalchemy.orm import Session

from . import models, schemas

def get_user(db: Session, user_id: int):
	return db.query(models.User).filter(models.User.id == user_id).first()

def get_user_by_email(db: Session, email: str):
	return db.query(models.User).filter(models.User.email == email).first()

def get_users(db: Session, skip: int = 0, limit: int = 100):
	return db.query(models.User).offset(skip).limit(limit).all()

def create_user():
	pass

def get_task(db: Session, task_id: int):
	return db.query(models.Task).filter(models.Task.id == task_id).first()

def get_tasks_by_user_id(db: Session, user_id: int):
	# return db.query(models.User).filter(models.User.id == user_id).first()

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