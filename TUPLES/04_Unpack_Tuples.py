# ----CODE1----#
fruits = ("apple", "banana", "cherry")

(x, y, z) = fruits

print(x) #output = apple
print(y) #output = banana
print(z) #output = cherry

# ----CODE2----#
fruits = ("apple", "banana", "cherry")

(x, y, *z) = fruits

print(x) #output = apple
print(y) #output = banana
print(z) #output = ['cherry']

# ----CODE3----#
fruits = ("apple", "banana", "cherry")

(x, *y, z) = fruits

print(x) #output = apple
print(y) #output = ['banana']
print(z) #output = cherry