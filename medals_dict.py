import csv

medals_table = [
    {'country': 'United States', 'gold': 39, 'silver': 41, 'bronze': 33, 'rank': 1},
    {'country': 'China', 'gold': 38, 'silver': 32, 'bronze': 18, 'rank': 2},
    {'country': 'Japan', 'gold': 27, 'silver': 14, 'bronze': 17, 'rank': 3},
]


def sort_key(d: dict) -> str:
    return d['country']


# columns = ['country', 'gold', 'silver', 'bronze', 'rank']
columns = ['country', 'gold', 'silver', 'bronze']

filename = 'country_medals.csv'

with open(filename, "w", encoding='utf-8', newline='') as output_file:
    # writer = csv.DictWriter(output_file, fieldnames=columns)
    writer = csv.DictWriter(output_file, fieldnames=columns, extrasaction='ignore')
    writer.writeheader()
    # for row in medals_table:
    #     writer.writerow(row)

    writer.writerows(sorted(medals_table, key=sort_key))
