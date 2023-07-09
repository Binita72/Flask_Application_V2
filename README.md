# Flask REST API with MongoDB

This is a Flask application that provides a REST API for performing CRUD operations on a User resource. The User data is stored in a MongoDB database.

## Requirements

- Python 3.x
- Flask
- Flask-RESTful
- PyMongo

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/Binita72/Flask_Application_V2.git
   ```

2. Create and activate a virtual environment:

   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Start the Flask application:

   ```bash
   python server.py
   ```

   The application will run at `http://localhost:80`.

## API Endpoints

The following REST API endpoints are available:

- `GET /users`: Returns a list of all users.
- `POST /users`: Creates a new user.
- `GET /users/<id>`: Returns the user with the specified ID.
- `PUT /users/<id>`: Updates the user with the specified ID.
- `DELETE /users/<id>`: Deletes the user with the specified ID.

## Usage

You can use an HTTP client like cURL or Postman to interact with the API endpoints. For example:

- Retrieve all users:

  ```bash
  curl http://localhost:80/users
  ```

- Create a new user:

  ```bash
  curl -X POST -H "Content-Type: application/json" -d '{"name": "Indiana", "email": "Indi@example.com", "password": "secret"}' http://localhost:80/users
  ```

- Retrieve a specific user:

  ```bash
  curl http://localhost:80/users/<id>
  ```

- Update a user:

  ```bash
  curl -X PUT -H "Content-Type: application/json" -d '{"name": "Updated Name", "email": "updated@example.com", "password": "newpassword"}' http://localhost:80/users/<id>
  ```

- Delete a user:

  ```bash
  curl -X DELETE http://localhost:80/users/<id>
  ```

Make sure to replace `<id>` with the actual ID of the user you want to interact with.

## Configuration

The application connects to a local MongoDB database by default. If your MongoDB server is running on a different host or port, you can modify the connection URL in the code (`MongoClient('mongodb://localhost:27017/')`) to match your MongoDB server configuration.

## Database Setup

By default, the application assumes that a MongoDB database named `test2` is available. You can modify the database name in the code (`db = client['users']`) to match your desired database name.


### Feel free to modify and adapt this project to suit your needs.

---
