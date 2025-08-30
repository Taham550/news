from flask import Flask, render_template
import requests
import os
from dotenv import load_dotenv



app = Flask(__name__)
load_dotenv()  # Load variables from .env
# Load NEWS_API_KEY from environment variable
NEWS_API_KEY = os.environ.get('NEWS_API_KEY')
if not NEWS_API_KEY:
    raise ValueError("NEWS_API_KEY environment variable not set")



@app.route('/')
def home():
    url = 'https://newsapi.org/v2/everything'
    params = {
    'q': 'stocks',
    'language': 'en',
    'sortBy': 'publishedAt',
    'apiKey': NEWS_API_KEY
   }


    response = requests.get(url, params=params)
    articles = response.json().get('articles', [])
    return render_template('index.html', articles=articles)

if __name__ == '__main__':
    app.run(debug=True)
