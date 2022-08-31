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

    def __init__(self):
        self.total_hours = 0
        self.tasks = list()

    def day_is_full(self):
        return self.total_hours == self.MAX_HOURS

    def append_task(self, name, time):
        if self.day_is_full():
            return False, 0

        if time + self.total_hours <= self.MAX_HOURS:
            self.tasks.append(ToggleTask(name, time))
            self.total_hours += time
            return True, 0
        else:
            time_left = time + self.total_hours - self.MAX_HOURS
            self.tasks.append(ToggleTask(name, time - time_left))
            return True, time_left

    def generate_report(self, is_friday):
        if len(self.tasks) < 1:
            raise RuntimeError

        if is_friday:
            HOURS_BEFORE_ENGLISH = 4.5
            if len(self.tasks) > 1:
                time_before_english = 0
                index = 0
                while time_before_english < HOURS_BEFORE_ENGLISH:
                    if time_before_english + self.tasks[index].time > HOURS_BEFORE_ENGLISH:
                        time_after = self.tasks[index].time - (HOURS_BEFORE_ENGLISH - time_before_english)
                        self.tasks[index].time -= time_after
                        name = self.tasks[index].name
                        self.tasks.insert(++index, ToggleTask(english_name, 1))
                        self.tasks.insert(++index, ToggleTask(name, time_after - 1))
                        break
                    elif time_before_english + self.tasks[index].time == HOURS_BEFORE_ENGLISH:
                        self.tasks.insert(++index, ToggleTask(english_name, 1))
                        self.tasks[++index].time -= 1

                    time_before_english += self.tasks[index].time
                    index += 1
            else:
                self.tasks[0] = ToggleTask(self.tasks[0].name, HOURS_BEFORE_ENGLISH)
                self.tasks.append(ToggleTask(english_name, 1))
                self.tasks.append(ToggleTask(self.tasks[0].name, 3))
        else:
            self.tasks.insert(0, ToggleTask(daily_name, 0.25))
            self.tasks[1].time -= 0.25  # 15 min for the Daily

        return self.tasks
