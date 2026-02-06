import random
from datetime import datetime

# 채영님이 좋아하는 메뉴 리스트로 자유롭게 수정하세요!
menu_list = ["김치찌개", "마라탕", "돈가스", "연어초밥", "텐동", "쌀국수", "제육볶음", "샌드위치", "파스타"]

def pick_lunch():
    today = datetime.now().strftime("%Y-%m-%d")
    menu = random.choice(menu_list)
    result = f"{today} 추천 메뉴: {menu}\n"
    
    # 결과를 파일에 기록
    with open("lunch_history.txt", "a", encoding="utf-8") as f:
        f.write(result)
    
    print(f"✨ 오늘 점심은 {menu} 어떠세요? (기록 완료)")

if __name__ == "__main__":
    pick_lunch()