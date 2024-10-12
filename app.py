from flask import Flask

app = Flask(__name__)

# Route for the home page
@app.route("/")
def home():
    return "<h1 style='color:#0D1117; text-align:center;'>Welcome to the Flask homepage</h1>"

# Route for the About page
@app.route("/about")
def about():
    return "<h1 style='color:#0D1117;'>This is the Flask 'About' page</h1>"

if __name__ == "__main__":
    app.run(debug=True)