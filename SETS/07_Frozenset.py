# ----CODE1----
x = frozenset({"apple", "banana", "cherry"})
print(x)   #output = frozenset({'cherry', 'banana', 'apple'})
print(type(x))  #output = <class 'frozenset'>

# ----CODE2----
# copy() - Returns a shallow copy
set1 = {1, 2, 3, 4, 5, 6}
set2 = set1.copy()
print(set2)  # Output: {1, 2, 3, 4, 5, 6}

# ----CODE3----
# difference() or '-' - Returns a new set with the difference
set1 = {1, 2, 3, 4, 5, 6}
set2 = {5, 7, 8, 4, 9, 2, 6}
set3 = set1.difference(set2)
print(set3)  # Output: {1, 3}

# ----CODE4----
# intersection() or '&' - Returns a new set with the intersection
set1 = {1, 2, 3, 4, 5, 6}
set2 = {5, 7, 8, 4, 9, 2, 6}
set3 = set1.intersection(set2)
print(set3)  # Output: {2, 4, 5, 6}

# ----CODE5----
# isdisjoint() - Returns True if there is NO intersection
set1 = {1, 2, 3}
set2 = {7, 8, 9}
result = set1.isdisjoint(set2)
print(result)  # Output: True

# ----CODE6----
# issubset() or '<=' - Returns True if it is a subset of another
set1 = {2, 4}
set2 = {1, 2, 3, 4, 5}
result = set1.issubset(set2)
print(result)  # Output: True

# ----CODE7----
# issuperset() or '>=' - Returns True if it is a superset of another
set1 = {1, 2, 3, 4, 5}
set2 = {2, 4}
result = set1.issuperset(set2)
print(result)  # Output: True

# ----CODE8----
# symmetric_difference() or '^' - Returns a new set with elements in either set, but not both
set1 = {1, 2, 3, 4, 5, 6}
set2 = {5, 7, 8, 4, 9, 2, 6}
set3 = set1.symmetric_difference(set2)
print(set3)  # Output: {1, 3, 7, 8, 9}

# ----CODE9----
# union() or '|' - Returns a new set containing all elements from both sets
set1 = {1, 2, 3}
set2 = {4, 5, 6}
set3 = set1.union(set2)
print(set3)  # Output: {1, 2, 3, 4, 5, 6}
