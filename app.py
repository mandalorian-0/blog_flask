from flask import Flask
from routes.blog_routes import blog_bp

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
app.register_blueprint(blog_bp)

if __name__ == "__main__":
    app.run(debug=True)
