# 점프 투 FastAPI

> 개발환경 구성 
> - 개발환경 : VirtualBox + Ubuntu 22.04 Server
>   - 메모리 : 8GB
>   - 프로세서 : 4개 이상(pycharm, vscode 사용 때문)
>   - 비디오메모리 : 16MB
>   - 모니터개수 : 1개
>   - 저장소 메모리 : 25GB 이상
>   - 네트워크 : NAT 네트워크 포트포워딩
> - 백엔드 : FastAPI (uvicorn 실행)
> - 백엔드 프레임워크 : Pycharm 
> - 프론트엔드 : Svelte (Bootstrap 5.3.6 UI 기반)
> - 프론트엔드 프레임워크 : VS Code 
> - 데이터베이스 : SQLite
> - 배포용 GitHub Repository : khangte/fastapi_study

> - 가상환경 생성
> ```
> $ uv venv
> ```

> - 가상환경 활성화
> ```bash
> $ source .venv/bin/activate 
> ```

> - 가상환경 활성화
> ```bash
> $ source .venv/bin/activate 
> ```

> - 패키지 설치
> ```bash
> $ uv pip install fastapi uvicorn sqlalchemy```
> ```

> - 백엔드 실행코드
> ```bash
> $ uvicorn main:app --host 0.0.0.0 --port 8000
> ```

> - 프론트엔드 실행코드
> ```bash
> $ npm run dev
> ```
