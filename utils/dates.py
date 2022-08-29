import calendar
from datetime import date
import holidays
import config


def get_this_month_range(day_from):
    month = date.today().month
    year = date.today().year
    current_day = date.today().day

    ua_holidays = holidays.country_holidays(config.country)
    work_week = range(0, 5)
    last_day = calendar.monthrange(year, month)[1]
    last_day = current_day if last_day > current_day else last_day

    for i in range(day_from, last_day + 1):
        day = date(year, month, i)
        weekday = day.weekday()
        if weekday in work_week and day not in ua_holidays and i not in config.vacation:
            yield day.strftime("%Y-%m-%d"), weekday
