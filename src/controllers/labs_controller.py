from src.app import app
from src.db import db

@app.route("/lab/create")
def create_lab():
    pass

@app.route("/lab/<lab_id>/search")
def analyze_lab(lab_id):
    pass

@app.route("/lab/memeranking")
def memeranking():
    pass

@app.route("/lab/<lab_id>/meme")
def random_meme(lab_id):
    pass
