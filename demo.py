a_string = "this is \n a string split\t\t and tabbed"
print(a_string)

raw_string = r"this is \n a string split\t\t and tabbed"
print(raw_string)

b_string ="this is"+chr(10)+"a string split"+chr(9)+chr(9)+"and tabbed"
print(b_string)

backslash_string = "this is a backslash \followed by a text"
backslash_string1 = "this is a backslash \\followed by a text"
backslash_string2 = r"this is a backslash \followed by a text"
print(backslash_string)
print(backslash_string1)
print(backslash_string2)

error_string = "this string ends with \\"
# error_string1 = r"this string ends with \"
print(error_string)
