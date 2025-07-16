# 점프 투 FastAPI
[[위키독스 **점프 투 FastAPI**]](https://www.google.com/search?q=%EC%A0%90%ED%94%84%ED%88%AC+fastapi&rlz=1C1GCEU_koKR1161KR1161&oq=%EC%A0%90%ED%94%84%ED%88%AC&gs_lcrp=EgZjaHJvbWUqBggBEEUYOzIGCAAQRRg5MgYIARBFGDsyBggCEEUYOzIGCAMQRRg7MgYIBBBFGDvSAQkzMDA1ajBqMTWoAgiwAgE&sourceid=chrome&ie=UTF-8)

---

## 개발환경 구성

### 시스템 환경

| 항목             | 내용                                 |
|------------------|--------------------------------------|
| 가상화 플랫폼    | VirtualBox + Ubuntu 22.04 Server     |
| 메모리           | 8GB                                  |
| 프로세서         | 4개 이상 (PyCharm, VSCode 사용 때문) |
| 비디오 메모리    | 16MB                                 |
| 모니터 개수      | 1개                                  |
| 저장소 메모리    | 16~25GB                              |
| 네트워크         | NAT + 포트포워딩                    |

### 백엔드

| 항목         | 내용          |
|--------------|---------------|
| 프레임워크    | FastAPI       |
| 서버 실행     | Uvicorn       |
| 개발 환경     | PyCharm       |

### 프론트엔드

| 항목             | 내용                |
|------------------|---------------------|
| 프레임워크        | Svelte              |
| UI 라이브러리     | Bootstrap 5.3.6     |
| 개발 환경         | Visual Studio Code  |

### 데이터베이스

| 항목    | 내용       |
|---------|------------|
| RDBMS   | SQLite     |
| ORM     | SQLAlchemy |

### 배포용 GitHub Repository

| 항목     | 링크                                                                 |
|----------|----------------------------------------------------------------------|
| GitHub   | [GitHub/khangte](https://github.com/khangte/fastapi_study)          |

---

## 파일 구조
```
myapi/
├── domain/
│   ├── answer/
│   │   ├── answer_crud.py
│   │   ├── answer_router.py
│   │   └── answer_schema.py
│   ├── question/
│   │   ├── question_crud.py
│   │   ├── question_router.py
│   │   └── question_schema.py
│   └── user/
│       ├── user_crud.py
│       ├── user_router.py
│       └── user_schema.py
├── frontend/
│   ├── dist/
│   │   ├── assets/
│   │   │   ├── index-??.css
│   │   │   └── index-h-??.js
│   │   ├── index.html
│   │   └── vite.svg
│   ├── public/
│   │   └── vite.svg
│   ├── src/
│   │   ├── components/
│   │   │   ├── Error.svelte
│   │   │   └── Navigation.svelte
│   │   ├── lib/
│   │   │   ├── api.js
│   │   │   └── store.js
│   │   ├── routes/
│   │   │   ├── AnswerModify.svelte
│   │   │   ├── Detail.svelte
│   │   │   ├── Home.svelte
│   │   │   ├── QuestionCreate.svelte
│   │   │   ├── QuestionModify.svelte
│   │   │   ├── UserCreate.svelte
│   │   │   └── UserLogin.svelte
│   │   ├── app.css
│   │   ├── App.svelte
│   │   ├── main.js
│   │   └── vite-env.d.ts
│   ├── .env
│   ├── .gitignore
│   ├── index.html
│   ├── jsconfig.json
│   ├── package-lock.json
│   └── package.json
├── migrations/
│   ├── versions/
│   └── env.py
├── .env
├── database.py
├── main.py
├── models.py
├── myapi.db
├── README.md
└── requirements.txt
```

---

## 개발 환경 설정

### Svelte 설치

```bash
$ npm create vite@latest frontend -- --template svelte
$ cd frontend
$ npm install
```
- ```jsconfig.json``` 타입스크립트 사용 안함 => false로 변경
```json
파일명: /frontend/jsconfig.json
{
  (...생락...)
  "checkJs": false
  (...생락...)
}
```

### 가상환경 설정

```bash
# 가상환경 생성
$ uv venv

# 가상환경 활성화
$ source .venv/bin/activate 

# 패키지 설치
$ uv pip install requirements.txt
```

### 데이터베이스 마이그레이션 (Alembic)

0. alembic 설치
```bash
sudo apt install alembic
```

1. Alembic 초기화
```bash
$ alembic init migrations
```

2. 설정 파일 수정
- ```alembic.ini```수정
```ini
sqlalchemy.url = sqlite:///./myapi.db
```

- ```migrations/env.py```수정
```python
from models
target_metadata = models.Base.metadata
```

3. 변경사항 감지하고 마이그레이션 파일 생성
```bash
$ alembic revision --autogenerate
```

4. DB에 적용
```bash
$ alembic upgrade head
```

### 환경 변수 설정
- 환경 파일 경로 : ```/frontent/.enc```
- 다음과 같이 백엔드 API 서버 URL 등록:
```ini
VITE_SERVER_URL=http://127.0.0.1:8000
```

---

## 실행코드

### 개발중

1. 백엔드 실행 (FastAPI)
```bash
$ uvicorn main:app --reload --host 0.0.0.0 --port 8000
```
2. 프론트엔드 실행 (Svelte + Vite 개발 서버)
```bash
$ cd frontend
$ npm run dev
```
3. 개발 서버 접속 ```URL: **localhost:5173**```

### 배포용

1. 프론트엔드 빌드
```bash
$ cd frontend
$ npm run build
```
2. 프론트엔드 정적 파일 서빙 설정
```python
# main.py 에 추가
from starlette.responses import FileResponse
from starlette.staticfiles import StaticFiles
origins=["http://localhost:8000", # 배포 서버]
app.mount("/assets", StaticFiles(directory="frontend/dist/assets"))
@app.get("/") # / 경로로 접속하면 frontend/dist/index.html 파일을 읽어서 서비스 한다.
def index():
   return FileResponse("frontend/dist/index.html")
```
3. 백엔드 실행 (FastAPI)
```bash
$ uvicorn main:app --host 0.0.0.0 --port 8000
```
4. FastAPI 서버 접속 ```URL: **localhost:8000**```

---

#### 중요 파일
- router.py - 라우터 파일 - URL과 API의 전체적인 동작을 관리
- crud.py - 데이터베이스 처리 파일 - 데이터의 생성(Create), 조회(Read), 수정(Update), 삭제(Delete)를 처리 (CRUD)
- schema.py - 입출력 관리 파일 - 입력 데이터와 출력 데이터의 스펙 정의 및 검증

---

## 터미널에서 DB 확인방법
1. SQLite3 클라이언트 설치
```bash
$ sudo apt update
$ sudo apt install sqlite3
```
2. ```myapi.db``` 접속
```bash
$ sqlite3 myapi.db
```
3. 테이블 목록 확인
```sqlite
.tables
```
4. 테이블 구조 확인
```sqlite
.schema user
```
5. 데이터 확인
```sqlite
SELECT * FROM user;
```
6. 종료
```sqlite
.quit
```

---

## Ubuntu 내의 SQLite DB 파일을 Windows DB Browser for SQLite로 열기
### 방법 1: SCP로 복사(가장 간단하고 안전)
1. Ubuntu에서 DB 파일 경로 확인
```bash
$ pwd myapi.db
/home/kmh/myapi/myapi.db
```

2. Ubuntu의 IP 주소 확인
```bash
$ ip a
127.0.0.1
```

3. Windows CMD or PowerShell 에서 복사
```shell
> scp kmh@127.0.0.1:/home/kmh/myapi/myapi.db .
```

4. DB Browser (SQLite) 에서 DB 열기

---

## 기능 구현 절차
- 백엔드: 데이터 처리 흐름
  1. 스키마 생성
  2. CRUD 함수 작성
  3. 라우터 작성 및 등록
- 프론트엔드: 화면 구성 흐름
  1. Svelte 컴포넌트 작성
  2. 라우터에 컴포넌트 등록

---
