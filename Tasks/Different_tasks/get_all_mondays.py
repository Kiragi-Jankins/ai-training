import calendar
import datetime

def get_all_mondays(year: int) -> list[datetime.date]:
    result = []
    for month_idx in range(1, 13):
        for week in calendar.monthcalendar(year, month_idx):
            monday_day = week[0]
            if monday_day != 0:
                result.append(datetime.date(year, month_idx, monday_day))
    return result