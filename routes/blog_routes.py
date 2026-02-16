from flask import Blueprint, render_template
from services.post_service import get_posts, get_specific_post

blog_bp = Blueprint('blog', __name__)


@blog_bp.route('/blog')
def home():
    data = get_posts()
    return render_template("index.html", posts=data)


@blog_bp.route("/blog/posts/<slug>")
def get_post(slug: str):
    post = get_specific_post(slug)

    if not post:
        return "Post not found", 404

    return render_template("post.html", post=post)
