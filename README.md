
# Flask Todo App

This is a basic Flask web application for managing a to-do list. It demonstrates essential Flask concepts like routing, templating, database interaction with SQLAlchemy (including CRUD operations), and environmental variables.

## Features

- Add tasks to your to-do list.
- View all tasks.
- Mark tasks as complete or incomplete.
- Delete tasks.

## Setup Instructions

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/IsHereZahin/Python-Flask-Web-Development.git
   ```

2. **Navigate to the project directory:**
   ```bash
   cd Python-Flask-Web-Development
   ```

3. **Create a virtual environment:**
   ```bash
   python -m venv venv
   ```

4. **Activate the virtual environment:**
   ```bash
   # For Windows:
   venv\Scripts\activate
   # For macOS/Linux:
   source venv/bin/activate
   ```

5. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

6. **Initialize the database:**
   ```bash
   flask db init
   flask db migrate
   flask db upgrade
   ```

7. **Run the app:**
   ```bash
   flask run
   ```

## File Structure

```plaintext
/project-root
│
├── /migrations      # Database migration files
├── /static          # Static assets (CSS, JS, etc.)
├── /templates       # HTML templates for the app
├── /venv            # Virtual environment
├── app.py           # Main application file
├── .env             # Environment variables (not tracked by git)
├── .gitignore       # Git ignore rules
└── requirements.txt # List of dependencies
```
