# Pydantic은 FastAPI의 입출력 스펙을 정의하고 그 값을 검증하기 위해 사용하는 라이브러리이다.
# Pydantic은 API의 입출력 항목을 다음과 같이 정의하고 검증할수 있다.
# - 입출력 항목의 갯수와 타입을 설정
# - 입출력 항목의 필수값 체크
# - 입출력 항목의 데이터 검증

import datetime

from pydantic import BaseModel, field_validator

from domain.answer.answer_schema import Answer
from domain.user.user_schema import User

# Question 스키마
class Question(BaseModel):
    id: int
    subject: str
    content: str
    create_date: datetime.datetime
    answers: list[Answer] = []
    user: User | None
    modify_date: datetime.datetime | None = None
    voter: list[User] = [] # 추천인

class QuestionCreate(BaseModel):
    subject: str
    content: str

    @field_validator('subject', 'content')
    def not_empty(cls, v):
        if not v or not v.strip():
            raise ValueError('빈 값은 허용되지 않습니다.')
        return v

# 질문 목록 API의 응답으로 사용하는 스키마
class QuestionList(BaseModel):
    total: int = 0                      # 전체 게시물 개수
    question_list: list[Question] = []  # 질문 목록 데이터

class QuestionUpdate(QuestionCreate): # QuestionCreate를 상속
    question_id: int

class QuestionDelete(BaseModel):
    question_id: int

# 질문 추천 스키마
class QuestionVote(BaseModel):
    question_id: int

