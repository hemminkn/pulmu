from flask import render_template, flash, redirect, url_for
from src import app
from pathlib import Path
import json

posts_dir = Path("templates/posts")

@app.route("/")
@app.route("/home")
def home():
    posts = []

    for post_dir in posts_dir.iterdir():
        if post_dir.is_dir():
            with open(post_dir/"meta.json") as f:
                meta = json.load(f)

                posts.append({"title": meta["title"], "slug": post_dir.name})
                print(posts)
    return render_template("home.html", posts=posts[:4])

@app.route("/contact")
def contact():

    return render_template("contact.html", title="contact")

@app.route("/about")
def about():
    return render_template("about.html", title="about")

@app.route("/posts")
def posts():
    all_posts = []

    for post_dir in posts_dir.iterdir():
        if post_dir.is_dir():
            with open(post_dir/"meta.json") as f:
                meta = json.load(f)

            all_posts.append({"title": meta["title"], "slug": post_dir.name})

    return render_template("posts.html", posts=all_posts)

@app.route("/posts/<slug>")
def show_post(slug): #slug is post's directory's name
    post_dir = posts_dir/slug

    return render_template(f"posts/{slug}/post.html")

