from src.app import app
from src.db import db
from flask import request

@app.route("/student/create/<student_name>")
def create_student(student_name):
    

@app.route("/student/all")
def list_students():
    pass