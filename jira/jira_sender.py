from dataclasses import dataclass

import requests
from requests.auth import HTTPBasicAuth
import json

from config import username_work, api_key_jira


@dataclass
class JiraSender:
    headers = {
        "Content-Type": "application/json",
    }
    auth = HTTPBasicAuth(username_work, api_key_jira)

    def get_request(self, url):
        response = requests.request(
            "GET",
            url,
            headers=self.headers,
            auth=self.auth
        )

        if response.text is None:
            raise Exception('Bad response')

        return json.loads(response.text)
