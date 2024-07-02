from dataclasses import dataclass
from toggle.time_entities import daily_name, english_name


@dataclass
class ToggleTask:
    name: str
    time: int

    def __init__(self, name, time):
        self.name = name
        self.time = time


@dataclass
class ToggleDay:
    MAX_HOURS = 8
    total_hours: int
    tasks: list
    date: None

    def __init__(self):
        self.total_hours = 0
        self.date = None
        self.tasks = list()

    def day_is_full(self):
        if self.total_hours > self.MAX_HOURS:
            raise RuntimeError

        return self.total_hours == self.MAX_HOURS

    def day_is_valid(self):
        return self.total_hours > 0

    def append_task(self, name, time, date=None):
        self.date = date

        if self.day_is_full():
            return False, 0

        if time + self.total_hours <= self.MAX_HOURS:
            self.tasks.append(ToggleTask(name, time))
            self.total_hours += time
            return True, 0
        else:
            time_left = round(time + self.total_hours - self.MAX_HOURS, 1)
            time_to_fill = round(time - time_left, 1)
            self.tasks.append(ToggleTask(name, time_to_fill))
            self.total_hours += time_to_fill
            return True, time_left

    def generate_report(self):
        if len(self.tasks) < 1:
            raise RuntimeError

        self.tasks.insert(0, ToggleTask(daily_name, 0.5))
        self.tasks[1].time -= 0.5  # 30 min for the Daily

        return self.tasks
