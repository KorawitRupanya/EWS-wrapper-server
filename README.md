# EWS - HTTP server

A strategic wrapper has been implemented using the Flask API to encapsulate the functionalities of EWS (Emergent Web Server). The project includes the necessary API endpoints, establishing a well-defined and accessible interface for seamless interaction with the EWS exemplar.

## Table of Contents
- [How to Run the Project](#how-to-run-the-project)
- [Project Directories](#project-directories)
- [Dependencies](#dependencies)

## How to Run the Project

As a wrapper you would need to run the EWS first please follow the instruction in the quick start part of the README of EWS [here](https://github.com/robertovrf/emergent_web_server#quick-start)

After that please follow these steps:

1. **Build the Docker Image:**
    ```bash
    docker build -t ews-wrapper-server .
    ```

2. **Run the Docker Container:**
    ```bash
    docker run -p 5001:5000 ews-wrapper-server
    ```

   The application should now be accessible at [http://localhost:5001](http://localhost:5001).

   _> :warning: ** Note: Make sure Docker is installed on your machine.**_

## Project Directories

- __EWS\-wrapper\-server__
   - [Dockerfile](Dockerfile): Instructions for building the Docker image.
   - __app__ : This directory contains the main application code.
     - [\_\_init\_\_.py](app/__init__.py) : Entry point for creating the Flask application.
     - [extensions.py](app/extensions.py): Contains extensions for Flask (e.g., Flask-Restx).
     - [resources.py](app/resources.py): Defines the API resources and namespaces.
   - [requirements.txt](requirements.txt): Lists the Python dependencies for the project.

## Dependencies

- [Flask](https://flask.palletsprojects.com/en/3.0.x/)
- [Flask-Restx](https://flask-restx.readthedocs.io/en/latest/)
- [genson](https://pypi.org/project/genson/)
- [requests](https://pypi.org/project/requests/)

