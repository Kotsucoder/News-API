import requests
import os
import smtplib, ssl

api_key = os.getenv("NEWSAPI")
url = f"https://newsapi.org/v2/everything?q=tesla&from=2024-02-28&\
    sortBy=publishedAt&apiKey={api_key}"

host = "smtp.gmail.com"
port = 465

username = os.getenv("GOOGLE_EMAIL")
password = os.getenv("GOOGLE_PASSWORD")
reciever = os.getenv("PERSONAL_EMAIL")
context = ssl.create_default_context()

request = requests.get(url)
content = request.json()
email = ""
for article in content["articles"]:
    if article["title"] is not None and article["description"] is not None:
        email = email + article["title"] + '\n'
        email = email + article["description"] + '\n'
        email = email + '\n'

with smtplib.SMTP_SSL(host, port, context=context) as server:
    server.login(username, password)
    server.sendmail(username, reciever, email.encode('utf-8'))