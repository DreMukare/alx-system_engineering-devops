#!/usr/bin/python3
'''
queries the reddit API using recursion
returns a list of all hot articles in a subreddit
'''
import requests


def recurse(subreddit, hot_list=[], after=None):
    """returns a list of all hot post titles for a given subreddit"""
    if subreddit is None or not isinstance(subreddit, str):
        return None
    url = 'http://www.reddit.com/r/{}/hot.json'.format(subreddit)
    r = requests.get(
        url,
        headers={
            'User-Agent': 'DreMukare'},
        params={
            'after': after}).json()
    after = r.get('data', {}).get('after', None)
    posts = r.get('data', {}).get('children', None)
    if posts is None or (len(posts) > 0 and posts[0].get('kind') != 't3'):
        if len(hot_list) == 0:
            return None
        return hot_list
    else:
        for post in posts:
            hot_list.append(post.get('data', {}).get('title', None))
    if after is None:
        if len(hot_list) == 0:
            return None
        return hot_list
    else:
        return recurse(subreddit, hot_list, after)
