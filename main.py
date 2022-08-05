import requests
from toggl.TogglPy import Toggl

import config
from rally import rally_rest
from toggle import time_entities, toggle_rest


def create_new_time_entity(days, functor):
    toggl = Toggl()
    toggl.setAuthCredentials(config.username_toggle, config.password_toggle)

    for day in days:
        if day < 10:
            day = "0" + str(day)

        data = functor(day)
        url = toggle_rest.toggle_host + toggle_rest.toggle_time_entities_route
        toggl.postRequest(url, parameters=data)


def query_rally_tasks():
    query = f'((CreatedBy = {config.username_rally}) AND \
                ((LastUpdateDate >= 2022-06-01) AND (LastUpdateDate <= today)))'
    query = '?query=' + query

    url = rally_rest.host + rally_rest.rally_artifacts_route + query
    return requests.get(url, headers={'ZSESSIONID': config.api_key_rally})


if __name__ == '__main__':
    daily = False
    english = False
    rally = False

    if daily:
        create_new_time_entity(range(23, 24), time_entities.create_daily)
    if english:
        create_new_time_entity([1], time_entities.create_english)
    if rally:
        response = query_rally_tasks()
        print(response.text)
