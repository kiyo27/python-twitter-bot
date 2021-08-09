import ast
import tweepy
import os
from qiita import Qiita
import secrets_manager

# secret = ast.literal_eval(secrets_manager.get_secret())

# consumer_key = secret['CONSUMER_KEY']
# consumer_secret = secret['CONSUMER_SECRET']
# access_token = secret['ACCESS_TOKEN']
# access_token_secret = secret['ACCESS_TOKEN_SECRET']

consumer_key = os.environ['CONSUMER_KEY']
consumer_secret = os.environ['CONSUMER_SECRET']
access_token = os.environ['ACCESS_TOKEN']
access_token_secret = os.environ['ACCESS_TOKEN_SECRET']

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

# user = os.environ['QIITA_USER']
# qiita = Qiita(secret['QIITA_TOKEN'])
# article = qiita.get_random_article(user)
# tags = '#qiita'
# for t in article['tags']:
#     tags += ' #' + t['name']
# message = article['title']
# message += ' ' + tags + '\n'
# message += article['url']
# print(message)

# api.update_status(message)

# tl = api.user_timeline()
# for tweet in tl:
#     print(tweet.entities['hashtags'])
#     break

# query = 'puggdrasill'
# tl = api.search(query, count=1)
# for tweet in tl:
#     print(tweet)

# search_words = '#qiita from:puggdrasill'
# tweets = tweepy.Cursor(api.search, q=search_words, max_id=-1, result_type='recent').items(20)
# for tweet in tweets:
#     print(tweet.text)

count=1
page=1
tl = api.user_timeline(os.environ['USER'], count=count, page=page)
for tweet in tl:
    print(tweet.retweeted)
    print(tweet.text)
    api.retweet(tweet.id)
    break