import requests
from flask import Flask, render_template

def get_posts():
    res = requests.get("https://api.npoint.io/c790b4d5cab58020d391")
    res.raise_for_status()
    data = res.json()
    return data

app = Flask(__name__)

@app.route('/')
def home():
    data = get_posts()
    return render_template("index.html", posts=data)

@app.route("/posts/<int:id>")
def get_post():
    return render_template("post.html")

if __name__ == "__main__":
    app.run(debug=True)
