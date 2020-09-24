from flask import Response
from bson import json_util
import re
import requests
from config import HEADERS, INSTRUCTORS
from datetime import datetime
from random import choice


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


def get_last_commit_time(pull):
    """Get time of last commit of a pull request."""
    url = f"{pull['pull_request']['url']}/commits"
    res = requests.get(url, headers=HEADERS)
    last = res.json()[-1]["commit"]["author"]["date"][:-1]
    return datetime.fromisoformat(last)


def get_closed_time(pull):
    """Get closed time of a pull request"""
    closed = pull["closed_at"][:-1]
    return datetime.fromisoformat(closed)


def get_memes(pull):
    """Get memes of a pull request"""
    memes = []
    img_re = re.compile(r"https://user-images[\S][^()]+")

    # Get memes of author
    if "user-images" in pull["body"]:
        meme = img_re.findall(pull["body"])[-1]
        memes.append(meme)

    # Get memes of instructor
    res = requests.get(pull["comments_url"], headers=HEADERS)
    comments = res.json()
    for comment in comments:
        if comment["user"]["login"] in INSTRUCTORS:
            found = img_re.findall(comment["body"])
            if found:
                meme = found[-1]
                memes.append(meme)
    
    return memes
    
    
def parse_pull(pull):
    """Parse GitHub API pull item."""
    # Check if pull is INVALID
    labels = pull["labels"]
    if labels: # pull is labeled
        if labels[0]["name"] == "INVALID":
            return None

    # Number
    number = int(pull["url"].split("/")[-1])

    # Lab
    title = pull["title"]
    lab = re.search(r"\w+(-\w+)+", title)
    if lab:
        lab = lab.group()
    else: # invalid title format
        return None

    # Authors
    authors = []
    authors.append(pull["user"]["login"])
    if len(title.split()) >= 5: # additional authors
        additional = get_additional_authors(pull)
        authors.extend(additional)

    # Status
    state = pull["state"]

    # Grade time
    if state == "closed":
        closed = get_closed_time(pull)
        last = get_last_commit_time(pull)
        grade_time = round((closed - last).total_seconds() / 3600, 2)
    else:
        grade_time = None

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


def analyze_lab(students, pulls):
    """Analyze lab."""
    # State
    open_pulls = sum([True for pull in pulls if pull["state"] == "open"])
    closed_pulls = len(pulls) - open_pulls
    completeness = round(closed_pulls/len(pulls)*100, 2)
    
    # Extract all authors and memes
    authors = []
    memes = []
    for pull in pulls:
        authors.extend(pull["authors"])
        memes.extend(pull["memes"])

    # Missing students
    missing = []
    for student in students:
        if student["username"] not in authors:
            missing.append(student["username"])
    
    total_missing = len(missing)

    # Grade time (max)
    if completeness == 100:
        grade_time = max([pull["grade_time"] for pull in pulls])
    else:
        grade_time = None

    return {
        "name": pulls[0]["lab"],
        "open_pulls": open_pulls,
        "closed_pulls": closed_pulls,
        "completeness": completeness,
        "missing_pulls": {
            "total": total_missing,
            "students": missing,
        },
        "memes": memes,
        "grade_time": grade_time
    }


def gen_random_meme(lab):
    """Generate random meme from lab."""
    return choice(list(set(lab["memes"])))


def ranking(lab):
    """Generate meme ranking of lab"""
    unique_memes = list(set(lab["memes"]))

    ranking = []
    for meme in unique_memes:
        ranking.append({
            "meme": meme,
            "count": unique_memes.count(meme),
        })

    ranking.sort(key=lambda x: x["count"], reverse=True)

    return {
        "lab": lab["name"],
        "ranking": ranking
    }