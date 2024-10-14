from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SECRET_KEY'] = '02cb294d2689485d8910bb850d9bc2e2'
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# Route for the home page
datas = {
    "name": "Zahin",
    "numbers": [1, 2, 3, 4, 5, 6, 7, 8, 9]
}

@app.route("/")
@app.route("/home")
def home():
    return render_template('index.html', data=datas)

# Route for the About page
@app.route("/about")
def about():
    return render_template('about.html')


class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    completed = db.Column(db.Boolean)



# Route for the Todo page
todo_app_data = {
    "title": "Todo List Management",
    "description": "The Flask Todo Application is a simple web app for managing tasks. Users can add, view, and update tasks in a clean, user-friendly interface, showcasing Flask's dynamic capabilities.",
    "tasks": [
        {
            "id": 1,
            "title": "Task 1",
            "completed": False,
        },
        {
            "id": 2,
            "title": "Task 2",
            "completed": True,
        },
        {
            "id": 3,
            "title": "Task 3",
            "completed": False,
        },
    ]
}

last_task_id = max(task["id"] for task in todo_app_data["tasks"]) if todo_app_data["tasks"] else 0

@app.route("/todo", methods=["GET", "POST"])
def todo():
    global last_task_id
    if request.method == "POST":
        title = request.form["title"]
        print("Title:", title)

        last_task_id += 1

        new_task = {
            "id": last_task_id,
            "title": title,
            "completed": False
        }
        todo_app_data["tasks"].append(new_task)

    return render_template("todo.html", data=todo_app_data)

@app.route("/task/delete/<int:taskid>")
def deletetask(taskid):
    global todo_app_data
    todo_app_data["tasks"] = [task for task in todo_app_data["tasks"] if task["id"] != taskid]
    return redirect(url_for('todo'))

@app.route("/task/edit/<int:taskid>", methods=["GET", "POST"])
def edit_task(taskid):
    global todo_app_data

    task_to_edit = next((task for task in todo_app_data["tasks"] if task["id"] == taskid), None)

    if request.method == "POST":
        # Update the task with new title and completed status from the form
        new_title = request.form["title"]
        new_completed = request.form["completed"] == "True"  # Convert string to boolean
        if task_to_edit:
            task_to_edit["title"] = new_title  # Update task title
            task_to_edit["completed"] = new_completed  # Update completed status
            return redirect(url_for('todo'))  # Redirect after update

    return render_template("edit_task.html", task=task_to_edit)

if __name__ == "__main__":
    app.run(debug=True)
