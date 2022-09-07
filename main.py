from datetime import datetime, timedelta

from rally.rally_data import get_rally_tasks

from toggle.time_entities import create_time_entity, beginning_of_the_day
from toggle.toggle_sender import ToggleSender

from utils.dates import get_this_month_range
from utils.tasks_bridge import adapt_rally_to_toggle

if __name__ == '__main__':

    toggle_sender = ToggleSender()
    last_day, was_full, reported_tasks = toggle_sender.get_last_tasks_data()
    if was_full:
        last_day += timedelta(days=1)

    this_month = list(get_this_month_range(last_day.day))

    rally_tasks = get_rally_tasks(this_month[0][0])
    days_to_report = adapt_rally_to_toggle(reported_tasks, rally_tasks)

    for date, weekday in this_month:
        is_friday = weekday == 4
        day = days_to_report.pop(0)
        report_data = day.generate_report(is_friday)

        current_time = datetime.strptime(beginning_of_the_day, '%H:%M')
        for task in report_data:
            time = current_time.strftime('%H:%M')
            time_entity = create_time_entity(task.name, date, time, task.time)
            toggle_sender.send_time_entity(time_entity)
            current_time += timedelta(hours=task.time)
