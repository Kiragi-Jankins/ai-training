import csv
import datetime

FMT = '%d/%m/%Y %H:%M'

with open('name_log.csv', encoding='utf-8') as log, open('new_name_log.csv', 'w', encoding='utf-8') as new_log:
    rdr = csv.DictReader(log)
    wrt = csv.DictWriter(new_log, fieldnames=rdr.fieldnames)
    tmp_dict = {}
    for line in rdr:
        if line['email'] in tmp_dict:
            tmp_dict[line['email']] = max(line, tmp_dict.get(line['email']), key=lambda x: datetime.datetime.strptime(x['dtime'], FMT))
        else:
            tmp_dict[line['email']] = line
    wrt.writeheader()
    wrt.writerows(sorted(tmp_dict.values(), key=lambda x: x['email']))