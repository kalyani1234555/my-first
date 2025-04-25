import csv

cereals = [
    ["Barley", 556, 1.7, 32.9, 10.1, 13.8],
    ["Durum", 339, 5, 27.4, 4.09, 9.7],
    ["Fonio", 240, 1, 4, 1.7, 0.05],
    ["Maize", 442, 7.4, 37.45, 6.15, 11.03],
    ["Millet", 484, 2, 37.9, 13.4, 9.15],
    ["Rice (Brown)", 346, 2.8, 38.1, 9.9, 0.8],
    ["Rice, (White)", 345, 3.6, 37.6, 5.4, 0.1]
]

column_headings = ["Cereal", "Calories", "Fat", "Protein", "Fibre", "Vitamin E"]

output_filename = 'my_cereals.csv'

with open(output_filename, "w", encoding='utf-8', newline='') as output_file:
    writer = csv.writer(output_file, quoting=csv.QUOTE_NONNUMERIC)
    # writer.writerows(column_headings)
    writer.writerow(column_headings)
    writer.writerows(cereals)
