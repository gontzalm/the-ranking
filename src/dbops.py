from src.db import db
from bson.objectid import ObjectId
from bson.errors import InvalidId

def insert_student(student):
    """Insert student in database if not already in it."""
    # Check if student already in database
    query = {"username": student["username"]}
    if db["students"].find_one(query):
        return None

    # Perform insert
    oid = db["students"].insert_one(student).inserted_id
    return str(oid)


def fetch_students(project=None):
    """Fetch students from database."""
    projection = {"_id": 0}
    if project:
        if isinstance(project, list):
            for attr in project:
                projection[attr] = 1
        else:
            projection[project] = 1

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
    cur = db["pulls"].find({"lab": lab_name}, projection={"_id": 0})

    if cur.count() == 0:
        return None

    return list(cur)


def insert_lab(lab):
    """Insert lab in database."""
    oid = db["labs"].insert_one(lab).inserted_id
    return str(oid)


def fetch_lab(lab_id):
    """Fetch lab from database."""
    try:
        return db["labs"].find_one(ObjectId(lab_id), projection={"_id": 0})
    except InvalidId:
        return None

def fetch_labs(project=None):
    """Fetch all labs from database."""
    projection = {"_id": 0}
    if project:
        if isinstance(project, list):
            for attr in project:
                projection[attr] = 1
        else:
            projection[project] = 1

    cur = db["labs"].find({}, projection=projection)

    if cur.count() == 0:
        return None

    return list(cur)