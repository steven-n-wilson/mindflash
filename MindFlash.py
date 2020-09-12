from flask import Flask, render_template
import requests, sys, json

# news_request = "https://www.example.com"

# try:
#     news_content = requests.get(news_request).text
# except:
#     print(f"unable to get {news_request}")
#     sys.exit(1)

app = Flask(__name__)

# news_cards = json.loads(news_content)

# MYSQL Handlers
# db = MYSQL database

@app.route("/", methods=["GET", "POST", "DELETE"]) # main page
def home():
    return render_template(
    "home.html",
    # news_cards = news
    )

if __name__ == "__main__":
    app.run(debug=True)