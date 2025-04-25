data = [
    "Andromeda - Shrub",
    "Bellflower - Flower",
    "China Pink - Flower",
    "Daffodil - Flower",
    "Evening Primrose - Flower",
]

# plants_filename = "flowers_print1.txt"
#
# with open(plants_filename, "w") as plants:
#     for plant in data:
#         print(plant, file=plants)
#
# new_list = []
# with open(plants_filename) as plants:
#     for plant in plants:
#         new_list.append(plant.rstrip( ))
#
# print(new_list)

# plants_filename = "flowers_print1.txt"
#
# with open(plants_filename, "w") as plants:
#     for plant in data:
#         plants.write(plant)
#
# print(data)
# string_representation = data.__str__()
# print(type(string_representation))

filename = "test_numbers.txt"
with open(filename, "w") as test:
    for i in range(10):
        print(i, file=test)

with open(filename, "w") as test:
    for i in range(10):
        test.write(str(i) + "\n")
