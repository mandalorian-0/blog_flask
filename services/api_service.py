import requests
from config import API_URL


def fetch_data():
    res = requests.get(API_URL)
    res.raise_for_status()
    data = res.json()
    return data
