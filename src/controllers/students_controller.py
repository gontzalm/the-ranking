from src.app import app
from src.db import db
from flask import request, Response
from src import github, dbops
from src.helpers import json_response 


@app.route("/student/create/<student_name>")
def create_student(student_name):
    """Add student to database."""
    # Fetch student
    student = github.fetch_user(student_name)
    if not student:
        return {
            "status": "Not found",
            "msg": "Please enter a valid github username.",
        }, 400

    # Add student to database
    inserted_id = dbops.insert_student(student) 
    if not inserted_id:
        return {
            "status": "Conflict",
            "msg": f"The student {student['name']} is already in the database",
        }, 409

    # Fetch student's pull requests 
    pulls = github.fetch_pulls(student_name)

    # Add pulls to database
    dbops.insert_pulls(pulls)
    
    # JSON response
    response = {
        "status": "OK",
        "msg": f"Student {student['name']} added succesfully.",
        "student_id": inserted_id
    }
    return json_response(response)

@app.route("/student/all")
def list_students():
    """List all students in database."""
    students = dbops.fetch_students()
    if not students:
        return {
            "status": "Not found",
            "msg": "The database is empty",
        }, 404
    
    # JSON response
    return json_response(students)