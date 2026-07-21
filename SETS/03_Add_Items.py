# ----CODE1----
set1 = {"apple", "banana", "cherry","mango"}
set1.add("orange")
print(set1) #output = {'banana', 'cherry', 'mango', 'apple', 'orange'}

# ----CODE2----
set1 = {"apple", "banana", "cherry","mango"}
set2 = {"orange","dragon fruit"}
set1.update(set2)
print(set1) #output = {'banana', 'mango', 'apple', 'cherry', 'orange', 'dragon fruit'}

# ----CODE3----
set1 = {"apple", "banana", "cherry","mango"}
set2 = ["orange","dragon fruit"]
set1.update(set2)
print(set1) #output = {'banana', 'mango', 'apple', 'cherry', 'orange', 'dragon fruit'}