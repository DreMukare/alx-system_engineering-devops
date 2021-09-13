#!/usr/bin/python3
''' makes a get request to a REST API '''
import requests
from sys import argv


if __name__ == '__main__':
    url = 'https://jsonplaceholder.typicode.com/'
    user_data = requests.get(url + 'users/{}'.format(argv[1])).json()
    user_tasks = requests.get(url + 'todos', params={'userId': argv[1]}).json()
    completed_tasks = [task.get('title')
                       for task in user_tasks if task.get('completed') is True]
    print('Employee {} is done with tasks({}/{}):'
          .format(user_data.get('name'),
                  len(completed_tasks), len(user_tasks)))
    [print('\t {}'.format(title)) for title in completed_tasks]
