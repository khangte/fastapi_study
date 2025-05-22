# models.py
# 파이보 프로젝트는 ORM 을 지원하는 파이썬 데이터베이스 도구인 SQLAlchemy를 사용한다.
# SQLAlchemy는 모델 기반으로 데이터베이스를 처리한다.
# 모델 클래스들을 정의하는 파일

from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey, Table
from sqlalchemy.orm import relationship

from database import Base

# 3-12 추천
# 질문이나 답변에 "추천"을 적용하려면 질문 모델과 답변 모델에 "추천인" 이라는 속성을 추가해야 한다.
# 하나의 질문에 여러명이 추천할 수 있고 한 명이 여러개의 질문에 추천할 수 있으므로
# 이런 경우에는 "다대다(M:N)" 관계를 사용해야 한다.
# SQLAlchemy에서 MtN 관계를 적용하는 방법에 대해 알아보자.
question_voter = Table(
    'question_voter', # 테이블명
    Base.metadata,
    Column('user_id', Integer,
           ForeignKey('user.id'), primary_key=True),
    Column('question_id', Integer,
           ForeignKey('question.id'), primary_key=True)
)
# question_voter는 질문 추천을 위해 사용할 테이블 객체이다.
# MtM 관계를 적용하기 위해서는 sqlalchemy의 Table을 사용하여
# M:N 관계를 의미하는 테이블을 먼저 생성해야 한다.
# 사용자 id와 질문자 id가 모두 PK이므로 ManyToMany 관계가 성립된다.

# Question 모델
class Question(Base):
    __tablename__ = "question"

    id = Column(Integer, primary_key=True)
    subject = Column(String, nullable=False)
    content = Column(Text, nullable=False)
    create_date = Column(DateTime, nullable=False)
    user_id = Column(Integer, ForeignKey("user.id"), nullable=True)
    user = relationship("User", backref="question_users")
    modify_date = Column(DateTime, nullable=True)
    # voter(추천인) 속성 추가
    voter = relationship('User',
                         secondary=question_voter,
                         backref='question_voters'
                         # user 속성의 backref="question_users"와 중복되면 안된다.
                         )
    # secondary 값으로 위에 생성한 question_voter 테이블 객체를 지정.
    # => Question 모델을 통해 추천인을 저장하면 실제 데이터는
    # quesiton_voter 테이블에 저장되고 저장된 추천인 정보는
    # Question 모델의 voter 속성을 통해 참조할 수 있게 된다.
    # backref 이름은 question_voters 라는 이름으로 지정했는데,
    # 만약 어떤 계정이 a_user 라는 객체로 참조되었다면,
    # a_user.question_voters 로 해당 계정이 추천한 질문 리스트를 구할 수 있다.

answer_voter = Table(
    'answer_voter',
    Base.metadata,
    Column('user_id', Integer,
           ForeignKey('user.id'), primary_key=True),
    Column('answer_id', Integer,
           ForeignKey('answer.id'), primary_key=True)
)

class Answer(Base):
    __tablename__ = "answer"

    id = Column(Integer, primary_key=True)
    content = Column(Text, nullable=False)
    create_date = Column(DateTime, nullable=False)
    question_id = Column(Integer, ForeignKey("question.id"))
    question = relationship("Question", backref="answers") # backref 역참조
    user_id = Column(Integer, ForeignKey("user.id"), nullable=True)
    user = relationship("User", backref="answer_users")
    modify_date = Column(DateTime, nullable=True)
    voter = relationship('User',
                         secondary=answer_voter,
                         backref='answer_voters')

class User(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True)
    username = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)

