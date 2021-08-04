import urllib.request
import json
import os
import random

API = 'https://qiita.com/api/v2'

def send_request(url):
    req = urllib.request.Request(url)
    req.headers = {
        'Authorization': 'Bearer ' + os.environ['TOKEN']
    }
    with urllib.request.urlopen(req) as response:
        return json.loads(response.read().decode('utf-8'))

def get_article_ids(user, page=1, per_page=20):
    url = f'{API}/users/{user}/items?page={page}&per_page={per_page}'
    decode = send_request(url)
    ids = []
    for s in range(len(decode)):
        ids.append(decode[s]['id'])
    return ids

def get_article(id):
    url =  f'{API}/items/{id}'
    decode = send_request(url)
    return decode

def get_random_article(user):
    ids = get_article_ids(user)
    l = len(ids)
    i = random.randint(0, l - 1)
    article = get_article(ids[i])
    return article

if __name__ == "__main__":
    get_random_article()