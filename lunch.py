import requests
from datetime import datetime

def get_dog_image():
    try:
        response = requests.get("https://dog.ceo/api/breeds/image/random")
        if response.status_code == 200:
            return response.json()['message']
    except:
        return "https://via.placeholder.com/150?text=Error"

def save_dog_log():
    today = datetime.now().strftime("%Y-%m-%d %H:%M")
    dog_url = get_dog_image()
    
    # 💡 핵심: 사진이 보이게 마크다운 문법으로 변경!
    log_entry = f"### 📅 {today}\n![귀여운 강아지]({dog_url})\n\n---\n"
    
    # 파일 확장자를 .md로 변경
    with open("dog_log.md", "a", encoding="utf-8") as f:
        f.write(log_entry)
    
    print(f"✅ 강아지 사진 수집 및 이미지 변환 완료!")

if __name__ == "__main__":
    save_dog_log()