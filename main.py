import requests
import os

api_key = os.getenv("NEWSAPI")
url = f"https://newsapi.org/v2/everything?q=tesla&from=2024-02-28&\
    sortBy=publishedAt&apiKey={api_key}"

request = requests.get(url)
content = request.json()
for article in content["articles"]:
    print(article["title"])
    print(article["description"])