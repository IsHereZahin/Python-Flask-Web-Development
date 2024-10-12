from flask import Flask, render_template, request
import random

app = Flask(__name__)

# Route for the home page
datas = {
    "name": "Zahin",
    "numbers":[1,2,3,4,5,6,7,8,9]
}
@app.route("/")
@app.route("/home")
def home():
    return render_template('index.html', data=datas)

# Route for the About page
@app.route("/about")
def about():
    return render_template('about.html')

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

@app.route("/todo", methods=["GET", "POST"])
def todo():
    if request.method == "POST":
        title = request.form["title"]
        print("Title:", title)

        new_task = {
            "id": random.randint(1, 11),
            "title": title,
            "completed": False
        }
        todo_app_data["tasks"].append(new_task)

    return render_template("todo.html", data=todo_app_data)

if __name__ == "__main__":
    app.run(debug=True)