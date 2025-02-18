# FastAPI Project

This is a FastAPI project that provides a RESTful API for managing users.

## Features

- Create, read, update, and delete users
- Secure password hashing
- SQLAlchemy ORM for database interactions

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/yourusername/your-repo.git
    cd your-repo
    ```

2. Create and activate a virtual environment:
    ```sh
    python -m venv fastapi-venv
    source fastapi-venv/bin/activate  # On Windows use `fastapi-venv\Scripts\activate`
    ```

3. Install the dependencies:
    ```sh
    pip install -r requirements.txt
    ```

## Usage

1. Start the FastAPI server:
    ```sh
    uvicorn main:app --reload
    ```

2. Open your browser and navigate to `http://127.0.0.1:8000/docs` to access the interactive API documentation.

## Endpoints

- **Create user**: `POST /user/`
- **Get all users**: `GET /user/`
- **Get user by ID**: `GET /user/{id}`
- **Update user**: `POST /user/{id}/update`
- **Delete user**: `GET /user/delete/{id}`

## Example

To create a new user, send a `POST` request to `/user/` with the following JSON body:
```json
{
  "username": "johndoe",
  "email": "johndoe@example.com",
  "password": "securepassword"
}

```

## Notes
After starting server fastapi-practise.db will appear can be run by TablePlus or any other database management tool.
Simple install it choose SQLlight find the file and run it.