# ----CODE1----
a = 5
b = 2
if a > b: print("a is greater than b")
#output = a is greater than b

# ----CODE2----
a = 56
b = 170
print("A") if a > b else print("B")
#output = B

# ----CODE3----
a = 13
b = 28
bigger = a if a > b else b
print("Bigger is", bigger)
#output = Bigger is 28

# ----CODE4----
a = 330
b = 330
print("A") if a > b else print("=") if a == b else print("B")
#output = '='

# ----CODE5----
x = 15
y = 20
max_value = x if x > y else y
print("Maximum value:", max_value)
#output = Maximum value: 20

# ----CODE6----
username = ""
display_name = username if username else "Guest"
print("Welcome,", display_name)
#output = Welcome, Guest

