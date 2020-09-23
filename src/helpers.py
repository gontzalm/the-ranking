from flask import Response
from bson import json_util
import re
import requests
from config import HEADERS, INSTRUCTORS
from datetime import datetime


def json_response(data):
    """ Process data with bson serializer to avoid ObjectID to string errors in flask."""
    return Response(
        json_util.dumps(data),
        mimetype='application/json'
    )


def get_additional_authors(pull):
    """Get additional authors from a pull request."""
    # Author(s) in body via @author
    if "@" in pull["body"]:
        additional = re.findall(r"@\w+", pull["body"])
        additional = [s.replace("@", "") for s in additional]
        return additional

    # Author(s) in comment via JOIN
    else:
        res = requests.get(pull["comments_url"], headers=HEADERS)
        comments = res.json()
        additional = []
        for comment in comments:
            if comment["body"] == "join":
                additional.append(comment["user"]["login"])
        return additional


def get_closed_time(pull):
    """Get closed time of a pull request"""
    closed = pull["closed_at"][:-1]
    return datetime.fromisoformat(closed)


def get_last_commit_time(pull):
    """Get time of last commit of a pull request."""
    url = f"{pull['pull_request']['url']}/commits"
    res = requests.get(url, headers=HEADERS)
    last = res.json()[-1]["commit"]["author"]["date"][:-1]
    return datetime.fromisoformat(last)


def get_memes(pull):
    """Get memes of a pull request"""
    memes = []
    img_re = re.compile(r"https://user-images.+\.(jpeg|jpg|png)")

    # Get memes of author
    if "user-images" in pull["body"]:
        meme = img_re.search(pull["body"]).group()
        memes.append(meme)

    # Get memes of instructor
    res = requests.get(pull["comments_url"], headers=HEADERS)
    comments = res.json()
    for comment in comments:
        if comment["user"]["login"] in INSTRUCTORS:
            meme = img_re.search(comment["body"]).group()
            memes.append(meme)
    
    return memes
    
    
def parse_pull(pull):
    """TODO Parse GitHub API pull item."""
    # Check if pull is INVALID
    labels = pull["labels"]
    if labels: # pull is labeled
        if labels[0]["name"] == "INVALID":
            return None

    # Number
    number = int(pull["url"].split("/")[-1])

    # Lab
    title = pull["title"]
    lab = re.search(r"\w+(-\w+)+", title).group()

    # Authors
    authors = []
    authors.append(pull["user"]["login"])
    if len(title.split()) >= 5: # additional authors
        additional = get_additional_authors(pull)
        authors.extend(additional)

    # Status
    state = pull["state"]

    # Grade time
    closed = get_closed_time(pull)
    last = get_last_commit_time(pull)
    grade_time = round((closed - last).total_seconds() / 3600, 2)

    # Memes
    memes = get_memes(pull)

    return {
        "number": number,
        "lab": lab,
        "authors": authors,
        "state": state,
        "grade_time": grade_time,
        "memes": memes,
    }


def analyze_lab(pulls):
    """TODO Analyze lab."""
    pass