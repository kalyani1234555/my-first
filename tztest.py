import pytz
import datetime

# country = "Europe/Moscow"

# tz_to_display = pytz.timezone(country)
# print(tz_to_display)
# local_time = datetime.datetime.now(tz=tz_to_display)
# print("The time {} in {} ".format(country, local_time))
# # print("Utc is {}".format(datetime.datetime.utcnow()))
#
# for x in pytz.all_timezones:
#     print(x)
# print()
# for x in sorted(pytz.country_names):
#     print(x + ": " + pytz.country_names[x])
# print()
# for x in sorted(pytz.country_names):
#     print("{}: {}: {}".format(x, pytz.country_names[x], pytz.country_timezones[x]))
# for x in sorted(pytz.country_names):
#     print("{}: {}: {}".format(x, pytz.country_names[x], pytz.country_timezones.get(x)))

for x in sorted(pytz.country_names):
    print("{}: {}".format(x, pytz.country_names[x]))
    if x in pytz.country_timezones:
        for zone in sorted(pytz.country_timezones[x]):
            tz_to_display = pytz.timezone(zone)
            local_time = datetime.datetime.now(tz=tz_to_display)
            print("\t\t{}: {}".format(zone, local_time))
    else:
        print("\t\tNo time zone defined")
