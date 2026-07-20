# ----CODE1---- #
list = ["Iron man", "Hulk", "Doctor strange","Captian America","Black panther"]
list.remove("Hulk")
print(list)
# output = ['Iron man', 'Doctor strange', 'Captian America', 'Black panther']

# ----CODE2---- #
list = ["Iron man", "Hulk", "Doctor strange","Captian America","Black panther"]
list.pop(3)
print(list)
# output = ['Iron man', 'Hulk', 'Doctor strange', 'Black panther']

# ----CODE3---- #
list = ["Iron man", "Hulk", "Doctor strange","Captian America","Black panther"]
list.pop()
print(list)
# output = ['Iron man', 'Hulk', 'Doctor strange', 'Captian America']

# ----CODE4---- #
list = ["Iron man", "Hulk", "Doctor strange","Captian America","Black panther"]
del list[3]
print(list)
# output = ['Iron man', 'Hulk', 'Doctor strange', 'Black panther']

# ----CODE5---- #
list = ["Iron man", "Hulk", "Doctor strange","Captian America","Black panther"]
list.clear()
print(list)
# output = []

# ----CODE6---- #
list = ["Iron man", "Hulk", "Doctor strange","Captian America","Black panther"]
del list
# output = Delete the entire list