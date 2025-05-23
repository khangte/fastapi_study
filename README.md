# 점프 투 FastAPI
[[위키독스 **점프 투 FastAPI**]](https://www.google.com/search?q=%EC%A0%90%ED%94%84%ED%88%AC+fastapi&rlz=1C1GCEU_koKR1161KR1161&oq=%EC%A0%90%ED%94%84%ED%88%AC&gs_lcrp=EgZjaHJvbWUqBggBEEUYOzIGCAAQRRg5MgYIARBFGDsyBggCEEUYOzIGCAMQRRg7MgYIBBBFGDvSAQkzMDA1ajBqMTWoAgiwAgE&sourceid=chrome&ie=UTF-8)

> ## 개발환경 구성 
> ### 시스템 환경
> - 가상화 플랫폼: VirtualBox + Ubuntu 22.04 Server
> - 메모리: 8GB
> - 프로세서: 4개 이상(pycharm, vscode 사용 때문)
> - 비디오메모리: 16MB
> - 모니터개수: 1개
> - 저장소 메모리: 16~25GB
> - 네트워크: NAT + 포트포워딩
> ### 백엔드
> - 프레임워크: FastAPI
> - 서버 실행: Uvicorn
> - 개발 환경: PyCharm
> ### 프론트엔드
> - 프레임워크: Svelte
> - UI 라이브러리: Bootstrap 5.3.6
> - 개발환경: Visual Studio Code
> ### 데이터베이스 
> - RDBMS: SQLite
> - ORM: SQLAlchemy
> ### 배포용 GitHub Repository
> - [GitHub/khangte](https://github.com/khangte/fastapi_study)

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

> ## 기능 구현 절차
> - 백엔드: 데이터 처리 흐름
>   1. 스키마 생성
>   2. CRUD 함수 작성
>   3. 라우터 작성 및 등록
> - 프론트엔드: 화면 구성 흐름
>   1. Svelte 컴포넌트 작성
>   2. 라우터에 컴포넌트 등록

---

> ## Svelte 설치
> ```bash
> $ npm create vite@latest frontend -- --template svelte
> $ cd frontend
> $ npm install
> ```
> - jsconfig.json 타입스크립트 사용 안함 => false로 변경
> ```json
> 파일명: /frontend/jsconfig.json
> {
>   (...생락...)
>   "checkJs": false
>   (...생락...)
> }
> ```

---

> ## 실행방법
> - 가상환경 생성
> ```
> $ uv venv
> ```
> - 가상환경 활성화
> ```bash
> $ source .venv/bin/activate 
> ```
> 패키지 설치
> ```bash
> uv pip install requirements.txt
> ```
> ---
> 리비전 파일 생성
> ```bash
> alembic revision --autogenerate
> ```
> 마이그레이션 적용
> ```bash
> alembic upgrade head
> ```
> ---
> - ```/frontent/.enc```파일에서 본인 URL 등록
> ```text
> VITE_SERVER_URL=http://127.0.0.1:8000
> ```
> ---
> ### 실행코드
> #### 개발중
> 1.백엔드 실행 (FastAPI)
> ```bash
> $ uvicorn main:app --host 0.0.0.0 --port 8000
> ```
> 2.프론트엔드 실행 (Svelte + Vite 개발 서버)
> ```bash
> $ cd frontend
> $ npm run dev
> ```
> 3. 개발 서버 접속 URL: **localhost:5173**
> ---
> #### 배포용
> 1. 프론트엔드 빌드
> ```bash
> $ cd frontend
> $ npm run build
> ```
> 2. 프론트엔드 정적 파일 서빙 설정
> ```python
> # main.py 에 추가
> from starlette.responses import FileResponse
> from starlette.staticfiles import StaticFiles
> origins=["http://localhost:8000", # 배포 서버]
> app.mount("/assets", StaticFiles(directory="frontend/dist/assets"))
> @app.get("/") # / 경로로 접속하면 frontend/dist/index.html 파일을 읽어서 서비스 한다.
> def index():
>    return FileResponse("frontend/dist/index.html")
> ```
> 3. FastAPI 서버 접속 URL: **localhost:8000**

---

> ### 필요 파일
> - router.py - 라우터 파일 - URL과 API의 전체적인 동작을 관리
> - crud.py - 데이터베이스 처리 파일 - 데이터의 생성(Create), 조회(Read), 수정(Update), 삭제(Delete)를 처리 (CRUD)
> - schema.py - 입출력 관리 파일 - 입력 데이터와 출력 데이터의 스펙 정의 및 검증

---

> ## Alembic 마이그레이션 과정
> 1. Alembic 초기화
> ```bash
> alembic init migrations
> ```
> 2. 설정 파일 수정
> - ```alembic.ini```수정
> - ```migrations/env.py```수정
> ```python
>  from models
>  target_metadata = models.Base.metadata
> ```
> 3. 변경사항 감지하고 마이그레이션 파일 생성
> ```bash
> alembic revision --autogenerate
> ```
> 4. DB에 적용
> ```bash
> alembic upgrade head
> ```

---

> ## 터미널에서 DB 확인방법
> 1. SQLite3 클라이언트 설치
> ```bash
> sudo apt update
> sudo apt install sqlite3
> ```
> 2. ```myapi.db``` 접속
> ```bash
> sqlite3 myapi.db
> ```
> 3. 테이블 목록 확인
> ```sqlite
> .tables
> ```
> 4. 테이블 구조 확인
> ```sqlite
> .schema user
> ```
> 5. 데이터 확인
> ```sqlite
> SELECT * FROM user;
> ```
> 6. 종료
> ```sqlite
> .quit
> ```

---

> ## Ubuntu 내의 SQLite DB 파일을 Windows DB Browser for SQLite로 열기
> ### 방법 1: SCP로 복사(가장 간단하고 안전)
> 1. Ubuntu에서 DB 파일 경로 확인
> ```bash
> $ pwd myapi.db
> /home/kmh/myapi/myapi.db
> ```
> ![check_db_path.PNG](images/check_db_path.PNG)
> 
> 2. Ubuntu의 IP 주소 확인
> ```bash
> $ ip a
> 127.0.0.1
> ```
> ![check_db_path.PNG](images/check_db_path.PNG)
>
> 3. Windows CMD or PowerShell 에서 복사
> ```bash
> > scp kmh@127.0.0.1:/home/kmh/myapi/myapi.db .
> ```
> ![copy_db.PNG](images/copy_db.PNG)
> 
> 4. DB Browser (SQLite) 에서 DB 열기
> ![open_db.png](images/open_db.png)

---

## 기능 구현 화면 캡처
- 회원가입
![스크린샷(111)](https://github.com/user-attachments/assets/31ea6a20-5477-4db3-a177-a6c66ec73185)
![스크린샷(112)](https://github.com/user-attachments/assets/29352b59-47c7-4ffb-9efd-94c079c66944)

- 로그인
![스크린샷(113)](https://github.com/user-attachments/assets/e8d5a255-5482-418d-9dec-9a273994a8e5)
![스크린샷(114)](https://github.com/user-attachments/assets/6e80384b-6720-48d1-8dc2-d7ae3b67f78e)

- 로그아웃
![스크린샷(114)](https://github.com/user-attachments/assets/0aaa916f-de2f-4304-9bd6-c4edcded6741)
![스크린샷(115)](https://github.com/user-attachments/assets/2f471feb-a94b-4f37-a193-bc5908ed4e11)

- 게시판
  - 게시글 번호, 제목, 답변개수, 작성자, 작성일시, 표시
  - 최대 10개의 게시글
![스크린샷(153)](https://github.com/user-attachments/assets/507e5a44-e007-4eea-b294-420f55ef9cb7)

- 게시판 페이징
  - 현재 페이지 기준 ± 5
![스크린샷(152)](https://github.com/user-attachments/assets/e0ea27c7-8931-4755-be41-abf70ac6f77c)

- 질문 등록
![스크린샷(116)](https://github.com/user-attachments/assets/5072bf72-e0cb-41f4-ae1d-ba4b3eabdce1)
![스크린샷(118)](https://github.com/user-attachments/assets/2c1c7419-26fe-499d-b079-875c408869f7)
![스크린샷(119)](https://github.com/user-attachments/assets/e3304042-cf73-4443-afe0-d8e108cec00f)
![스크린샷(120)](https://github.com/user-attachments/assets/10f8843b-b8aa-47a7-82ba-be9533cf7a0a)

- 질문 수정
![스크린샷(120)](https://github.com/user-attachments/assets/b8e13ba4-4c48-452b-9a32-aca56f33e780)
![스크린샷(121)](https://github.com/user-attachments/assets/95520691-ab82-4ccb-8278-a9ee72a4539c)
![스크린샷(122)](https://github.com/user-attachments/assets/b362b73a-c6c8-4b24-b922-bf6161c75b61)

- 답변 등록
![스크린샷(123)](https://github.com/user-attachments/assets/67877cec-0d38-42f6-a9bd-2f918fb43c2f)
![스크린샷(124)](https://github.com/user-attachments/assets/d0dca5c4-704b-4658-b5c8-a63d4e4b58d4)

- 답변 수정
![스크린샷(124)](https://github.com/user-attachments/assets/51f91a39-bd51-4da7-80c6-9b885618187c)
![스크린샷(125)](https://github.com/user-attachments/assets/e7e50e8b-59b0-4fb5-b093-ae91d35bc4df)
![스크린샷(126)](https://github.com/user-attachments/assets/b9e3f07d-1074-4e48-aaed-998a0c40b6ea)

- 질문/답변 추천
![스크린샷(132)](https://github.com/user-attachments/assets/19ef9084-ea6b-4407-b632-de3633dce66b)
![스크린샷(133)](https://github.com/user-attachments/assets/44134a29-95e0-4aee-82df-663f56cf08fa)
![스크린샷(134)](https://github.com/user-attachments/assets/a33ddb7c-da07-4802-b280-0245cf3f0b76)

- 답변 삭제
![스크린샷(135)](https://github.com/user-attachments/assets/dfb6a549-f8e2-4f76-9378-fba4c0c305a7)
![스크린샷(136)](https://github.com/user-attachments/assets/03a2e0db-0f51-4227-9b16-ac05131510d3)
![스크린샷(137)](https://github.com/user-attachments/assets/16b16068-dcd2-447a-8ccf-a6731e11c820)

- 질문 삭제
![스크린샷(138)](https://github.com/user-attachments/assets/e7055b38-d7fe-4f7e-8d42-33dd059f0118)
![스크린샷(139)](https://github.com/user-attachments/assets/9b342488-9731-408c-943b-f3c15579982f)

- 질문/답변 검색
![스크린샷(145)](https://github.com/user-attachments/assets/819e266d-ec3a-4bd2-a54a-d9c10b57a602)
![스크린샷(146)](https://github.com/user-attachments/assets/7ecad8f0-2549-462e-be86-bf5c875e5774)
![스크린샷(147)](https://github.com/user-attachments/assets/17bbe7de-c53c-4d27-90df-2682e3304e8a)

- 상세 게시글 목록 버튼
![스크린샷(157)](https://github.com/user-attachments/assets/b8963763-9d5d-4c9b-8685-4ba641ac58fb)
![스크린샷(158)](https://github.com/user-attachments/assets/8257ba9d-e5c2-4e79-8482-5656f919ab1e)
![스크린샷(159)](https://github.com/user-attachments/assets/4ee10ec5-730e-45ea-b631-d4f1a4e6d508)

- 네비게이션바 브랜드 버튼
![스크린샷(160)](https://github.com/user-attachments/assets/cfb9865c-1ba5-4ac2-aa39-8b7a4dd2cb74)
![스크린샷(161)](https://github.com/user-attachments/assets/9a7dba55-36d6-4655-ac2e-98e71ff137e7)

- 마크다운 형식 가능
![스크린샷(148)](https://github.com/user-attachments/assets/639d26ca-f711-4f62-b843-98090702dd3d)
![스크린샷(149)](https://github.com/user-attachments/assets/11bd9bc5-e785-4da5-8471-bc3013d41b92)
![스크린샷(150)](https://github.com/user-attachments/assets/057941a7-3d45-4db9-8225-b7e4c9f1c973)
![스크린샷(151)](https://github.com/user-attachments/assets/8e1182a1-3114-49a0-b26a-90ead77904a3)

---
