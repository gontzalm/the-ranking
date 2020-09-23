from src.db import db


def insert_student(student):
    """Insert a student in the database if it is not already in it."""
    # Check if student already in database
    query = {"name": student["name"]}
    if db["students"].find_one(query):
        return None

    # Perform insert
    return db["students"].insert_one(student).inserted_id


def fetch_students():
    """Fetch students from the database."""
    cur = db["students"].find({})

    # Check if collection is empty
    if cur.count() == 0:
        return None

    return list(cur)


def insert_pulls(pulls):
    """TODO Insert pull requets in the database."""
    for pull in pulls:
        # Check if pull already in database
        query = {"number": pull["number"]}
        if db["pulls"].find_one(query):
            continue
        
        db["pulls"].insert_one(pull)