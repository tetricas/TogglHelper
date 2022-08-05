import requests
from toggl.TogglPy import Toggl

import config
from rally import rally_rest
from toggle import time_entities, toggle_rest
from utils.dates import get_this_month


def create_new_time_entities(is_daily, is_english):
    toggl = Toggl()
    toggl.setAuthCredentials(config.username_toggle, config.password_toggle)

    for date, weekday in get_this_month():
        if weekday in range(0, 4) and is_daily:
            functor = time_entities.create_daily
        elif weekday == 4 and is_english:
            functor = time_entities.create_english
        else:
            raise Exception("Wrong weekday")

        data = functor(date)
        url = toggle_rest.toggle_host + toggle_rest.toggle_time_entities_route
        toggl.postRequest(url, parameters=data)


def query_rally_tasks():
    query = f'((CreatedBy = {config.username_rally}) AND \
                ((LastUpdateDate >= 2022-06-01) AND (LastUpdateDate <= today)))'
    query = '?query=' + query

    url = rally_rest.host + rally_rest.rally_artifacts_route + query
    return requests.get(url, headers={'ZSESSIONID': config.api_key_rally})


if __name__ == '__main__':
    is_daily = False
    is_english = False
    is_rally = False

    create_new_time_entities(is_daily, is_english)
    if is_rally:
        response = query_rally_tasks()
        print(response.text)
