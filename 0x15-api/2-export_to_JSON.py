#!/usr/bin/python3
''' makes a get request to a REST API '''
import json
import requests
from sys import argv


if __name__ == '__main__':
    url = 'https://jsonplaceholder.typicode.com/'
    user_data = requests.get(url + 'users/{}'.format(argv[1])).json()
    user_tasks = requests.get(url + 'todos', params={'userId': argv[1]}).json()
    file_dict = {str(argv[1]): []}
    out_dict = {}
    with open('{}.json'.format(argv[1]), 'w') as f:
        for task in user_tasks:
            out_dict['task'] = task.get('title')
            out_dict['completed'] = task.get('completed')
            out_dict['username'] = user_data.get('username')
            file_dict[str(argv[1])].append(out_dict)
        json.dump(file_dict, f)
