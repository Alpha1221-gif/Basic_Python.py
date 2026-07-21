# ----Code1----
dict1 = {
  "brand": "Toyata",
  "model": "Fortuner",
  "year": 2020
}
x = dict1["model"]
print(x) #output = Fortuner

# ----Code2----
dict1 = {
  "brand": "Toyata",
  "model": "Fortuner",
  "year": 2020
}
x = dict1.get("model")
print(x) #output = Fortuner

# ----Code3----
dict1 = {
  "brand": "Toyata",
  "model": "Fortuner",
  "year": 2020
}
dict1["Color"] = "Black"
print(dict1) #output = {'brand': 'Toyata', 'model': 'Fortuner', 'year': 2020, 'Color': 'Black'}

# ----Code4----
dict1 = {
  "brand": "Toyata",
  "model": "Fortuner",
  "year": 2020
}
x = dict1.values()
print(x) #output = dict_values(['Toyata', 'Fortuner', 2020])

# ----Code5----
dict1 = {
  "brand": "Toyata",
  "model": "Fortuner",
  "year": 2020
}
dict1["year"] = 2026
print(dict1) #output = {'brand': 'Toyata', 'model': 'Fortuner', 'year': 2026}

# ----Code6----
dict1 = {
  "brand": "Toyata",
  "model": "Fortuner",
  "year": 2020
}
x = dict1.values()
print(x) #output = dict_values(['Toyata', 'Fortuner', 2020])
dict1["Color"] = "Black"
print(x) #output = dict_values(['Toyata', 'Fortuner', 2020, 'Black'])

# ----Code7----
dict1 = {
  "brand": "Toyata",
  "model": "Fortuner",
  "year": 2020
}
x = dict1.items()
print(x) #output = dict_items([('brand', 'Toyata'), ('model', 'Fortuner'), ('year', 2020)])

# ----Code8----
dict1 = {
  "brand": "Toyata",
  "model": "Fortuner",
  "year": 2020
}
if "model" in dict1:
    print("model is present!") #output = model is present!