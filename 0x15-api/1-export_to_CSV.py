#!/usr/bin/python3
''' makes a get request to a REST API '''
import requests
from sys import argv


if __name__ == '__main__':
    url = 'https://jsonplaceholder.typicode.com/'
    user_data = requests.get(url + 'users/{}'.format(argv[1])).json()
    user_tasks = requests.get(url + 'todos', params={'userId': argv[1]}).json()
    with open('{}.csv'.format(argv[1]), 'w') as f:
        for task in user_tasks:
            line = '"{}","{}","{}","{}"\n'.format(
                task.get('userId'),
                user_data.get('username'),
                task.get('completed'),
                task.get('title'))
            f.write(line)
