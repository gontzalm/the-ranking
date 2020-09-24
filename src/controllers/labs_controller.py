from src.app import app
from src.db import db
from src import dbops
from src.helpers import analyze_lab, gen_random_meme, ranking
from flask import request

@app.route("/lab/create", methods=["POST"])
def create_lab():
    """Add lab to database."""
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
    students = dbops.fetch_students(project="username")
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
        "msg": f"Lab {lab_name} created successfully.",
        "id": insterted_id,
    }


@app.route("/lab/<lab_id>/search")
def search_lab(lab_id):
    """Search database for lab."""
    # Fetch lab
    lab = dbops.fetch_lab(lab_id)
    if not lab:
        return {
            "status": "Not found",
            "msg": "Enter a valid lab id."
        }, 404
    
    # Get UNIQUE memes
    lab["memes"] = list(set(lab["memes"]))

    return {
        "status": "OK",
        "msg": f"{lab['name']} retrieved successfully.",
        "analysis": lab,
    }
    

@app.route("/lab/memeranking")
def meme_ranking():
    """Generate meme ranking."""
    # Fetch labs
    labs = dbops.fetch_labs(project=["name", "memes"])
    if not labs:
        return {
            "status": "Not found",
            "msg": "No labs in database."
        }, 404
    
    # Ranking
    rankings = [ranking(lab) for lab in labs]
    
    return {
        "status": "OK",
        "msg": "Meme ranking generated successfully.",
        "rankings": rankings,
    }

@app.route("/lab/<lab_id>/meme")
def random_meme(lab_id):
    """Generate random meme from lab."""
    # Fetch lab
    lab = dbops.fetch_lab(lab_id)
    if not lab:
        return {
            "status": "Not found",
            "msg": "Enter a valid lab id."
        }, 404
    
    # Generate random meme
    random_meme = gen_random_meme(lab)

    return {
        "status": "OK",
        "msg": f"Random meme from {lab['name']} generated successfully.",
        "random_meme": random_meme,
    }