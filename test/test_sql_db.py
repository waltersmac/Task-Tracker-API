from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

class TestSqlDb:
    def test_sql_db(self):
        sqlalchemy_database_url = "sqlite:///./data/sql_app.db"

        engine = create_engine(
            sqlalchemy_database_url, connect_args={"check_same_thread": False}
        )
        session_local = sessionmaker(autocommit=False, autoflush=False, bind=engine)

        base = declarative_base()

        assert engine
        assert session_local
        assert base