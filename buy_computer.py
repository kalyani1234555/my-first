available_parts = ["computer",
                   "monitor",
                   "mouse",
                   "mouse mat",
                   "hdmi cable",
                   "dvd drive"]
current_choice = "_"
computer_parts = [] # create an empty list
# valid_choices = [str(i) for i in range(1, len(available_parts) + 1)]
valid_choices = []
for i in range (1, len(available_parts) + 1):
    valid_choices.append(str(i))
print(valid_choices)

while current_choice != '0':
    if current_choice in valid_choices:
    # if current_choice in "123456":
        index = int(current_choice) - 1
        chosen_parts = available_parts[index]
        if chosen_parts in computer_parts:
            print("removing {}".format(current_choice))
            computer_parts.remove(chosen_parts)
        else:
            print("adding {}".format(current_choice))
            computer_parts.append(chosen_parts)
        print("your list now contains: {}".format(computer_parts))
        # if current_choice == '1':
        #     computer_parts.append("computer")
        # elif current_choice == '2':
        #     computer_parts.append("monitor")
        # elif current_choice == '3':
        #     computer_parts.append("keyboard")
        # elif current_choice == '4':
        #     computer_parts.append("mouse")
        # elif current_choice == '5':
        #     computer_parts.append("mouse mat")
        # elif current_choice == '6':
        #     computer_parts.append("hdmi cable")
    else:
        print("please choose your option from the list below:")
        for number, parts in enumerate(available_parts):
            print("{0}: {1}".format(number + 1, parts))
            # print("{0}: {1}".format(available_parts.index(parts) + 1, parts))
        # print("1: computer")
        # print("2: monitor")
        # print("3: keyboard")
        # print("4: mouse")
        # print("5: mouse mat")
        # print("6: hdmi cable")
        # print("0: exit")
    current_choice = input()
print(computer_parts)
