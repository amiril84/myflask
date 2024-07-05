from flask import Flask, render_template, jsonify
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

def check_and_scrape(url, num_words):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')
            text = ' '.join(soup.get_text(separator=' ', strip=True).split()[:num_words])
            return text
    except requests.RequestException as e:
        return f"Error accessing {url}: {e}"

@app.route('/')
def index():
  return render_template('index.html')

@app.route('/hello')
def hello():
    return jsonify({"hello world": "amiril"})

@app.route('/coba')
def coba():
    test_url = "https://almanhaj.or.id/84056-jenis-jenis-ibadah-haji.html"
    num_words = 100
    scraped_text = check_and_scrape(test_url, num_words)
    return jsonify({"scraped_text": scraped_text})
    

@app.route('/scrape')
def scrape():
    url = request.args.get('url')
    num_words = int(request.args.get('num_words'))
    if not url:
        return jsonify({"error": "URL parameter is required"}), 400
    scraped_text = check_and_scrape(url, num_words)
    return jsonify({"scraped_text": scraped_text})

if __name__ == '__main__':
  app.run(port=5000)
