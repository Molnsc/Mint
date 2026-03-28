from flask import Flask, request, jsonify
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

@app.route("/")
def home():
    return "Scraper API running"

@app.route("/scrape")
def scrape():
    url = request.args.get("url")
    
    if not url:
        return jsonify({"error": "Missing URL"}), 400

    headers = {"User-Agent": "Mozilla/5.0"}
    res = requests.get(url, headers=headers)

    soup = BeautifulSoup(res.text, "html.parser")

    return jsonify({
        "title": soup.title.string if soup.title else None,
        "links": [a.get("href") for a in soup.find_all("a")]
    })
