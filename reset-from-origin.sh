#!/bin/bash

echo "📥 원격 저장소에서 코드 가져오는 중..."
git fetch origin

echo "🧹 로컬 코드를 origin/main 기준으로 초기화합니다..."
git reset --hard origin/main

echo ""
echo "📜 최근 커밋 로그:"
git log --oneline

echo ""
echo "📂 현재 Git 상태:"
git status

echo ""
echo "✅ 완료: 로컬이 origin/main과 동일해졌습니다."
