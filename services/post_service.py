import markdown
import requests
from datetime import datetime
from services.api_service import fetch_data

cached_posts = None


def get_posts():
    global cached_posts
    if cached_posts is not None:
        return cached_posts

    try:
        posts_objects = []
        posts_data = fetch_data()

        for post in posts_data:
            post["body"] = markdown.markdown(post["body"])

            date_to_dt_obj = datetime.strptime(post["created_at"], "%Y-%m-%dT%H:%M:%S.%f")
            post["created_at"] = date_to_dt_obj.strftime("%A %d, %Y")
            
            posts_objects.append(post)

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
    post = next((post for post in posts if post['slug'] == post_slug), None)

    return post
