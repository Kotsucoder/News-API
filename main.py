import requests
import os
import smtplib, ssl

topic = "apple computer"
api_key = os.getenv("NEWSAPI")
url = f"https://newsapi.org/v2/everything?" \
    f"q={topic}&" \
    f"sortBy=publishedAt&" \
    f"apiKey={api_key}&" \
    f"language=en"

host = "smtp.gmail.com"
port = 465

username = os.getenv("GOOGLE_EMAIL")
password = os.getenv("GOOGLE_PASSWORD")
reciever = os.getenv("PERSONAL_EMAIL")
context = ssl.create_default_context()

request = requests.get(url)
content = request.json()
email = "Subject: Today's news\n"
for article in content["articles"][:20]:
    if article["title"] is not None and article["description"] is not None:
        email = email + article["title"] + '\n'
        email = email + article["description"] + '\n'
        email = email + article["url"] + '\n'
        email = email + '\n'

with smtplib.SMTP_SSL(host, port, context=context) as server:
    server.login(username, password)
    server.sendmail(username, reciever, email.encode('utf-8'))