#!/usr/bin/python3
''' makes a get request to a REST API '''
import json
import requests
from sys import argv


if __name__ == '__main__':
    url = 'https://jsonplaceholder.typicode.com/'
    user_data = requests.get(url + 'users/{}'.format(argv[1])).json()
    user_tasks = requests.get(url + 'todos', params={'userId': argv[1]}).json()
    with open('{}.json'.format(argv[1]), 'w') as f:
        json.dump({argv[1]: [{
            "task": task.get('title'),
            "completed": task.get('completed'),
            "username": user_data.get('username')
        } for task in user_tasks]}, f)
