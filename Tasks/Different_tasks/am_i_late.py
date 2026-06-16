from datetime import datetime as dt, time

FMT = '%d.%m.%Y %H:%M'
work_time = {0: {'start': time(9, 0), 'end': time(21, 0)}, 
             1: {'start': time(10, 0), 'end': time(18, 0)}}

def am_i_late(s_time):
    cur_time = dt.strptime(s_time, FMT)
    is_weekend = cur_time.weekday() // 5
    start_time = work_time[is_weekend]['start']
    end_time = work_time[is_weekend]['end']
    if start_time <= cur_time.time() < end_time:
        return (end_time.hour * 60 + end_time.minute) - (cur_time.hour * 60 + cur_time.minute)
    else:
        return 'Магазин не работает'

print(am_i_late(input()))