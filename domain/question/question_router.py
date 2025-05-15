from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from database import get_db
from domain.question import question_schema, question_crud
# from models import Question

from starlette import status

# router 객체를 생성하여 FastAPI 앱에 등록해야만 라우팅 기능이 동작한다.
# 라우팅이란 FastAPI가 요청받은 URL을 해석하여 그에 맞는 함수를 실행하여 그 결과를 리턴하는 행위를 말한다.
router = APIRouter(
    prefix="/api/question"
)


# @router.get("/list")
# def question_list(): # db 세션을 생성하고 해당 세션을 이용하여 질문 목록을 조회하여 리턴하는 함수
#     # db = SessionLocal()
#     # _question_list = db.query(Question).order_by(Question.create_date.desc()).all()
#     # db.close()
#
#     # get_db 사용
#     with get_db() as db:
#         _question_list = db.query(Question).order_by(Question.create_date.desc()).all()
#     return _question_list


@router.get("/list", response_model=question_schema.QuestionList)
# 출력 항목에 전체 건수를 추가하기 위해 response_model을 QuestionList 스키마로 변경
def question_list(db: Session = Depends(get_db),
                  page: int = 0, size: int = 10):
    total, _question_list = question_crud.get_question_list(
        db, skip=page*size, limit=size)
    return {
        'total': total,
        'question_list': _question_list
    }


# question_detail 함수는 URL을 통해 얻은 question_id ㅏㄱㅂㅅ으로
# 질문 상세 내역을 조회하여 Question 스키마로 리턴하는 함수
@router.get("/detail/{question_id}", response_model=question_schema.Question)
def question_detail(question_id: int, db: Session = Depends(get_db)):
    question = question_crud.get_question(db, question_id=question_id)
    return question

# 라우터 함수의 응답으로 response_model을 사용하는 대신
# status_code=status.HTTP_204_NO_CONTENT 를 사용했다.
# 이렇게 리턴할 응답이 없을 경우에는 응답코드 204를 리턴하여
# "응답 없음"을 나타낼 수 있다.
@router.post("/create", status_code=status.HTTP_204_NO_CONTENT)
def question_create(_question_create: question_schema.QuestionCreate,
                    db: Session = Depends(get_db)):
    question_crud.create_question(db=db, question_create=_question_create)

