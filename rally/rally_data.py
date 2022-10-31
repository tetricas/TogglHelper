import requests
import config
import json
from rally import rally_rest
from utils import outside_task


def get_rally_tasks(start_day):
    tasks = list(query_rally_tasks(start_day))
    tasks.sort(key=lambda el: el.start_at, reverse=True)
    return tasks


def query_rally_tasks(start_date):
    query = f'((Owner = {config.username_work}) AND \
                ((LastUpdateDate >= {start_date}) AND (LastUpdateDate <= today)))'
    query = '?query=' + query

    url = rally_rest.host + rally_rest.artifacts_route + query
    response = requests.get(url, headers={'ZSESSIONID': config.api_key_rally})
    query_result = json.loads(response.text)['QueryResult']
    results = query_result['Results']
    for result in results:
        if result['_type'] == "Task":
            yield read_rally_task(result['_refObjectUUID'])


def read_rally_task(object_id):
    url = rally_rest.host + rally_rest.task_route + '/' + object_id
    response = requests.get(url, headers={'ZSESSIONID': config.api_key_rally})
    task_result = json.loads(response.text)['Task']
    return outside_task.OutsideTask(task_result['_refObjectName'], task_result['LastUpdateDate'],
                                    task_result['Estimate'] - task_result['ToDo'], task_result['WorkProduct']['_refObjectName'])
