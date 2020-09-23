from flask import Response
from bson import json_util
import re
import requests
from config import HEADERS


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


def parse_pull(pull):
    """TODO Parse GitHub API pull item."""
    # Check if INVALID
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
    
    # Memes

    return {
        "number": number,
        "lab": lab,
        "authors": authors,
        "state": state,
        #"grade_time": grade_time,
        #"memes": memes,
    }