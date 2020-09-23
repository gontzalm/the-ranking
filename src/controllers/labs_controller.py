from src.app import app
from src.db import db
from src import dbops
from src.helpers import analyze_lab, json_response

@app.route("/lab/create")
def create_lab():
    """TODO Add lab to database."""
    # EXTRACT 'LABNAME' FROM POST

    # Check if lab already in database
    if db["labs"].find_one({"name": lab_name}):
        return {
            "status": "Conflict"
            "msg": "This lab already exists."
        }, 409
    
    # Fetch pulls of lab
    pulls = dbops.fetch_pulls(lab_name)
    if not pulls:
        return {
            "status": "Not found",
            "msg": "Please enter a valid lab name.",
        }, 404

    # Analyze pulls of lab
    lab = analyze_lab(pulls)

    # Insert/update lab
    insterted_id = dbops.insert_lab(lab)
    
    # JSON response
    response = {
        "status": "OK",
        "msg": f"Lab {lab_name} created succesfully.",
        "id": insterted_id,
    }

    return json_response(response)


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
