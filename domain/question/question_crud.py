from datetime import datetime

from starlette.exceptions import HTTPException

from domain.question.question_schema import QuestionCreate, QuestionUpdate
from models import Question, User, Answer
from sqlalchemy import and_ # 최신버전에서 outerjoin 'and_'를 반드시 사용
from sqlalchemy.orm import Session

    # skip : 조회한 데이터의 시작위치
    # limit : 시작위치부터 가져올 데이터의 건수
def get_question_list(db: Session, skip: int = 0, limit: int = 10,
                      keyword: str = ''):
    question_list = db.query(Question)
    if keyword: # 입력된 키워드가 있으면
        search = '%%{}%%'.format(keyword)
        sub_query = db.query(Answer.question_id, Answer.content, User.username) \
            .outerjoin(User, and_(Answer.user_id == User.id)).subquery()
        question_list = question_list \
            .outerjoin(User) \
            .outerjoin(sub_query, and_(sub_query.c.question_id == Question.id)) \
            .filter(Question.subject.ilike(search) |  # 질문제목
                    Question.content.ilike(search) |  # 질문내용
                    User.username.ilike(search) |  # 질문작성자
                    sub_query.c.content.ilike(search) |  # 답변내용
                    sub_query.c.username.ilike(search)  # 답변작성자
                    )
    total = question_list.distinct().count()
    question_list = question_list.order_by(Question.create_date.desc()) \
        .offset(skip).limit(limit).distinct().all()

    return total, question_list  # (전체 건수, 페이징 적용된 질문 목록)


def get_question(db: Session, question_id: int):
    question = db.query(Question).get(question_id)
    return question

def create_question(db: Session, question_create: QuestionCreate,
                    user: User):
    db_question = Question(subject=question_create.subject,
                           content=question_create.content,
                           create_date=datetime.now(),
                           user=user)
    db.add(db_question)
    db.commit()

def update_question(db: Session, db_question: Question, question_update: QuestionUpdate):
    db_question.subject = question_update.subject
    db_question.content = question_update.content
    db_question.modify_date = datetime.now()
    db.add(db_question)
    db.commit()

def delete_question(db: Session, db_question: Question):
    db.delete(db_question)
    db.commit()

# 질문 추천 CRUD (교재식. 지금 사용 안함)
# Question 모델의 voter에 추천인(User 모델)을 추가하는 함수
def vote_question(db: Session,
                  db_question: Question,
                  db_user: User):
    if db_user not in db_question.voter:
        db_question.voter.append(db_user)
        db.commit()
        return True
    else:
        return False

def toggle_vote_question(db: Session,
                         db_question: Question,
                         db_user: User) -> bool:
    if db_user in db_question.voter:
        db_question.voter.remove(db_user)
        db.commit()
        return False
    else:
        db_question.voter.append(db_user)
        db.commit()
        return True

