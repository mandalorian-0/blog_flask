import markdown
import requests
from flask import Flask, render_template

from post import Post

cached_posts = None

def fetch_data():
    res = requests.get("https://api.npoint.io/f988fe2f89471cfb558e")
    res.raise_for_status()
    data = res.json()
    return data

def get_posts():
    global cached_posts
    if cached_posts is not None:
        return cached_posts

    try:
        posts_objects = []
        posts_data = fetch_data()

        for post in posts_data:
            body_to_html = markdown.markdown(post["body"])
            post_object = Post(post["title"], body_to_html, post["description"], post["author"])
            posts_objects.append(post_object)

        cached_posts = posts_objects
        return cached_posts
    except requests.exceptions.RequestException as e:
        print(f"Error fetching blog posts: {e}")
        return []
    except Exception as e:
        print(f"Error processing posts: {e}")
        return []

def get_specific_post(post_slug: str):
    posts = get_posts()
    post = next((post for post in posts if post.slug == post_slug), None)

    return post

app = Flask(__name__)

@app.route('/blog')
def home():
    data = get_posts()
    return render_template("index.html", posts=data)

@app.route("/blog/posts/<slug>")
def get_post(slug: str):
    post = get_specific_post(slug)

    if not post:
        return "Post not found", 404

    return render_template("post.html", post=post)

if __name__ == "__main__":
    app.run(debug=True)
