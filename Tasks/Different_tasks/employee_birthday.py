from datetime import datetime as dt, date, timedelta

FMT = '%d.%m.%Y'

def incoming_parser(s):
    s = s.split()
    return [' '.join(s[:2]), dt.strptime(s[2], FMT).date()]

cur_date = dt.strptime(input(), FMT).date()
n = int(input())
youngest_employee = [None, date.min]

for _ in range(n):
    employee, emp_birthday = incoming_parser(input())
    tmp_date = emp_birthday.replace(year=cur_date.year)
    if tmp_date < cur_date:
        tmp_date = tmp_date.replace(year=tmp_date.year + 1)
    if cur_date < tmp_date <= cur_date + timedelta(days=7):
        youngest_employee = max(youngest_employee, [employee, emp_birthday], key=lambda x: x[1])

print(youngest_employee[0] if youngest_employee[0] else 'Дни рождения не планируются')