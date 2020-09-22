from src.db import db

def insert_student(student):
    """Insert a student in the database if it is not already in it."""
    # Check if student is in database
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

def insert_pull_requets(pull_requests):
    """TODO Insert pull requets in the database."""
    pass

