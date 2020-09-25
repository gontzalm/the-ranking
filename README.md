# the-ranking
Flask API project made in Ironhack August '20 cohort.

<a>
  <img src="https://cdn.onlinewebfonts.com/svg/img_544576.png" width="400" />
</a>

## Objective
The main objective of this project is to practice developing APIs with `flask`. The secondary objectives are learning how to integrate a *MongoDB* database with an API (via `pymongo`) and practice deploying an API to the cloud using *Heroku* and *Docker*. 

The API built allows creating users (students of the Ironhack DataMAD Aug '20 cohort) in order to analyze their pull requests for different course *laboratories*.

## Project Structure
The structure and contents of the project are as follows:
- `docker/`: Dockerfile and package requiremets for the container.
- `src/`: Source code files.
  - `controllers/`: API controllers.
    1. `labs_controller.py`: Controller for the lab endpoints.
    2. `students_controller.py`: Controller for the student endpoints.
  1. `app.py`: App creation.
  2. `db.py`: Database connection.
  3. `dbops.py`: Database operations.
  4. `github.py`: GitHub API requests.
  5. `helpers.py`: Helper functions.
- `config.py`: Configuration parameters.
- `dbsync.sh`: Script to sync the local *MongoDB* database with a *MongoDB Atlas* cluster.
- `server.py`: App run.

## API Usage

## References
1. [`flask`](https://flask.palletsprojects.com/en/1.1.x/)
2. [`pymongo`](https://pymongo.readthedocs.io/en/stable/)
3. [*MongoDB*](https://www.mongodb.com/community)
4. [*Heroku*](https://www.heroku.com/)
5. [*Docker*](https://www.docker.com/docker-community)
