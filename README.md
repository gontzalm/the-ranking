# the-ranking
Flask API project made in Ironhack August '20 cohort.

<a>
  <img src="https://cdn.onlinewebfonts.com/svg/img_544576.png" width="400" />
</a>

## Objective
The main objective of this project is to practice API development with `flask`. The secondary objectives are learning how to integrate a *MongoDB* database with an API (via `pymongo`) and practice deploying an API to the cloud using *Heroku* containerized with *Docker*. 

The API built allows creating users (students of the Ironhack DataMAD Aug '20 cohort) in order to analyze their pull requests for different course *laboratories*.

## Project Structure
The structure and contents of the project are as follows:
- `docker/`: Dockerfile and package requiremets for the container.
- `src/`: Source code files.
  - `controllers/`: API controllers.
    - `labs_controller.py`: Controller for the lab endpoints.
    - `students_controller.py`: Controller for the student endpoints.
  - `app.py`: App creation.
  - `db.py`: Database connection.
  - `dbops.py`: Database operations.
  - `github.py`: GitHub API requests.
  - `helpers.py`: Helper functions.
- `config.py`: Configuration parameters.
- `dbsync.sh`: Script to sync the local *MongoDB* database with a *MongoDB Atlas* cluster.
- `server.py`: App run.

## API Usage
#### Access: 
`https://the-ranking-gontzal.herokuapp.com`

#### Endpoints:

`(GET) /` Homepage.
```json
{
    "msg": "Welcome to the-ranking-gontzal!",
    "status": "OK"
}
```

`(GET) /student/create/<username>` Create a new student.
```json
{
        "msg": "Student rfminguez added succesfully.",
        "status": "OK",
        "student_id": "5f6df23d02a1808530397a9f"
}
```

`(GET) /student/all` List all the students in the database.
```json
{
    "msg": "Students retrieved successfuly.",
    "status": "OK",
    "students": [
        {
            "avatar": "https://avatars1.githubusercontent.com/u/63603386?v=4",
            "name": "Gontzal Monasterio",
            "username": "gontzalm"
        },
        {
            "avatar": "https://avatars1.githubusercontent.com/u/5184420?v=4",
            "name": null,
            "username": "rfminguez"
        },
        ...
```

`(POST) /lab/create` Create a lab via a POST form `lab_name=<lab_name>`.
```json
{
    "id": "5f6df23d02a1808530397a9f",
    "msg": "Lab lab-api-scavenger-game created successfully.",
    "status": "OK"
}
```

`(GET) /lab/<lab-id>/search` Search a lab in the database and return its analysis.
```json
{
    "analysis": {
        "closed_pulls": 11,
        "completeness": 100.0,
        "grade_time": 141.23,
        "memes": [
            "https://user-images.githubusercontent.com/57899051/92721831-f9b7af80-f366-11ea-94c8-016dc002e278.jpg",
            "https://user-images.githubusercontent.com/57899051/92724207-857f0b00-f36a-11ea-8662-0fef1f36dafb.jpg",
            "https://user-images.githubusercontent.com/57899051/92721357-451d8e00-f366-11ea-9cae-70548bafd6fc.jpg",
            "https://user-images.githubusercontent.com/52798316/93099913-debba700-f6a8-11ea-9653-ce5b2a5e6d7d.png",
            "https://user-images.githubusercontent.com/57899051/92743489-def23480-f380-11ea-950f-939509b20ae0.jpg",
            "https://user-images.githubusercontent.com/52798316/93095414-5b4b8700-f6a3-11ea-8023-8f961b73cee1.png",
            "https://user-images.githubusercontent.com/52798316/93094512-4c180980-f6a2-11ea-9332-68c0ca570462.png",
            "https://user-images.githubusercontent.com/57899051/92722772-61222f00-f368-11ea-8ed2-2a7ccb64b4c7.jpg"
        ],
        "missing_pulls": {
            "students": [
                "Diegon8",
                "Jav1-Mart1nez",
                "Daniel-GarciaGarcia"
            ],
            "total": 3
        },
        "name": "lab-api-scavenger-game",
        "open_pulls": 0
    },
    "msg": "lab-api-scavenger-game retrieved successfully.",
    "status": "OK"
}
```

`(GET) /lab/<lab-id>/meme` Generate a random meme used in a lab.
```json
{
    "msg": "Random meme from lab-api-scavenger-game generated successfully.",
    "random_meme": "https://user-images.githubusercontent.com/57899051/92721831-f9b7af80-f366-11ea-94c8-016dc002e278.jpg",
    "status": "OK"
}
```

`(GET) /lab/memeranking` Generate a meme ranking for each lab.
```json
{
    "msg": "Meme ranking generated successfully.",
    "rankings": [
        {
            "lab": "lab-api-scavenger-game",
            "ranking": [
                {
                    "count": 1,
                    "meme": "https://user-images.githubusercontent.com/57899051/92721831-f9b7af80-f366-11ea-94c8-016dc002e278.jpg"
                },
                {
                    "count": 1,
                    "meme": "https://user-images.githubusercontent.com/57899051/92724207-857f0b00-f36a-11ea-8662-0fef1f36dafb.jpg"
                },
                {
                    "count": 1,
                    "meme": "https://user-images.githubusercontent.com/57899051/92721357-451d8e00-f366-11ea-9cae-70548bafd6fc.jpg"
                },
                {
                    "count": 1,
                    "meme": "https://user-images.githubusercontent.com/52798316/93099913-debba700-f6a8-11ea-9653-ce5b2a5e6d7d.png"
                },
                {
                    "count": 1,
                    "meme": "https://user-images.githubusercontent.com/57899051/92743489-def23480-f380-11ea-950f-939509b20ae0.jpg"
                },
                {
                    "count": 1,
                    "meme": "https://user-images.githubusercontent.com/52798316/93095414-5b4b8700-f6a3-11ea-8023-8f961b73cee1.png"
                },
                {
                    "count": 1,
                    "meme": "https://user-images.githubusercontent.com/52798316/93094512-4c180980-f6a2-11ea-9332-68c0ca570462.png"
                },
                {
                    "count": 1,
                    "meme": "https://user-images.githubusercontent.com/57899051/92722772-61222f00-f368-11ea-8ed2-2a7ccb64b4c7.jpg"
                }
            ]
        }
    ],
    "status": "OK"
}
```

## References
1. [`flask`](https://flask.palletsprojects.com/en/1.1.x/)
2. [`pymongo`](https://pymongo.readthedocs.io/en/stable/)
3. [*MongoDB*](https://www.mongodb.com/community)
4. [*Heroku*](https://www.heroku.com/)
5. [*Docker*](https://www.docker.com/docker-community)
