from flask import Flask, render_template, jsonify
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

@app.route('/')
def index():
  return render_template('index.html')

@app.route('/test', methods=['GET'])
def test():
    test_url = "https://almanhaj.or.id/84056-jenis-jenis-ibadah-haji.html"
    num_words = 100
    scraped_text = check_and_scrape(test_url, num_words)
    return jsonify({"scraped_text": scraped_text})

@app.route('/hello')
def hello():
    return jsonify({"hello world": "amiril"})

#Function to check URL and scrape content
def check_and_scrape(url, num_words):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')
            text = ' '.join(soup.get_text(separator=' ', strip=True).split()[:num_words])
            return text
    except requests.RequestException as e:
        return f"Error accessing {url}: {e}"


if __name__ == '__main__':
  app.run(port=5000)
