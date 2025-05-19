# import contextlib

from sqlalchemy import create_engine, MetaData
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
naming_convention = {
    "ix": 'ix_%(column_0_label)s',
    "uq": "uq_%(table_name)s_%(column_0_name)s",
    "ck": "ck_%(table_name)s_%(column_0_name)s",
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
    "pk": "pk_%(table_name)s"
}
Base.metadata = MetaData(naming_convention=naming_convention)

# FastAPI는 제너레이터 기반 함수를 직접 지원하며, 자동으로 리소스 관리를 처리한다.
# 그러나 @contextlib.contextmanager를 사용하면
# get_db 함수가 contextlib._GeneratorContextManager 객체를 반환하게 되어
# FastAPI의 종속성 주입이 제대로 동작하지 않는다.
# 따라서 get_db 함수에서 @contextlib.contextmanager 어노테이션을 제거해야 한다.
# @contextlib.contextmanager
def get_db(): # db 객체를 리턴하는 제너레이터
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
