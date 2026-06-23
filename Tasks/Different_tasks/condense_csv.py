import csv

def condense_csv(filename: str, id_name: str = 'id_name') -> None:
    with open(filename, encoding='utf-8') as file, open('condensed.csv', 'w', encoding='utf-8') as out_file:
        rdr = csv.reader(file)
        tmp_dict = {}
        for line in rdr:
            tmp_dict.setdefault(line[0], {id_name: line[0]}).update({line[1]: line[2]})
        headers = list(next(iter(tmp_dict.values())).keys())
        wrt = csv.DictWriter(out_file, fieldnames=headers)
        wrt.writeheader()
        wrt.writerows(tmp_dict.values())