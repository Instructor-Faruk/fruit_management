from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base


#DATABASE_URL = "mysql+pymysql://root:root@localhost:3306/training"
DATABASE_URL="postgresql+psycopg2://my_db_zt27_user:wCl3QF8SLLrLNfzN3IltSCfXVdNEHfZB@dpg-dc3qdp6i0phs7388al6g-a.oregon-postgres.render.com/my_db_zt27"
engine = create_engine(DATABASE_URL)
session_local = sessionmaker(autocommit=False, autoflush=False, bind=engine)
base = declarative_base()


def get_db():
    db = session_local()
    try:
        yield db
    finally:
        db.close()
