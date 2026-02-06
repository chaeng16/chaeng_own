import requests
import random
from datetime import datetime

def get_advice():
    # 1. 외부 API에서 데이터 가져오기 (랜덤 조언 API)
    response = requests.get("https://api.adviceslip.com/advice")
    if response.status_code == 200:
        data = response.json()
        return data['slip']['advice'] # API가 주는 조언 문구
    return "맛있게 드세요!"

def pick_lunch():
    menu_list = ["마라탕", "초밥", "돈가스", "쌀국수", "제육볶음", "샌드위치"]
    today = datetime.now().strftime("%Y-%m-%d %H:%M")
    menu = random.choice(menu_list)
    
    # 2. API로 가져온 데이터
    advice = get_advice()
    
    result = f"{today}\n🍴 점심 추천: {menu}\n💡 오늘의 한마디(API): {advice}\n"
    result += "-"*30 + "\n"
    
    with open("lunch_history.txt", "a", encoding="utf-8") as f:
        f.write(result)
    
    print(f"✅ API 데이터 수집 및 추천 완료!")

if __name__ == "__main__":
    pick_lunch()