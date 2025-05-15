from datetime import datetime

from sqlalchemy.orm import Session

from domain.answer.answer_schema import AnswerCreate
from models import Question, Answer


# 답변을 등록하기 위한 함수
def create_answer(db: Session, question: Question, answer_create: AnswerCreate):
    db_answer = Answer(question=question,
                       content=answer_create.content,
                       create_date=datetime.now())
    db.add(db_answer)
    db.commit()
