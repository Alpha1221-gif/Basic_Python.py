# ----CODE1---- #
list = ["Iron man", "Hulk", "Doctor strange","Captian America","Black panther"]
list.append("Ant Man")
print(list)
# output = ['Iron man', 'Hulk', 'Doctor strange', 'Captian America', 'Black panther', 'Ant Man']

# ----CODE2---- #
list = ["Iron man", "Hulk", "Doctor strange","Captian America","Black panther"]
list.insert(3,"Ant Man")
print(list)
# output = ['Iron man', 'Hulk', 'Doctor strange', 'Ant Man', 'Captian America', 'Black panther']

# ----CODE3---- #
list1 = ["Iron man", "Hulk", "Doctor strange"]
list2 = ["Captian America","Black panther"]
list1.extend(list2)
print(list1)
# output = ['Iron man', 'Hulk', 'Doctor strange', 'Captian America', 'Black panther']