import calendar
from datetime import date
import holidays
import config


def get_this_month_range():
    month = date.today().month
    year = date.today().year

    ua_holidays = holidays.country_holidays(config.country)
    for i in range(1, calendar.monthrange(year, month)[1] + 1):
        day = date(year, month, i)
        weekday = day.weekday()
        if weekday in range(0, 5) and day not in ua_holidays:
            yield day.strftime("%Y-%m-%d"), weekday
