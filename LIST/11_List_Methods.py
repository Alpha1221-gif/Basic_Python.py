# ----CODE01---- #
# Concept: append() - Adds an element at the end of the list
fruits = ["apple", "banana"]
fruits.append("cherry")
print(fruits) # output = ['apple', 'banana', 'cherry']

# ----CODE02---- #
# Concept: clear() - Removes all the elements from the list
fruits = ["apple", "banana", "cherry"]
fruits.clear()
print(fruits) # output = []

# ----CODE03---- #
# Concept: copy() - Returns a copy of the list
fruits = ["apple", "banana", "cherry"]
new_list = fruits.copy()
print(new_list) # output = ['apple', 'banana', 'cherry']

# ----CODE04---- #
# Concept: count() - Returns the number of elements with the specified value
fruits = ["apple", "banana", "cherry", "apple"]
x = fruits.count("apple")
print(x) # output = 2

# ----CODE05---- #
# Concept: extend() - Add the elements of a list (or any iterable), to the end of the current list
fruits = ["apple", "banana"]
cars = ["Ford", "BMW"]
fruits.extend(cars)
print(fruits) # output = ['apple', 'banana', 'Ford', 'BMW']

# ----CODE06---- #
# Concept: index() - Returns the index of the first element with the specified value
fruits = ["apple", "banana", "cherry"]
x = fruits.index("banana")
print(x) # output = 1

# ----CODE07---- #
# Concept: insert() - Adds an element at the specified position
fruits = ["apple", "banana", "cherry"]
fruits.insert(1, "orange")
print(fruits) # output = ['apple', 'orange', 'banana', 'cherry']

# ----CODE08---- #
# Concept: pop() - Removes the element at the specified position
fruits = ["apple", "banana", "cherry"]
removed_item = fruits.pop(1)
print(fruits) # output = ['apple', 'cherry']
print(removed_item) # output = banana

# ----CODE09---- #
# Concept: remove() - Removes the item with the specified value
fruits = ["apple", "banana", "cherry"]
fruits.remove("banana")
print(fruits) # output = ['apple', 'cherry']

# ----CODE10---- #
# Concept: reverse() - Reverses the order of the list
fruits = ["apple", "banana", "cherry"]
fruits.reverse()
print(fruits) # output = ['cherry', 'banana', 'apple']

# ----CODE11---- #
# Concept: sort() - Sorts the list
fruits = ["cherry", "apple", "banana"]
fruits.sort()
print(fruits) # output = ['apple', 'banana', 'cherry']
