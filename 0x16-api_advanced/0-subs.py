#!/usr/bin/python3
'''queries the reddit API and returns total subs for a subreddit'''
import requests


def number_of_subscribers(subreddit):
    '''returns number of subscribers or 0 if subreddit is invalid'''
    if subreddit is None or not isinstance(subreddit, str):
        return 0
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    res = requests.get(url, headers={'User-Agent': 'DreMukare'}).json()
    sub_count = 0
    if 'error' not in res.keys():
        sub_count = res.get('data').get('subscribers')
    return sub_count
