menu = [
    ["egg", "bacon"],
    ["egg", "sausage", "bacon"],
    ["egg", "spam"],
    ["egg", "bacon", "spam"],
    ["egg", "bacon", "sausage","spam"],
    ["spam", "bacon", "sausage","spam"],
    ["spam", "sausage", "spam", "bacon", "spam", "tomato", "spam" ],
    ["spam", "egg", "spam", "spam", "bacon", "spam"],
]
for meal in menu:
    for index in range(len(meal)-1,-1,-1):
        # print(index)
        if meal[index] == "spam":
            del meal[index]
    # print(meal)
    print(", ".join(meal))
# for meal in menu:
#     for item in meal:
#         if item != "spam":
#             print(item, end=" , ")
#     print()
