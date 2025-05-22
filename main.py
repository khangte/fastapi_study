##################################################
# 실행 유의 사항
# uvicorn main:app --reload
# 기본값은 127.0.0.1:8000 이기 때문에
# 외부(호스트)에서 접근 불가합니다. 반드시 이렇게 실행하세요:
# 1. 가상머신에서 실행
# => uvicorn main:app --host 0.0.0.0 --port 8000
# 2. 윈도우에서 브라우저로 확인
# => http://localhost:8000/
##################################################

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from starlette.responses import FileResponse
from starlette.staticfiles import StaticFiles

from domain.answer import answer_router
from domain.question import question_router
from domain.user import user_router

app = FastAPI()

origins = [
    "http://localhost:5173", # 개발 서버
    "http://localhost:8000", # 배포 서버
]

# CORS 설정
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  # Svelte 개발 서버 주소
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# @app.get("/hello")
# async def hello():
#     return {"message" : "안녕하세요 파이보"}

# app 객체에 include_router 메서드를 사용하여 question_router.py 파일의 router 객체를 등록했다.
app.include_router(question_router.router)
app.include_router(answer_router.router)
app.include_router(user_router.router)

# 프론트엔드 빌드 후 적용 => FastAPI 서버 서비스 가능
# localhost:8000
app.mount("/assets", StaticFiles(directory="frontend/dist/assets"))
@app.get("/") # / 경로로 접속하면 frontend/dist/index.html 파일을 읽어서 서비스 한다.
def index():
   return FileResponse("frontend/dist/index.html")
    # FileResponse는 FastAPI가 정적인 파일을 출력할 때 사용

