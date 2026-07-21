# ----CODE1----
set1 = {"apple", "banana", "cherry","mango"}
set1.remove("cherry")
print(set1) #output = {'banana', 'mango', 'apple'}

# ----CODE2----
set1 = {"apple", "banana", "cherry","mango"}
set1.discard("cherry")
print(set1) #output = {'mango', 'apple', 'banana'}

# ----CODE3----
set1 = {"apple", "banana", "cherry","mango"}
set1.pop()
print(set1) #output = {'apple', 'banana', 'cherry'}(remove random value)

# ----CODE4----
set1 = {"apple", "banana", "cherry","mango"}
set1.clear()
print(set1) #output = set()

# ----CODE5----
set1 = {"apple", "banana", "cherry","mango"}
del set1
print(set1) 