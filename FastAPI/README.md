# FastAPI example app

This repository contains code for asynchronous example api using the [Fast Api framework](https://fastapi.tiangolo.com/) ,Uvicorn server and Postgres Database to perform crud operations on notes.

## Installation method 1 (Run application locally)

1. Clone this Repo `git clone (https://github.com/kabirul/FastAPI-example)`
2. Cd into the Fast-Api folder
   `cd FastAPI-example`
3. Activate virtualenv
   `source /bin/activate`
4. Install the required packages
   `python -m pip install -r requirements.txt`
5. Start the app using Uvicorn
   `uvicorn app.main:app --reload --workers 1 --host 0.0.0.0 --port 8002`
6. Ensure you have a Postgres Database running locally.
   Additionally create a testdb db with user postgres having required priviledges
   OR
   Change the DATABASE_URL variable in the .env file to reflect db settings (user:password/db)
7. Check the app on [notes](http://localhost:8002/notes)
8. Api documentation generated on [docs](http://localhost:8002/docs)

## Installation method 2 (Run Locally using Docker)
1.Ensure [Docker](https://docs.docker.com/install/) is installed
2.Ensure [Docker Compose](https://docs.docker.com/compose/install/) is installed
3.Clone this Repo
`git clone (https://github.com/kabirul/FastAPI-example)`

4.`cd FastAPI-example`
5.Use Docker-Compose to spin up containers `docker-compose up -d --build`

6.If everything completes should be available on [notes](http://localhost:8002/notes)

7.Docs are generated on [docs](http://localhost:8002/docs)

## Tests

Tests are available using pytest
Run them using `pytest .` while in the root directory (/FastAPI-example)

## Documentation
Open API Documentation is provided by [Redoc](http://localhost:8002/redoc)
