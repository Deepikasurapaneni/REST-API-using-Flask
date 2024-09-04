# REST-API-using-Flask
This project demonstrates my learning experience in building a REST API using Python and Flask, with integration of SQLAlchemy for database management. The API is designed to handle various HTTP requests, manage JSON data, and interact with a database to perform CRUD operations.

# Features
Minimal "Hello, World!" API: A simple starting point to understand the basics of creating a Flask REST API.
Resource Management: Ability to add, update, retrieve, and delete resources through various API endpoints.
JSON Handling: The API processes and returns data in JSON format, making it easy to interact with.
Argument Parsing: Supports passing arguments to endpoints and validating incoming request data.
In-Memory Data Storage: Temporarily store data in memory for testing and development purposes.
HTTP Status Codes: The API responds with appropriate status codes based on the outcome of requests.
Database Integration: Configured with SQLAlchemy to manage persistent data storage and retrieval.
Model Creation: Defined models to represent data structure within the database.
CRUD Operations: Supports creating, reading, updating, and deleting entries in the database.
Object Serialization: Converts Python objects into JSON format for easy API responses.
# Installation:
To run this project locally, follow these steps:

Install Dependencies:
pip install -r requirements.txt

Run the Application:
python app.py

Test the API: 
Use tools like Postman or CURL to send requests to the API endpoints.

# Project Structure
main.py: Main application file where the Flask app is initialized and routes are defined.

database.db: Stores the objects in the database

test.py: Contains the database models used by SQLAlchemy.

requirements.txt: Lists the Python dependencies needed for the project.

README.md: Project documentation.
