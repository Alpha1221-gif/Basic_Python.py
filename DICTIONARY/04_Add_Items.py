# ----Code1----
dict1 = {
  "brand": "Toyata",
  "model": "Fortuner",
  "year": 2020
}
dict1["Color"] = "Black"
print(dict1) #output = {'brand': 'Toyata', 'model': 'Fortuner', 'year': 2020, 'Color': 'Black'}

# ----Code2----
dict1 = {
  "brand": "Toyata",
  "model": "Fortuner",
  "year": 2020
}
dict1.update({"Color":"Black"})
print(dict1) #output = {'brand': 'Toyata', 'model': 'Fortuner', 'year': 2020, 'Color': 'Black'}