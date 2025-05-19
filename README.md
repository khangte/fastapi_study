# 점프 투 FastAPI

> ## 개발환경 구성 
> - 개발환경 : VirtualBox + Ubuntu 22.04 Server
>   - 메모리 : 8GB
>   - 프로세서 : 4개 이상(pycharm, vscode 사용 때문)
>   - 비디오메모리 : 16MB
>   - 모니터개수 : 1개
>   - 저장소 메모리 : 10GB 이상
>   - 네트워크 : NAT 네트워크 포트포워딩
> - 백엔드 : FastAPI (uvicorn 실행)
> - 백엔드 프레임워크 : Pycharm 
> - 프론트엔드 : Svelte (Bootstrap 5.3.6 UI 기반)
> - 프론트엔드 프레임워크 : VS Code 
> - 데이터베이스 : SQLite
> - 배포용 GitHub Repository : khangte/fastapi_study

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
> - 패키지 설치
> ```bash
> $ uv pip install fastapi uvicorn sqlalchemy
> ```

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
> $ scp kmh@127.0.0.1:/home/kmh/myapi/myapi.db .
> ```
> ![copy_db.PNG](images/copy_db.PNG)
> 
> 4. DB Browser (SQLite) 에서 DB 열기
> ![open_db.png](images/open_db.png)

---

