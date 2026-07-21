# ----Code1----
dict1 = {
  "brand": "Toyata",
  "model": "Fortuner",
  "year": 2020
}
for i in dict1:
 print(i) 
'''brand
model
year'''

# ----Code2----
dict1 = {
  "brand": "Toyata",
  "model": "Fortuner",
  "year": 2020
}
for i in dict1:
 print(dict1[i])
'''Toyata
Fortuner
2020'''

# ----Code3----
dict1 = {
  "brand": "Toyata",
  "model": "Fortuner",
  "year": 2020
}
for i in dict1.values():
 print(i)
'''Toyata
Fortuner
2020
''' 

# ----Code4----
dict1 = {
  "brand": "Toyata",
  "model": "Fortuner",
  "year": 2020
}
for i in dict1.keys():
 print(i)
 '''brand
model
year'''

# ----Code5 ----
dict1 = {
  "brand": "Toyata",
  "model": "Fortuner",
  "year": 2020
}
for x,y in dict1.items():
 print(x,y)
 '''brand Toyata
model Fortuner
year 2020'''