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

# Database model for Todo tasks
class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    completed = db.Column(db.Boolean, default=False)

# Route for the Todo page
@app.route("/todo", methods=["GET", "POST"])
def todo():
    if request.method == "POST":
        title = request.form["title"]
        new_task = Todo(title=title)
        db.session.add(new_task)
        db.session.commit()
        return redirect(url_for('todo'))

    # Fetch all tasks from the database
    tasks = Todo.query.all()

    # Define the data dictionary
    data = {
        "title": "Todo List Management",
        "description": "The Flask Todo Application is a simple web app for managing tasks. Users can add, view, and update tasks in a clean, user-friendly interface.",
        "tasks": tasks
    }

    return render_template("todo.html", data=data)

@app.route("/task/delete/<int:taskid>")
def deletetask(taskid):
    task_to_delete = Todo.query.get(taskid)
    if task_to_delete:
        db.session.delete(task_to_delete)
        db.session.commit()
    return redirect(url_for('todo'))

@app.route("/task/edit/<int:taskid>", methods=["GET", "POST"])
def edit_task(taskid):
    task_to_edit = Todo.query.get(taskid)
    if not task_to_edit:
        return redirect(url_for('todo'))  # Redirect if task not found

    if request.method == "POST":
        task_to_edit.title = request.form["title"]
        task_to_edit.completed = request.form.get("completed") == "True"
        db.session.commit()
        return redirect(url_for('todo'))

    return render_template("edit_task.html", task=task_to_edit)

if __name__ == "__main__":
    app.run(debug=True)
