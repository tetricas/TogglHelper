from toggle.toggle_day import ToggleDay

TOGGLE_DAY = ToggleDay.MAX_HOURS
RALLY_DAY = 5


def adapt_jira_to_toggle(reported_tasks, jira_tasks):
    days_ready_for_report = list()
    toggle_day = ToggleDay()

    for task in jira_tasks:
        should_continue, task = check_reported_data(reported_tasks, task)
        if should_continue:
            continue

        toggle_day.append_task(task.name, task.hours_done, task.start_at.strftime("%Y-%m-%d"))
        toggle_day = check_full_day(days_ready_for_report, toggle_day)

    return days_ready_for_report


def adapt_rally_to_toggle(reported_tasks, rally_tasks):
    days_ready_for_report = list()
    toggle_day = ToggleDay()

    for task in rally_tasks:
        task.hours_done = task.hours_done / RALLY_DAY * TOGGLE_DAY

        should_continue, task = check_reported_data(reported_tasks, task)
        if should_continue:
            continue

        days_count = int(task.hours_done / TOGGLE_DAY)
        while days_count > 0:
            toggle_day, days_count = fill_day(days_ready_for_report, toggle_day, task.name, TOGGLE_DAY, days_count)

        modulo = round(task.hours_done % TOGGLE_DAY, 1)
        if modulo:
            toggle_day = fill_day(days_ready_for_report, toggle_day, task.name, modulo)

    if toggle_day.day_is_valid():
        days_ready_for_report.append(toggle_day)

    return days_ready_for_report


def check_reported_data(reported_tasks, task):
    if task.name in reported_tasks.keys():
        task.hours_done -= reported_tasks[task.name]
        task.hours_done = round(task.hours_done, 1)

    if task.hours_done <= 0:
        return True, task

    return False, task


def fill_day(days_ready_for_report, toggle_day, name, hours, days_count=None):
    success, hours_left = toggle_day.append_task(name, hours)
    if success:
        if days_count is not None:
            days_count -= 1

        toggle_day = check_full_day(days_ready_for_report, toggle_day)
        if hours_left != 0:
            success, hours_left = toggle_day.append_task(name, hours_left)
            if not success or hours_left != 0:
                raise RuntimeError

    toggle_day = check_full_day(days_ready_for_report, toggle_day)

    if days_count is not None:
        return toggle_day, days_count
    else:
        return toggle_day


def check_full_day(days_ready_for_report, toggle_day):
    if toggle_day.day_is_full():
        days_ready_for_report.append(toggle_day)
        toggle_day = ToggleDay()

    return toggle_day
