# ----Code1----
dict1 = {
  "brand": "Toyata",
  "model": "Fortuner",
  "year": 2020
}
dict1.pop("year")
print(dict1) #output = {'brand': 'Toyata', 'model': 'Fortuner'}

# ----Code2----
dict1 = {
  "brand": "Toyata",
  "model": "Fortuner",
  "year": 2020
}
dict1.popitem()
print(dict1) #output = {'brand': 'Toyata', 'model': 'Fortuner'}(remove the last value)

# ----Code3----
dict1 = {
  "brand": "Toyata",
  "model": "Fortuner",
  "year": 2020
}
dict1.clear()
print(dict1) #output = {}

# ----Code4----
dict1 = {
  "brand": "Toyata",
  "model": "Fortuner",
  "year": 2020
}
del dict1
print(dict1) #output = name 'dict1' is not defined