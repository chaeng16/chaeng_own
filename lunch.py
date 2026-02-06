import requests
from datetime import datetime

def get_dog_image():
    # Dog API에서 랜덤 사진 주소 가져오기
    try:
        response = requests.get("https://dog.ceo/api/breeds/image/random")
        if response.status_code == 200:
            return response.json()['message']
    except:
        return "사진을 가져오지 못했어요 😢"

def save_dog_log():
    today = datetime.now().strftime("%Y-%m-%d %H:%M")
    dog_url = get_dog_image()
    
    # 저장할 문구
    log_entry = f"[{today}] 오늘의 강아지 📸 : {dog_url}\n"
    
    # dog_log.txt 파일에 차곡차곡 기록 (파일명도 센스 있게 바꿔봤어요!)
    with open("dog_log.txt", "a", encoding="utf-8") as f:
        f.write(log_entry)
    
    print(f"✅ 새로운 강아지 사진 수집 완료: {dog_url}")

if __name__ == "__main__":
    save_dog_log()