from datetime import datetime as dt, time, date, timedelta

FMT = '%d.%m.%Y %H:%M'

def choose_plural(amount, declensions):
    x = amount % 10
    if x in range(5, 10) or x == 0 or (11 <= amount % 100 <= 14):
        return_index = 2
    elif x in range(2, 5):
        return_index = 1
    elif x == 1:
        return_index = 0
    return f'{declensions[return_index]}'

days = ['день', 'дня', 'дней']
hours = ['час', 'часа', 'часов']
minutes = ['минута', 'минуты', 'минут']

pub_date = dt.strptime('08.11.2022 12:00', FMT)
cur_date = dt.strptime(input(), FMT)
template_1 = 'До выхода курса осталось: '

if cur_date >= pub_date:
    print('Курс уже вышел!')
else:
    delta = pub_date - cur_date
    d_d = delta.days
    d_h = delta.seconds // 3600
    d_m = (delta.seconds % 3600) // 60
    if d_d:
        if d_h: # проверяем есть ли в delta хотя бы 1 час
            print(f'{template_1}{d_d} {choose_plural(d_d, days)} и {d_h} {choose_plural(d_h, hours)}')
        else:
            print(f'{template_1}{d_d} {choose_plural(d_d, days)}')
    else:
        if d_h and d_m: # проверяем есть ли хотя бы 1 минута (после конвертации в часы)
            print(f'{template_1}{d_h} {choose_plural(d_h, hours)} и {d_m} {choose_plural(d_m, minutes)}')
        elif d_m:
            print(f'{template_1}{d_m} {choose_plural(d_m, minutes)}')
        else:
            print(f'{template_1}{d_h} {choose_plural(d_h, hours)}')