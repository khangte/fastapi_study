from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from database import get_db
from domain.question import question_schema, question_crud
# from models import Question
from domain.user.user_router import get_current_user
from models import User

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
                  page: int = 0, size: int = 10,
                  keyword: str = ''):
    total, _question_list = question_crud.get_question_list(
        db, skip=page*size, limit=size, keyword=keyword)
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
                    db: Session = Depends(get_db),
                    current_user: User = Depends(get_current_user)):
    question_crud.create_question(db=db, question_create=_question_create,
                                  user=current_user)

@router.put("/update", status_code=status.HTTP_204_NO_CONTENT)
def question_update(_question_update: question_schema.QuestionUpdate,
                    db: Session = Depends(get_db),
                    current_user: User = Depends(get_current_user)):
    db_question = question_crud.get_question(db, question_id=_question_update.question_id)
    if not db_question:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail="데이터를 찾을수 없습니다.")
    if current_user.id != db_question.user.id:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail="수정 권한이 없습니다.")
    question_crud.update_question(db=db, db_question=db_question,
                                  question_update=_question_update)


@router.delete("/delete", status_code=status.HTTP_204_NO_CONTENT)
def question_delete(_question_delete: question_schema.QuestionDelete,
                    db: Session = Depends(get_db),
                    current_user: User = Depends(get_current_user)):
    db_question = question_crud.get_question(db, question_id=_question_delete.question_id)
    if not db_question:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail="데이터를 찾을 수 없습니다.")
    if current_user.id != db_question.user.id:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            details="삭제 권한이 없습니다.")
    question_crud.delete_question(db=db, db_question=db_question)

# 질문 추천 라우터
@router.post("/vote", status_code=status.HTTP_200_OK)
def question_vote(_question_vote: question_schema.QuestionVote,
                  db: Session = Depends(get_db),
                  current_user: User = Depends(get_current_user)):
    db_question = question_crud.get_question(db, question_id=_question_vote.question_id)
    if not db_question:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail="데이터를 찾을수 없습니다.")
    # question_crud.vote_question(db, db_question=db_question, db_user=current_user)
    voted = question_crud.toggle_vote_question(db, db_question, db_user=current_user)
    return {"voted": voted, "voter_count": len(db_question.voter)}

