from rally.rally_data import query_rally_tasks
from toggle import time_entities, toggle_sender
from utils.dates import get_this_month_range


if __name__ == '__main__':
    is_daily = False
    is_english = False
    is_rally = True

    this_month = list(get_this_month_range())
    if is_rally:
        tasks = list(query_rally_tasks(this_month[0][0]))
        tasks.sort(key=lambda el: el.start_at)
        print(tasks)

    toggle_sender = toggle_sender.ToggleSender()

    for date, weekday in this_month:
        if weekday in range(0, 4) and is_daily:
            toggle_sender.send(time_entities.create_daily(date))
        elif weekday == 4 and is_english:
            toggle_sender.send(time_entities.create_english(date))
        else:
            continue
