# To-Do List API

A basic To-Do list API using Django and Django Rest Framework (DRF).

## Requirements

- Python 3.x
- Django
- Django Rest Framework

## Setup

### 1. Clone the Repository

Clone the repository to your local machine using the following command:

```sh
git clone https://github.com/Ankit-ICY/TASK.git
cd todo-list-api
```
### 2. Create and Activate a Virtual Environment
Create a virtual environment to install dependencies in an isolated environment:

CREATE : ```python -m venv venv```
ACTIVATE : ```venv\Scripts\activate```


### 3. Install Dependencies
Install the required dependencies using pip:
```pip install -r requirements.txt```

### 4. Apply Migrations
Apply the database migrations to set up your database schema:
```
python manage.py makemigrations
python manage.py migrate
```

### 5. Run the Development Server
Start the Django development server: ```python manage.py runserver```

## Endpoints
Here are the endpoints provided by the API:

- Create Task: POST /api/tasks/
- Retrieve Task List: GET /api/tasks/
- Retrieve Single Task: GET /api/tasks/<id>/
- date Task: PUT/PATCH /api/tasks/<id>/
- Delete Task: DELETE /api/tasks/<id>/
- Tasks Due Today: GET /api/tasks/due-today/


## Validations
  Title: Ensure the title is not empty.
  Due Date: If provided, the due date should be a future date.

##Example Requests

### Create a Task

```
POST /api/tasks/
Content-Type: application/json

{
    "title": "Test Task",
    "description": "This is a test task.",
    "completed": false,
    "due_date": "2024-12-31"
}
```

### Retrieve Task List
```GET /api/tasks/```

### Retrieve Single Task
```GET /api/tasks/1/```

### Update a Task
```
PUT /api/tasks/1/
Content-Type: application/json

{
    "title": "Updated Task",
    "description": "This is an updated test task.",
    "completed": true,
    "due_date": "2024-01-01"
}
```

### Delete a Task
```DELETE /api/tasks/1/```











