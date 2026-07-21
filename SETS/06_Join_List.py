# ----CODE1----
set1 = {1,2,3,4,5,6}
set2 = {5,7,8,4,9,2,6}
set3 = set1.union(set2)
print(set3) #output = {1, 2, 3, 4, 5, 6, 7, 8, 9}

# ----CODE2----
set1 = {1,2,3,4,5,6}
set2 = {5,7,8,4,9,2,6}
set3 = set1.intersection(set2)
print(set3) #output = {2, 4, 5, 6}

# ----CODE3----
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = {"John", "Elena"}
set4 = {"apple", "bananas", "cherry"}

myset = set1.union(set2, set3, set4)
print(myset) #output = {1, 2, 3, 'apple', 'bananas', 'cherry', 'a', 'b', 'John', 'Elena', 'c'}

# ----CODE4----
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = {"John", "Elena"}
set4 = {"apple", "bananas", "cherry"}

myset = set1 |set2 | set3 | set4
print(myset) #output = {1, 2, 3, 'apple', 'bananas', 'cherry', 'a', 'b', 'John', 'Elena', 'c'}

# ----CODE5----
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1 & set2
print(set3) #output = {'apple'}

# ----CODE6----
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set3 = set1.difference(set2)
print(set3) #output = {'banana', 'cherry'}

# ----CODE7----
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set3 = set1-set2
print(set3) #output = {'banana', 'cherry'}

# ----CODE8----
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1 ^ set2
print(set3) #output = {'microsoft', 'cherry', 'banana', 'google'}