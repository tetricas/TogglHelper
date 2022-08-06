from datetime import datetime
from dataclasses import dataclass


@dataclass
class RallyTask:
    name: str
    start_at: datetime
    hours_done: float

    def __init__(self, name: str, start_at: str, hours_done: int):
        self.name = name
        self.start_at = datetime.strptime(start_at, "%Y-%m-%dT%H:%M:%S.%f%z")
        self.hours_done = hours_done / 5 * 8

