import requests
from flask import Flask, render_template

from post import Post

def get_data():
    res = requests.get("https://api.npoint.io/f988fe2f89471cfb558e")
    res.raise_for_status()
    data = res.json()
    return data

def get_posts():
    posts_objects = []
    posts_data = get_data()

    for post in posts_data:
        post_object = Post(post["title"], post["body"], post["description"], post["author"])
        posts_objects.append(post_object)

    return posts_objects

def get_specific_post(post_slug: str):
    all_posts = get_posts()
    searched_post = {}

    for post in all_posts:
        if post.slug == post_slug:
            searched_post = post
            break
    return searched_post

app = Flask(__name__)

@app.route('/')
def home():
    data = get_posts()
    return render_template("index.html", posts=data)

@app.route("/posts/<slug>")
def get_post(slug: str):
    post = get_specific_post(slug)
    return render_template("post.html", post=post)

if __name__ == "__main__":
    app.run(debug=True)
