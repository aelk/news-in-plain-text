import os
import json
from datetime import date

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

def get_articles():
    articles = []
    directory = get_directory('/Users/aelk/news-please-repo/data')
    for filename in os.listdir(directory):
        if filename.endswith('.json'):
            with open(os.path.join(directory, filename), 'r') as f:
                articles.append(json.loads(f.read()))
    return articles

if __name__ == '__main__':
    articles = get_articles()
    print(articles)
