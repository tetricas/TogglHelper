import config
from toggl.TogglPy import Toggl
from toggle import toggle_rest
from dataclasses import dataclass


@dataclass
class ToggleSender:
    toggl = Toggl()

    def __init__(self):
        self.toggl.setAuthCredentials(config.username_toggle, config.password_toggle)

    def send(self, data):
        url = toggle_rest.toggle_host + toggle_rest.toggle_time_entities_route
        self.toggl.postRequest(url, parameters=data)
