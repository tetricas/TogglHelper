from toggl.TogglPy import Toggl

import config
import time_entities


def createNewTimeEntity(days, functor):
    for day in days:
        if day < 10:
            day = "0" + str(day)

        data = functor(day)
        toggl.postRequest("https://api.track.toggl.com/api/v8/time_entries", parameters=data)


if __name__ == '__main__':
    toggl = Toggl()
    toggl.setAuthCredentials(config.username, config.password)

    createNewTimeEntity(range(23, 24), time_entities.createDaily)
