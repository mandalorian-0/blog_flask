import requests
from flask import Flask, render_template

from post import Post

def get_data():
    res = requests.get("https://api.npoint.io/c790b4d5cab58020d391")
    res.raise_for_status()
    data = res.json()
    return data

def get_posts():
    posts_objects = []
    posts_data = get_data()

    for post in posts_data:
        post_object = Post(post["title"], post["body"], post["author"])
        posts_objects.append(post_object)

    return posts_objects

def get_specific_post(id_lookup: int):
    all_posts = get_posts()
    searched_post = {}

    for post in all_posts:
        if post["id"] == id_lookup:
            searched_post = post
            break
    return searched_post

app = Flask(__name__)

@app.route('/')
def home():
    data = get_posts()
    return render_template("index.html", posts=data)

@app.route("/posts/<int:post_id>")
def get_post(post_id):
    post = get_specific_post(post_id)
    return render_template("post.html", post=post)

if __name__ == "__main__":
    app.run(debug=True)
