import uuid
import datetime

class Post:
    def __init__(self, title, body, author=None):
        self.id = str(uuid.uuid4())
        self.title = title
        self.author = author
        self.slug = self.title.replace(" ", "-").lower()
        self.body = body
        self.created_at = datetime.datetime.now()
