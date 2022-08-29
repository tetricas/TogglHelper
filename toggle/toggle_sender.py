import datetime
from base64 import b64encode
from json import JSONDecodeError

import requests

import config
from toggle import toggle_rest
from dataclasses import dataclass


@dataclass
class ToggleSender:
    headers = {
        "Authorization": "",
        "Content-Type": "application/json",
        "Accept": "*/*",
        "User-Agent": "python/urllib",
    }

    def __init__(self):
        authHeader = '{0}:{1}'.format(config.username_toggle, config.password_toggle)
        authHeader = "Basic " + b64encode(authHeader.encode()).decode('ascii').rstrip()

        # add it into the header
        self.headers['Authorization'] = authHeader

    def request(self, url, method, parameters=None):
        try:
            response = None
            if method == 'GET':
                response = requests.get(url, json=parameters, headers=self.headers)
            elif method == 'POST':
                response = requests.post(url, json=parameters, headers=self.headers)

            if response:
                return response.json()
        except JSONDecodeError as e:
            print(e)

    def send_time_entity(self, parameters):
        url = toggle_rest.host + toggle_rest.workspaces_route + toggle_rest.time_entities_route
        self.request(url, parameters=parameters, method='POST')

    def get_last_tasks_data(self):
        url = toggle_rest.host + toggle_rest.me_route + toggle_rest.time_entities_route
        data = self.request(url, method='GET')
        last_date = data[0]['stop']
        last_date = datetime.datetime.strptime(last_date, "%Y-%m-%dT%H:%M:%SZ").date()
        day_hours = 0
        tasks_names = dict()
        for task in data:
            current = datetime.datetime.strptime(task['stop'], "%Y-%m-%dT%H:%M:%SZ").date()
            if current == last_date:
                day_hours += task['duration']

            task_name = task['description']
            if task_name != 'Daily meeting' and task_name != 'Lesson':
                duration = int(task['duration'] / 3600 + 0.5)

                if task_name not in tasks_names.keys():
                    tasks_names[task_name] = duration
                else:
                    tasks_names[task_name] += duration

        hour = 3600

        return last_date.day, day_hours == hour * 8, tasks_names
