import dotenv
import os

dotenv.load_dotenv()

# Get environment variables
PORT = os.getenv("PORT")
DBURL = os.getenv("DBURL")
GITHUB_KEY = os.getenv("GITHUB_KEY")

# GitHub API
BASE_URL = "https://api.github.com"
HEADERS = {
    "authorization": f"token {GITHUB_KEY}",
    "accept": "application/vnd.github.v3+json",
}

# Ironhack data
OWNER = "ironhack-datalabs"
REPO = "datamad0820"
INSTRUCTORS = ["agalvezcorell", "ferrero-felipe"]