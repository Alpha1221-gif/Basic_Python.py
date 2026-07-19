# ----CODE01---- #
# Concept: Identity Operator (is) - Returns True if both variables point to the same object
x = ["apple", "banana"]
y = ["apple", "banana"]
z = x

print(x is z)
# output = True

# Note: Even though x and y have the same content, they are different objects in memory
print(x is y)
# output = False


# ----CODE02---- #
# Concept: Identity Operator (is not) - Returns True if both variables do not point to the same object
x = ["apple", "banana"]
y = ["apple", "banana"]
z = x

print(x is not y)
# output = True

print(x is not z)
# output = False
