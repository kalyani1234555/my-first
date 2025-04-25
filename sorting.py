pangram = "The quick brown for jumps over the lazy dog"
letters = sorted(pangram)
print(letters)

numbers = [2.3, 4.5, 8.7, 3.1, 9.2, 1.6]
sorted_numbers = sorted(numbers)
print(sorted_numbers)
print(numbers)

numbers.sort()
print(numbers)
# another_sorted_numbers = numbers.sort()
# print(another_sorted_numbers)

missing_letter = sorted("The quick brown for jumped over the lazy dog",
                        key=str.casefold)
print(missing_letter)


names = ["Graham",
         "J0hn",
         "terry",
         "eric",
         "Terry",
         "michael"
         ]
names.sort(key=str.casefold)
print(names)
