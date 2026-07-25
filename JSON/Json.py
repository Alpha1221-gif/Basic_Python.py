# ----CODE1----
import json

x = '{"name":"Astro","age":25,"city":"america"}'

y = json.loads(x)
print(y["age"])  #output = 25

# ----CODE2----
import json

x = {"name":"Astro","age":25,"city":"america"}

y = json.dumps(x) #convert it into JSON
print(y)  #output = {"name": "Astro", "age": 25, "city": "america"}

# ----CODE3----
'''You can convert Python objects of the following types, into JSON strings:'''
import json

print(json.dumps({"name": "John", "age": 30}))
print(json.dumps(["apple", "bananas"]))
print(json.dumps(("apple", "bananas")))
print(json.dumps("hello"))
print(json.dumps(42))
print(json.dumps(31.76))
print(json.dumps(True))
print(json.dumps(False))
print(json.dumps(None))


# ----CODE4----
import json
a = {
  "name":"Robert",
  "age":31,
  "married":True,
  "divorsed":False,
  "childern":["Ann","Billy"],
  "pets":None,
  "cars": [
    {"model": "BMW 230", "mpg": 27.5},
    {"model": "Ford Edge", "mpg": 24.1}
    ]
}
print(json.dumps(a))
'''{"name": "Robert", "age": 31, "married": true, "divorsed": false,
"childern": ["Ann", "Billy"], "pets": null, "cars": [{"model": "BMW 230", "mpg": 27.5},
{"model": "Ford Edge", "mpg": 24.1}]}'''

# ----CODE5----
print(json.dumps(a, indent=4)) #he json.dumps() method has parameters to make it easier to read the result:
'''{
    "name": "Robert",
    "age": 31,
    "married": true,
    "divorsed": false,
    "childern": [
        "Ann",
        "Billy"
    ],
    "pets": null,
    "cars": [
        {
            "model": "BMW 230",
            "mpg": 27.5
        },
        {
            "model": "Ford Edge",
            "mpg": 24.1
        }
    ]
}'''


# ----CODE6----
