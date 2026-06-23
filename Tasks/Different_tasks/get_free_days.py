import calendar
import datetime

def get_free_days(year: int) -> list[datetime.date]:
    result = []
    for month_idx in range(1, 13):
        for week in calendar.monthcalendar(year, month_idx):
            free_day = week[3]
            if 15 <= free_day <= 21:
                result.append(datetime.date(year, month_idx, free_day))
    return result

for data in get_free_days(int(input())):
    print(data.strftime('%d.%m.%Y'))