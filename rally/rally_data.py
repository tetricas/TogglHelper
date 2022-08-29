import requests
import config
import json
from rally import rally_rest, rally_task


def get_rally_tasks(start_day, reported_tasks_names):
    tasks = list(query_rally_tasks(start_day))
    tasks.sort(key=lambda el: el.start_at, reverse=True)
    for task in tasks:
        if task.name in reported_tasks_names.keys():
            task.hours_done -= reported_tasks_names[task.name]

        days_count = int(task.hours_done / 8)
        while days_count > 0:
            yield task.name, 8
            days_count -= 1

        modulo = task.hours_done % 8
        if modulo and modulo > 1:  # English lesson
            yield task.name, modulo


def query_rally_tasks(start_date):
    query = f'((Owner = {config.username_rally}) AND \
                ((LastUpdateDate >= {start_date}) AND (LastUpdateDate <= today)))'
    query = '?query=' + query

    url = rally_rest.host + rally_rest.rally_artifacts_route + query
    response = requests.get(url, headers={'ZSESSIONID': config.api_key_rally})
    query_result = json.loads(response.text)['QueryResult']
    results = query_result['Results']
    for result in results:
        if result['_type'] == "Task":
            yield read_rally_task(result['_refObjectUUID'])


def read_rally_task(object_id):
    url = rally_rest.host + rally_rest.rally_task_route + '/' + object_id
    response = requests.get(url, headers={'ZSESSIONID': config.api_key_rally})
    task_result = json.loads(response.text)['Task']
    return rally_task.RallyTask(task_result['_refObjectName'], task_result['WorkProduct']['_refObjectName'],
                                task_result['LastUpdateDate'], task_result['Estimate'] - task_result['ToDo'])
