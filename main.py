from typing import List

from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

from core import crud, models, schemas
from core.sql_db import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# App home route
@app.get("/")
def hello_tracker():
    return {"message": "Hello everyone, this is a task tracker api"}


# Get create users
@app.post("/track-api/users/", response_model=schemas.User)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return crud.create_user(db=db, user=user)


# Get users
@app.get("/track-api/users/", response_model=List[schemas.User])
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = crud.get_users(db, skip=skip, limit=limit)
    return users


# Get user
@app.get("/track-api/{user_id}", response_model=schemas.User)
def read_user(user_id: int, db: Session = Depends(get_db)):
    db_user = crud.get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user


# Create task for user
@app.post("/track-api/users/{user_id}/tasks/", response_model=schemas.Task)
def create_task_for_user(user_id: int, item: schemas.TaskCreate, db: Session = Depends(get_db)):
    return crud.create_user_task(db=db, item=item, user_id=user_id)


# Get tasks
@app.get("/track-api/tasks/", response_model=List[schemas.Task])
def read_tasks(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    items = crud.get_tasks(db, skip=skip, limit=limit)
    return items
