import requests
from config import BASE_URL, HEADERS, OWNER, ENDPOINTS

def fetch_user(username):
    res = requests.get(f"{BASE_URL}/{ENDPOINTS["user"]}", headers=HEADERS)
    return {
        "name": data["name"],
        "username": user,
        "avatar": data["avatar_url"],
    }    
