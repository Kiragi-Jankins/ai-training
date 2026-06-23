import calendar
import datetime

def get_days_in_month(year: int, month: str) -> list[datetime.date]:
    month_idx = next(i for i, name in enumerate(calendar.month_name) if name == month)
    nums_days = calendar.monthrange(year, month_idx)[1]
    return [datetime.date(year, month_idx, i) for i in range(1, nums_days + 1)]