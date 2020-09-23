from src.db import db


def insert_student(student):
    """Insert student in database if not already in it."""
    # Check if student already in database
    query = {"name": student["name"]}
    if db["students"].find_one(query):
        return None

    # Perform insert
    return db["students"].insert_one(student).inserted_id


def fetch_students():
    """Fetch students from database."""
    cur = db["students"].find({})

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
    cur = db["pulls"].find({"lab": lab_name})

    # Check if collection is empty
    if cur.count() == 0:
        return None

    return list(cur)


def insert_lab(lab):
    """Insert analyzed lab in database."""
    return db["labs"].insert_one(lab).inserted_id


def fetch_lab(lab_id):
    """TODO Fetch a lab analysis from database."""
    pass
    