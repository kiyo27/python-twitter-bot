import urllib.request
import json
import os
import random

API = 'https://qiita.com/api/v2'

class Qiita:
    def __init__(self, token):
        self.token = token

    def send_request(self, url):
        req = urllib.request.Request(url)
        req.headers = {
            'Authorization': 'Bearer ' + self.token
        }
        with urllib.request.urlopen(req) as response:
            return json.loads(response.read().decode('utf-8'))

    def get_article_ids(self, user, page=1, per_page=20):
        url = f'{API}/users/{user}/items?page={page}&per_page={per_page}'
        decode = self.send_request(url)
        ids = []
        for s in range(len(decode)):
            ids.append(decode[s]['id'])
        return ids

    def get_article(self, id):
        url =  f'{API}/items/{id}'
        decode = self.send_request(url)
        return decode

    def get_random_article(self, user):
        ids = self.get_article_ids(user)
        l = len(ids)
        i = random.randint(0, l - 1)
        article = self.get_article(ids[i])
        return article

def main(token):
    qiita = Qiita(token)
    article = qiita.get_article('3db780252adcfd563a5f')
    print(article)

if __name__ == "__main__":
    import ast
    from secrets_manager import get_secret
    secret = ast.literal_eval(get_secret())
    main(secret['QIITA_TOKEN'])
