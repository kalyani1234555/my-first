input_filename = 'country_info.txt'

countries = {}
code_lookup = {}
with open(input_filename) as country_file:
    country_file.readline()
    for row in country_file:
        data = row.strip("\n").split("|")
        country, capital, code, code3, dialing, timezone, currency = data
        # print(data)
        # print(country, capital, code, code3, dialing, timezone, currency, sep='\n\t')
        country_dict = {
            'name': country,
            'capital': capital,
            'country code': code,
            'cc3': code3,
            'dialing_code': dialing,
            'timezone': timezone,
            'currency': currency,
        }
        # print(country_dict)
        countries[country.casefold()] = country_dict
        countries[code.casefold()] = country_dict
        code_lookup[code.casefold()] = country_dict
print(countries)
print(code_lookup)

while True:
    # chosen_country = input("please entry the county: ").casefold()
    chosen_country = input("please entry the county: ")
    country_key = chosen_country.casefold()
    # if chosen_country in countries:
    if country_key in countries:
        country_data = countries[country_key]
        print(f"The capital of {chosen_country} is {country_data['capital']}")
    elif country_key in code_lookup:
        country_data = code_lookup[country_key]
        print(f"The capital of {chosen_country} is {country_data['capital']}")

    elif chosen_country == "quit":
        break
