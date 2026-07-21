# ----Code1----
dict1 = {
  "brand": "Toyata",
  "model": "Fortuner",
  "year": 2020
}
dict1["year"] = 2026
print(dict1) #output = {'brand': 'Toyata', 'model': 'Fortuner', 'year': 2026}

# ----Code2----
dict1 = {
  "brand": "Toyata",
  "model": "Fortuner",
  "year": 2020
}
dict1.update({"year":2026})
print(dict1) #output = {'brand': 'Toyata', 'model': 'Fortuner', 'year': 2026}

