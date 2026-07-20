# ----CODE1---- add() - Adds an element to the set
b = {"apple", "banana"}
b.add("cherry")
print(b)  # output = {'apple', 'banana', 'cherry'}

# ----CODE2---- clear() - Removes all elements from the set
b = {"apple", "banana"}
b.clear()
print(b)  # output = set()

# ----CODE3---- copy() - Returns a copy of the set
b = {"apple", "banana"}
c = b.copy()
print(c)  # output = {'apple', 'banana'}

# ----CODE4---- difference() or '-' - Returns a set containing the difference
b = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
print(b - y)  # output = {'banana', 'cherry'}

# ----CODE5---- difference_update() or '-=' - Removes matching items from the original set
b = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
b -= y
print(b)  # output = {'banana', 'cherry'}

# ----CODE6---- discard() - Removes the specified item
b = {"apple", "banana", "cherry"}
b.discard("banana")
print(b)  # output = {'apple', 'cherry'}

# ----CODE7---- intersection() or '&' - Returns a set that is the intersection of sets
b = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
print(b & y)  # output = {'apple'}

# ----CODE8---- intersection_update() or '&=' - Keeps only the intersecting items in the original set
b = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
b &= y
print(b)  # output = {'apple'}

# ----CODE9---- isdisjoint() - Returns True if NO items match between sets
b = {"apple", "banana"}
y = {"google", "microsoft"}
print(b.isdisjoint(y))  # output = True

# ----CODE10---- issubset() or '<=' - Returns True if all items are present in another set
b = {"apple", "banana"}
y = {"apple", "banana", "cherry"}
print(b <= y)  # output = True

# ----CODE11---- Proper Subset or '<' - Returns True if all items are in another LARGER set
b = {"apple", "banana"}
y = {"apple", "banana", "cherry"}
print(b < y)  # output = True

# ----CODE12---- issuperset() or '>=' - Returns True if all items of another set are in this set
b = {"apple", "banana", "cherry"}
y = {"apple", "banana"}
print(b >= y)  # output = True

# ----CODE13---- Proper Superset or '>' - Returns True if all items of another SMALLER set are in this set
b = {"apple", "banana", "cherry"}
y = {"apple", "banana"}
print(b > y)  # output = True

# ----CODE14---- pop() - Removes and returns a random element from the set
b = {"apple", "banana"}
b.pop()
print(len(b))  # output = 1

# ----CODE15---- remove() - Removes the specified element
b = {"apple", "banana", "cherry"}
b.remove("banana")
print(b)  # output = {'apple', 'cherry'}

# ----CODE16---- symmetric_difference() or '^' - Returns a set with the symmetric differences of two sets
b = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
print(b ^ y)  # output = {'banana', 'cherry', 'google', 'microsoft'}

# ----CODE17---- symmetric_difference_update() or '^=' - Inserts the symmetric differences from this set and another
b = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
b ^= y
print(b)  # output = {'banana', 'cherry', 'google', 'microsoft'}

# ----CODE18---- union() or '|' - Return a set containing the union of sets
b = {"apple", "banana"}
y = {"google", "microsoft"}
print(b | y)  # output = {'apple', 'banana', 'google', 'microsoft'}

# ----CODE19---- update() or '|=' - Update the set with the union of this set and others
b = {"apple", "banana"}
y = {"google", "microsoft"}
b |= y
print(b)  # output = {'apple', 'banana', 'google', 'microsoft'}
