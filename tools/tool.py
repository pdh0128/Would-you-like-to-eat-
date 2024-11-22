import requests
from dotenv import load_dotenv
import os
load_dotenv()

def search_food(*ingredients):
    """음식의 정보를 찾기위한 도구입니다."""
    FOOD_API_KEY = os.getenv("FOOD_API_KEY")
    headers = {
            "Authorization": FOOD_API_KEY,
            "Content-Type": "application/json"
        }
    URL_ = '&'.join(f"RCP_PARTS_DTLS={i}" for i in ingredients)
    URL = f"http://openapi.foodsafetykorea.go.kr/api/sample/COOKRCP01/json/1/20/{URL_}"
    # URL = f"http://openapi.foodsafetykorea.go.kr/api/sample/COOKRCP01/json/1/20/RCP_NM={food_name}"
    res = requests.get(url=URL, headers=headers)
    if res.status_code == 200:
        return res.json()
    else : return None

if __name__ == '__main__':
    print(search_food("김치찌개"))

