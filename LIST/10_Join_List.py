# ----CODE1---- #
list1 = ["x", "y", "z"]
list2 = [1, 2, 3]

list3 = list1 + list2
print(list3)
# output = ['x', 'y', 'z', 1, 2, 3]

# ----CODE2---- #
list1 = ["x", "y", "z"]
list2 = [1, 2, 3]

for x in list2:
  list1.append(x)

print(list1)
# output = ['x', 'y', 'z', 1, 2, 3]

# ----CODE3---- #
list1 = ["x", "y", "z"]
list2 = [1, 2, 3]

list1.extend(list2)
print(list1)
# output = ['x', 'y', 'z', 1, 2, 3]