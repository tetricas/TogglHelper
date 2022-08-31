from datetime import datetime
from dataclasses import dataclass


@dataclass
class RallyTask:
    name: str
    start_at: datetime
    hours_done: float
    minutes_done: int

    def __init__(self, name: str, user_story: str, start_at: str, hours_done: int):
        user_story = user_story.replace('[Continued] ', '').replace('[Continued]', '') \
                               .replace('[Unfinished] ', '').replace('[Unfinished]', '')
        self.name = user_story + ': ' + name
        self.start_at = datetime.strptime(start_at, "%Y-%m-%dT%H:%M:%S.%f%z")
        self.hours_done = hours_done

