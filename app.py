from flask import Flask, render_template

app = Flask(__name__)

# Route for the home page
@app.route("/")
@app.route("/home")
def home():
    return render_template('index.html')

# Route for the About page
@app.route("/about")
def about():
    return render_template('about.html')

if __name__ == "__main__":
    app.run(debug=True)