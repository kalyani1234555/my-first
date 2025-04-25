shopping_list = ["milk",
                 "pasta",
                 "eggs",
                 "spam",
                 "bread",
                 "rice"]
another_list = shopping_list
print(id(shopping_list))
print(id(shopping_list))

shopping_list += ["cookies"]
print(shopping_list)
print(id(shopping_list))

a = b = c = d = e = f = another_list
print(a)

print("adding cream")
b.append("cream")
print(c)
c.append("chocolate")
print(d)
