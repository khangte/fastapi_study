##################################################
# 실행 유의 사항
# uvicorn main:app --reload
# 기본값은 127.0.0.1:8000 이기 때문에
# 외부(호스트)에서 접근 불가합니다. 반드시 이렇게 실행하세요:
# 1. 가상머신에서 실행
#   $ uvicorn main:app --host 0.0.0.0 --port 8000
# 2. 윈도우에서 브라우저로 확인
#   http://localhost:8000/
##################################################

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
app = FastAPI()

origins = [
    "http://localhost:5173",
]
# CORS 설정
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  # Svelte 개발 서버 주소
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/hello")
async def hello():
    return {"message" : "안녕하세요 파이보"}
