import csv

def sort_tuple(cls: str):
    num, letter = cls.split('-')
    return (int(num), letter)

with open('student_counts.csv', encoding='utf-8') as file:
    rdr = csv.DictReader(file)
    with open('sorted_student_counts.csv', 'w', encoding='utf-8') as out_file:
        headers = sorted(filter(lambda x: x != 'year', rdr.fieldnames), key=sort_tuple)
        headers.insert(0, 'year')
        wrt = csv.DictWriter(out_file, fieldnames=headers)
        wrt.writeheader()
        wrt.writerows(rdr)