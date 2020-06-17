import os
import json
import psycopg2
from datetime import date
from flask import Flask
from flask import render_template

app = Flask(__name__)

def get_time(time):
    if time < 10:
        return '0' + str(time)
    else:
        return str(time)

def get_date():
    today = date.today()
    month = get_time(today.month)
    day = get_time(today.day)
    return (str(today.year), month, day)

def get_directory(base_dir):
    year, month, day = get_date()
    return base_dir + '/' + year + '/' + month + '/' + day + '/rt.com/' # TODO: TEMP

def get_articles_from_db():
    conn = psycopg2.connect("dbname=newsDB user=redacted password=redacted")
    cur = conn.cursor()
    cur.execute('SELECT * FROM newsDB')


def get_articles():
    articles = []
    directory = get_directory('/Users/aelk/news-please-repo/data')
    for filename in os.listdir(directory):
        if filename.endswith('.json'):
            with open(os.path.join(directory, filename), 'r') as f:
                articles.append(json.loads(f.read()))
    return articles

@app.route('/')
def print_news():
    articles = get_articles()
    titles = [a['title'] for a in articles]
    return render_template('index.html', titles=titles)

