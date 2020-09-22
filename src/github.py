import requests
from config import BASE_URL, HEADERS, OWNER, REPO
from src.helpers import parse_pull

def fetch_user(username):
    """Fetch user from GitHub API."""
    url = f"{BASE_URL}/users/{username}"
    res = requests.get(url, headers=HEADERS)
    
    # Not found
    if res.status_code == 404:
        return None
    
    # Parse student
    data = res.json()
    return {
        "name": data["name"],
        "username": username,
        "avatar": data["avatar_url"],
    }

def fetch_pulls(username):
    """TODO (see test nb) Fetch pull requests of a username from GitHup API."""

