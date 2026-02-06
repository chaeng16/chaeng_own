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
    
    # README 맨 위에 보일 제목과 사진
    log_entry = f"## 📅 {today} 오늘의 강아지 🐶\n![귀여운 강아지]({dog_url})\n\n---\n"
    
    # 💡 파일을 README.md로 변경!
    with open("README.md", "a", encoding="utf-8") as f:
        f.write(log_entry)
    
    print(f"✅ README에 강아지 배달 완료!")

if __name__ == "__main__":
    save_dog_log()