import csv

cereal_filename = "cereal_grains.csv"

with open(cereal_filename, encoding='utf-8', newline='') as cereal_file:
    reader = csv.DictReader(cereal_file)
    for row in reader:
        print(row)
