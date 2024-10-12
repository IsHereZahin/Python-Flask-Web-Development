from flask import Flask, render_template

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

if __name__ == "__main__":
    app.run(debug=True)