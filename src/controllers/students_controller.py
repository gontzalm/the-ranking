from src.app import app
from src.db import db
from flask import request
from src import github, dbops


@app.route("/student/create/<student_name>")
def create_student(student_name):
    """Add student to database."""
    # Fetch student
    student = github.fetch_user(student_name)
    if not student:
        return {
            "status": "Not found",
            "msg": "Enter valid github username.",
        }, 404

    # Add student to database
    inserted_id = dbops.insert_student(student) 
    if not inserted_id:
        return {
            "status": "Conflict",
            "msg": f"Student {student['username']} already in database.",
        }, 409

    # Fetch student's pull requests 
    pulls = github.fetch_pulls(student_name)

    # Add pulls to database
    dbops.insert_pulls(pulls)
    
    return {
        "status": "OK",
        "msg": f"Student {student['name']} added succesfully.",
        "student_id": inserted_id
    }

@app.route("/student/all")
def list_students():
    """List all students in database."""
    students = dbops.fetch_students()
    if not students:
        return {
            "status": "Not found",
            "msg": "No students in database.",
        }, 404
    
    return {
        "status": "OK",
        "msg": "Students retrieved successfuly.",
        "students": students,
    }