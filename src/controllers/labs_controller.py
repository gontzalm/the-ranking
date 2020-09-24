from src.app import app
from src.db import db
from src import dbops
from src.helpers import analyze_lab
from flask import request

@app.route("/lab/create", methods=["POST"])
def create_lab():
    """TODO Add lab to database."""
    # Get lab name from POST
    lab_name = request.form.get("lab_name")
    if not lab_name:
        return {
            "status": "Bad request",
            "msg": "Enter a valid lab name."
        }, 400

    # Check if lab already in database
    if db["labs"].find_one({"name": lab_name}):
        return {
            "status": "Conflict",
            "msg": "This lab already exists."
        }, 409
    
    # Fetch students
    students = dbops.fetch_students(project=["username"])
    if not students:
        return {
            "status": "Not found",
            "msg": "No students in database."
        }, 404

    # Fetch pulls of lab
    pulls = dbops.fetch_pulls(lab_name)
    if not pulls:
        return {
            "status": "Not found",
            "msg": "Enter a valid lab name.",
        }, 404

    # Analyze pulls of lab
    lab = analyze_lab(students, pulls)

    # Insert/update lab
    insterted_id = dbops.insert_lab(lab)
    
    return {
        "status": "OK",
        "msg": f"Lab {lab_name} created succesfully.",
        "id": insterted_id,
    }


@app.route("/lab/<lab_id>/search")
def search_lab(lab_id):
    """TODO Search database for lab."""
    

    pass

@app.route("/lab/memeranking")
def meme_ranking():
    """TODO Show meme ranking."""
    pass

@app.route("/lab/<lab_id>/meme")
def random_meme(lab_id):
    """TODO Select a random meme from lab."""
    pass
