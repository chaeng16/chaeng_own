# 🍔 chaeng_own: 점심 메뉴 자동 추천 시스템

이 프로젝트는 GitHub Actions를 활용하여 매일 정해진 시간에 점심 메뉴를 추천하고 그 기록을 남기는 **자동화 파이프라인**입니다.

## 🛠️ 기술 스택
- **Language**: Python 3.9
- **Automation**: GitHub Actions
- **Storage**: GitHub Repository (lunch_history.txt)

## 🚀 작동 방식
1. 매일 설정된 시간에 GitHub Actions가 실행됩니다.
2. `lunch.py`가 실행되어 리스트 중 하나의 메뉴를 랜덤으로 선정합니다.
3. 선정된 메뉴는 날짜와 함께 `lunch_history.txt` 파일에 자동으로 기록됩니다.