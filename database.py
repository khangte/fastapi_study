from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# 데이터베이스 접속 주소
SQLALCHEMY_DATABASE_URL = "sqlite:///./myapi.db"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)

# 데이터베이스에 접속하기 위해 필요한 클래스
SessionLocal = sessionmaker(
    # sqlalchemy 사용 규칙
    autocommit=False,
    autoflush=False,
    bind=engine
)

Base = declarative_base()
