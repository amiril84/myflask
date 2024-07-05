from flask import Flask, render_template, jsonify
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

@app.route('/')
def index():
  return render_template('index.html')

@app.route('/hello')
def hello():
    return jsonify({"hello world": "amiril"})


if __name__ == '__main__':
  app.run(port=5000)
