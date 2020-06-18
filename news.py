import os
import json
from datetime import date
from flask import Flask, render_template, url_for

app = Flask(__name__)

def get_time(time):
    if time < 10:
        return '0' + str(time)
    else:
        return str(time)

def get_date():
    today = date.today()
    month = get_time(today.month)
    day = str(int(get_time(today.day)) + 1)
    return (str(today.year), month, day)

def get_directory(base_dir):
    year, month, day = get_date()
    return base_dir + '/' + year + '/' + month + '/' + day + '/rt.com/' # TODO: TEMP

def get_articles():
    articles = []
    directory = get_directory('/Users/aelk/news-please-repo/data')
    for filename in os.listdir(directory):
        if filename.endswith('.json'):
            with open(os.path.join(directory, filename), 'r') as f:
                articles.append(json.loads(f.read()))
    return articles

@app.route('/article/<filename>')
def article(filename):
    articles = get_articles()
    for article in articles:
        if article['filename'] == filename:
            return render_template('article.html', article=article)

@app.route('/')
def index():
    articles = get_articles()
    titles = [a['title'] for a in articles]
    return render_template('index.html', articles=get_articles())
