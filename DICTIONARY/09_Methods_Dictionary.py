# ----Code1----
# clear() removes all elements
dict1 = { "brand": "Toyata", "model": "Fortuner", "year": 2020 }
dict1.clear()
print(dict1) 
#output = {}

# ----Code2----
# copy() returns a copy
dict1 = { "brand": "Toyata", "model": "Fortuner", "year": 2020 }
x = dict1.copy()
print(x) 
#output = {'brand': 'Toyata', 'model': 'Fortuner', 'year': 2020}

# ----Code3----
# fromkeys() creates a dictionary from keys with a specified value
keys = ("brand", "model", "year")
x = dict.fromkeys(keys, "unknown")
print(x) 
#output = {'brand': 'unknown', 'model': 'unknown', 'year': 'unknown'}

# ----Code4----
# get() returns the value of the specified key
dict1 = { "brand": "Toyata", "model": "Fortuner", "year": 2020 }
x = dict1.get("model")
print(x) 
#output = Fortuner

# ----Code5----
# items() returns a list containing a tuple for each key value pair
dict1 = { "brand": "Toyata", "model": "Fortuner", "year": 2020 }
x = list(dict1.items())
print(x) 
#output = [('brand', 'Toyata'), ('model', 'Fortuner'), ('year', 2020)]

# ----Code6----
# keys() returns a list containing the dictionary's keys
dict1 = { "brand": "Toyata", "model": "Fortuner", "year": 2020 }
x = list(dict1.keys())
print(x) 
#output = ['brand', 'model', 'year']

# ----Code7----
# pop() removes the element with the specified key
dict1 = { "brand": "Toyata", "model": "Fortuner", "year": 2020 }
dict1.pop("year")
print(dict1) 
#output = {'brand': 'Toyata', 'model': 'Fortuner'}

# ----Code8----
# popitem() removes the last inserted key-value pair
dict1 = { "brand": "Toyata", "model": "Fortuner", "year": 2020 }
dict1.popitem()
print(dict1) 
#output = {'brand': 'Toyata', 'model': 'Fortuner'}

# ----Code9----
# setdefault() returns the value of a key. If it doesn't exist, inserts it.
dict1 = { "brand": "Toyata", "model": "Fortuner", "year": 2020 }
x = dict1.setdefault("color", "White")
print(dict1) 
#output = {'brand': 'Toyata', 'model': 'Fortuner', 'year': 2020, 'color': 'White'}

# ----Code10----
# update() updates the dictionary with the specified key-value pairs
dict1 = { "brand": "Toyata", "model": "Fortuner", "year": 2020 }
dict1.update({"year": 2024, "color": "Black"})
print(dict1) 
#output = {'brand': 'Toyata', 'model': 'Fortuner', 'year': 2024, 'color': 'Black'}

# ----Code11----
# values() returns a list of all the values in the dictionary
dict1 = { "brand": "Toyata", "model": "Fortuner", "year": 2020 }
x = list(dict1.values())
print(x) 
#output = ['Toyata', 'Fortuner', 2020]
