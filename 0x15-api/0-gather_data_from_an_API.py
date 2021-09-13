#!/usr/bin/python3
''' makes a get request to a REST API '''
import requests
import json
from sys import argv


if __name__ == '__main__':
    url = 'https://jsonplaceholder.typicode.com/'
    user_data = requests.get(url + 'users/{}'.format(argv[1])).json()
    user_tasks = requests.get(url + 'todos', params={'userId': argv[1]}).json()
    completed_tasks = []
    for task in user_tasks:
        if task.get('completed'):
            completed_tasks.append(task)
    user_name = user_data.get('name')
    print('Employee {} is done with tasks({}/{}):'.format(user_name,
          len(completed_tasks), len(user_tasks)))
    for task in completed_tasks:
        print('\t {}'.format(task.get('title')))
