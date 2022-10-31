from datetime import datetime
from dataclasses import dataclass


@dataclass
class OutsideTask:
    name: str
    start_at: datetime
    hours_done: float

    def __init__(self, name: str, start_at: str, hours_done: int, user_story=''):
        if user_story != '':
            user_story = user_story.replace('[Continued] ', '').replace('[Continued]', '') \
                                   .replace('[Unfinished] ', '').replace('[Unfinished]', '')
            self.name = user_story + ': ' + name
        else:
            self.name = name
        self.start_at = datetime.strptime(start_at, "%Y-%m-%dT%H:%M:%S.%f%z")
        self.hours_done = hours_done

