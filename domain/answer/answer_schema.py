import datetime
from pydantic import BaseModel, field_validator
from domain.user.user_schema import User

# 입력항목을 처리하는데 사용핧 스키마
class AnswerCreate(BaseModel):
    content: str

    # content 속성은 디폴트값이 없기 때문에 필수값이다.
    # 하지만 ""처럼 빈 문자열이 입력될 수 있다.
    # content에 빈 문자열을 허용하지 않도록 설정한다.
    @field_validator('content')
    def not_empty(cls, v):
        if not v or not v.strip():
            raise ValueError('빈 값은 허용되지 않습니다.')
        return v

class Answer(BaseModel):
    id: int
    content: str
    create_date: datetime.datetime
    user: User | None
    question_id: int
    modify_date: datetime.datetime | None = None
    voter: list[User] = [] # 추천인

class AnswerUpdate(AnswerCreate): # AnswerCreate 스키마 를 상속
    answer_id: int

class AnswerDelete(BaseModel):
    answer_id: int

# 답변 추천 스키마
class AnswerVote(BaseModel):
    answer_id: int

