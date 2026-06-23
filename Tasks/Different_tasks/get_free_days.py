import calendar
import datetime

def get_free_days(year: int) -> None:
    for month_idx in range(1, 13):
        for week in calendar.monthcalendar(year, month_idx):
            free_day = week[3]
            if 15 <= free_day <= 21:
                print(datetime.date(year, month_idx, free_day).strftime('%d.%m.%Y'))