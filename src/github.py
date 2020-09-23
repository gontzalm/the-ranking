import requests
from config import BASE_URL, HEADERS, OWNER, REPO
from src.helpers import parse_pull


def fetch_user(username):
    """Fetch user from GitHub API."""
    # Perform HTTP GET
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
    """Fetch pull requests of a student from GitHup API."""
    # Perform HTTP GET
    url = f"{BASE_URL}/search/issues"
    params = {
        "q": f"repo:{OWNER}/{REPO} is:pr involves:{username}",
        "per_page": 100
    }
    res = requests.get(url, headers=HEADERS, params=params)
    data = res.json()

    # Parse pulls
    pulls = []
    for raw_pull in data["items"]:
        pull = parse_pull(raw_pull)
        if pull:
            pulls.append(pull)
    
    return pulls