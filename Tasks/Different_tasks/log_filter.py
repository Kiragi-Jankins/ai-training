import csv
import datetime

FMT = '%d/%m/%Y %H:%M'

with open('name_log.csv', encoding='utf-8') as log, open('new_name_log.csv', 'w', encoding='utf-8') as new_log:
    rdr = csv.DictReader(log)
    wrt = csv.DictWriter(new_log, fieldnames=rdr.fieldnames)
    tmp_dict = {}
    for line in rdr:
        cur_dtime = datetime.datetime.strptime(line['dtime'], FMT)
        if line['email'] not in tmp_dict or cur_dtime > tmp_dict[line['email']]['parsed_dtime']:
            tmp_dict[line['email']] = line
            tmp_dict[line['email']]['parsed_dtime'] = cur_dtime
    wrt.writeheader()
    for record in tmp_dict.values():
        del record['parsed_dtime']
    wrt.writerows(sorted(tmp_dict.values(), key=lambda x: x['email']))