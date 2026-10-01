from flask import render_template
from src import app

@app.route("/")
@app.route("/index")
def index():
    posts = ["gloom", "light blue"]
    return render_template("index.html", title="Home", posts=posts)
