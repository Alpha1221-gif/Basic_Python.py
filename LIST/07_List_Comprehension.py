# ----CODE01---- #
# Concept: Basic List Comprehension - Replaces a standard for loop to create a new list from an iterable
numbers = [1, 2, 3, 4]
squares = [x**2 for x in numbers]
print(squares) # output = [1, 4, 9, 16]

# ----CODE02---- #
# Concept: List Comprehension with if condition - Filters elements from a list based on a specific criteria
numbers = [1, 2, 3, 4, 5, 6]
evens = [x for x in numbers if x % 2 == 0]
print(evens) # output = [2, 4, 6]

# ----CODE03---- #
# Concept: List Comprehension with if-else condition - Transforms items using an alternative value if a condition is met
numbers = [1, 2, 3, 4]
labels = ["Even" if x % 2 == 0 else "Odd" for x in numbers]
print(labels) # output = ['Odd', 'Even', 'Odd', 'Even']

# ----CODE04---- #
# Concept: Nested for loops in List Comprehension - Flattens a 2D matrix or combines elements from multiple iterables
matrix = [[1, 2], [3, 4]]
flat = [num for row in matrix for num in row]
print(flat) # output = [1, 2, 3, 4]

# ----CODE05---- #
# Concept: Dictionary Comprehension - Creates a new dictionary using an elegant inline key-value loop syntax
words = ["apple", "banana"]
word_lengths = {word: len(word) for word in words}
print(word_lengths) # output = {'apple': 5, 'banana': 6}

# ----CODE06---- #
# Concept: Set Comprehension - Builds a collection of unique, unordered elements dynamically from an iterable loop
numbers = [1, 2, 2, 3, 3, 3]
unique_squares = {x**2 for x in numbers}
print(unique_squares) # output = {1, 4, 9}

# ----CODE07---- #
# Concept: Generator Expression - Produces memory-efficient, lazy-evaluated data values one item at a time instead of generating full lists
numbers = [1, 2, 3]
gen = (x * 10 for x in numbers)
print(list(gen)) # output = [10, 20, 30]

# ----CODE08---- #
# Concept: List Comprehension with string methods - Modifies or cleans text items efficiently within an inline loop sequence
fruits = ["  apple ", "banana  ", " CHERRY "]
cleaned = [f.strip().lower() for f in fruits]
print(cleaned) # output = ['apple', 'banana', 'cherry']
