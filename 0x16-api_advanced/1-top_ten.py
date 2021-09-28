#!/usr/bin/python3
'''queries the reddit API and returns top ten hot posts in a subreddit'''
import requests


def top_ten(subreddit):
    '''returns number of subscribers or 0 if subreddit is invalid'''
    if subreddit is None or not isinstance(subreddit, str):
        print(None)
        return
    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    res = requests.get(url, headers={'User-Agent': 'DreMukare'}).json()
    if 'error' in res.keys():
        print(None)
        return
    all_posts = res.get('data').get('children')
    i = 0
    while i < 10:
        print(all_posts[i].get('data').get('title'))
        i += 1
