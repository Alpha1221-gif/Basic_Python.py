# ----CODE01---- #
# Concept: sort(reverse=True) - Sorts the original list in place in descending order
numbers = [5, 2, 9, 1]
numbers.sort(reverse=True)
print(numbers) # output = [9, 5, 2, 1]

# ----CODE02---- #
# Concept: reverse() after sort() - Sorts ascending first, then reverses the list to achieve descending order
numbers = [5, 2, 9, 1]
numbers.sort()
numbers.reverse()
print(numbers) # output = [9, 5, 2, 1]
