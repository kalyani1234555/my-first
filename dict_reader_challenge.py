import csv
input_filename = 'country_info.txt'

dialect = csv.excel
dialect.delimiter = "|"

countries = {}
with open(input_filename, encoding='utf-8', newline='') as country_file:
    headings = country_file.readline().strip('\n').split(dialect.delimiter)
    for index, heading in enumerate(headings):
        headings[index] = heading.casefold()
    print(headings)
    # sample = ""
    # for line in range(3):
    #     sample += country_file.readline()
    # country_dialect = csv.Sniffer().sniff(sample)
    # country_file.seek(0)
    # reader = csv.DictReader(country_file, dialect=country_dialect)
    # dict_reader = csv.DictReader(country_file, delimiter='|')
    dict_reader = csv.DictReader(country_file, dialect=dialect, fieldnames=headings)
    for row in dict_reader:
        print(row)
        # countries[country.casefold()] = country_dict
        countries[row['country'].casefold()] = row
        # countries[code.casefold()] = country_dict
        countries[row['cc'].casefold()] = row

print(countries)

while True:
    chosen_country = input("please entry the county: ")
    country_key = chosen_country.casefold()
    if country_key in countries:
        country_data = countries[country_key]
        print(f"The capital of {chosen_country} is {country_data['capital']}")
    elif chosen_country == "quit":
        break
