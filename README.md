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
> ## 실행코드
> - 백엔드 실행코드
> ```bash
> $ uvicorn main:app --host 0.0.0.0 --port 8000
> ```
> - 프론트엔드 실행코드
> ```bash
> $ npm run dev
> ```

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

> ## uv 가상환경
> - 가상환경 생성
> ```
> $ uv venv
> ```
> - 가상환경 활성화
> ```bash
> $ source .venv/bin/activate 
> ```

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

> Alembic 마이그레이션 과정
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

## 개발 과정 화면 캡처

---

### 3-14 검색
1. 검색 상자 생성 
![스크린샷(106) - 복사본.png](images/%EC%8A%A4%ED%81%AC%EB%A6%B0%EC%83%B7%28106%29%20-%20%EB%B3%B5%EC%82%AC%EB%B3%B8.png)
2. 검색 실행 
![스크린샷(107) - 복사본.png](images/%EC%8A%A4%ED%81%AC%EB%A6%B0%EC%83%B7%28107%29%20-%20%EB%B3%B5%EC%82%AC%EB%B3%B8.png)
![스크린샷(108).png](images/%EC%8A%A4%ED%81%AC%EB%A6%B0%EC%83%B7%28108%29.png)
3. 게시물 확인
![스크린샷(109).png](images/%EC%8A%A4%ED%81%AC%EB%A6%B0%EC%83%B7%28109%29.png)
4. '목록' 버튼 클릭
![스크린샷(109).png](images/%EC%8A%A4%ED%81%AC%EB%A6%B0%EC%83%B7%28109%29.png)
![스크린샷(108).png](images/%EC%8A%A4%ED%81%AC%EB%A6%B0%EC%83%B7%28108%29.png)
5. 'pybo' 네비게이션-브랜드 버튼 클릭
![스크린샷(108) - 복사본.png](images/%EC%8A%A4%ED%81%AC%EB%A6%B0%EC%83%B7%28108%29%20-%20%EB%B3%B5%EC%82%AC%EB%B3%B8.png)
![스크린샷(106).png](images/%EC%8A%A4%ED%81%AC%EB%A6%B0%EC%83%B7%28106%29.png)

---

### 3-15 프론트엔드 빌드

