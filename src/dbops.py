from src.db import db
from collections.abc import Iterable


def insert_student(student):
    """Insert student in database if not already in it."""
    # Check if student already in database
    query = {"username": student["username"]}
    if db["students"].find_one(query):
        return None

    # Perform insert
    oid = db["students"].insert_one(student).inserted_id
    return str(oid)


def fetch_students(project=None, exclude_id=True):
    """Fetch students from database."""
    projection = {}
    if project:
        if isinstance(project, Iterable):
            for attr in project:
                projection[attr] = 1
        else:
            projection[project] = 1
    if exclude_id:
        projection["_id"] = 0

    cur = db["students"].find({}, projection=projection)

    # Check if collection is empty
    if cur.count() == 0:
        return None

    return list(cur)


def insert_pulls(pulls):
    """Insert pull requets in database."""
    for pull in pulls:
        # Check if pull already in database
        query = {"number": pull["number"]}
        if db["pulls"].find_one(query):
            continue
        
        db["pulls"].insert_one(pull)


def fetch_pulls(lab_name):
    """Fetch all pull requests of a lab from database."""
    cur = db["pulls"].find({"lab": lab_name}, {"_id": False})

    # Check if collection is empty
    if cur.count() == 0:
        return None

    return list(cur)


def insert_lab(lab):
    """Insert analyzed lab in database."""
    oid = db["labs"].insert_one(lab).inserted_id
    return str(oid)


def fetch_lab(lab_id):
    """TODO Fetch a lab analysis from database."""
    pass
    