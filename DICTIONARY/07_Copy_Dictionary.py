# ----Code1----
dict1 = {
  "brand": "Toyata",
  "model": "Fortuner",
  "year": 2020
}
x = dict1.copy()
print(x) #output = {'brand': 'Toyata', 'model': 'Fortuner', 'year': 2020}

# ----Code2----
dict1 = {
  "brand": "Toyata",
  "model": "Fortuner",
  "year": 2020
}
x = dict(dict1)
print(x) #output = {'brand': 'Toyata', 'model': 'Fortuner', 'year': 2020}