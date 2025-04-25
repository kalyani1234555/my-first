import csv

csv_filename = 'olympicMedals_2020.csv'

with open(csv_filename, encoding='utf-8', newline='') as csv_file:
    headers = csv_file.readline().strip('\n\r').split(',')
    print(f'column headers: {headers}')
    reader = csv.reader(csv_file)
    for row in reader:
        rank, country, gold, silver, bronze, total = row
        rank1, gold1, silver1, bronze1, total1 = int(rank), int(gold), int(silver), int(bronze), int(total)
        print(row)
        print([rank1, country, gold1, silver1, bronze1, total1])

# print(reader)
