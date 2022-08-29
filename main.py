from rally.rally_data import get_rally_tasks
from toggle import time_entities
from toggle.toggle_sender import ToggleSender
from utils.dates import get_this_month_range


if __name__ == '__main__':
    is_daily = True
    is_english = True
    is_rally = True

    toggle_sender = ToggleSender()
    last_day, was_full, tasks_names = toggle_sender.get_last_tasks_data()
    if was_full:
        last_day += 1

    this_month = list(get_this_month_range(last_day))

    if is_rally:
        rally_tasks = list(get_rally_tasks(this_month[0][0], tasks_names))

    for date, weekday in this_month:
        if weekday in range(0, 4):
            if is_daily:
                toggle_sender.send_time_entity(time_entities.create_daily(date))
            if is_rally:
                task = rally_tasks.pop()
                toggle_sender.send_time_entity(time_entities.create_rally(date, task[0]))
        elif weekday == 4:
            if is_rally:
                task = rally_tasks.pop()
                toggle_sender.send_time_entity(time_entities.create_rally_friday_before(date, task[0]))
                toggle_sender.send_time_entity(time_entities.create_rally_friday_after(date, task[0]))
            if is_english:
                toggle_sender.send_time_entity(time_entities.create_english(date))
        else:
            continue
