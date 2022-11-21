from sqlalchemy import Column, Integer, String
from . import sql_db


# models
class Task(sql_db.Base):
    __tablename__ = "task"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, unique=True, index=True)
    description = Column(String, index=True)
