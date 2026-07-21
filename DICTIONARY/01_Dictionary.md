🐍 Python Dictionaries: Ultimate Beginner's Guide

Welcome to the beginner's guide to Python dictionaries! Dictionaries are used to store data values in **key:value** pairs. They are ordered, changeable, and do not allow duplicate keys. They are written with curly brackets `{}`.

> 💡 **Tip:** As of Python 3.7, dictionaries are ordered. Prior to that, they were unordered.

---

## 🔍 1. Access Items
You can access the items of a dictionary by referring to its key name inside square brackets `[]` or using the `get()` method.

```python
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

# Access value by key name
print(car["model"])  # Output: Mustang

# Access value using get()
print(car.get("year")) # Output: 1964
```

---

## 🔄 2. Change Items
You can change the value of a specific item by referring to its key name, or by using the `update()` method.

```python
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

# Change the year
car["year"] = 2020
print(car["year"]) # Output: 2020
```

---

## ➕ 3. Add Items
Adding an item to the dictionary is done by using a new index key and assigning a value to it.

```python
car = {
  "brand": "Ford",
  "model": "Mustang"
}

# Add a new color key
car["color"] = "red"
print(car) # Output: {'brand': 'Ford', 'model': 'Mustang', 'color': 'red'}
```

---

## ❌ 4. Remove Items
There are several methods to remove items from a dictionary, including `pop()`, `popitem()`, and the `del` keyword.

```python
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

# Remove a specific item by key name
car.pop("model")

# Remove the last inserted item
car.popitem()

# Delete the dictionary entirely
del car
```

---

## 🔁 5. Loop Dictionaries
You can loop through a dictionary by using a `for` loop to access keys, values, or both using `.keys()`, `.values()`, or `.items()`.

```python
car = {"brand": "Ford", "model": "Mustang"}

# Loop through keys and values together
for key, value in car.items():
    print(key, ":", value)
# Output:
# brand : Ford
# model : Mustang
```

---

## 📋 6. Copy Dictionaries
You cannot copy a dictionary simply by typing `dict2 = dict1`. Use the built-in dictionary method `copy()`.

```python
car = {"brand": "Ford", "model": "Mustang"}

# Make a copy
my_car = car.copy()
print(my_car) # Output: {'brand': 'Ford', 'model': 'Mustang'}
```

---

## 🪆 7. Nested Dictionaries
A dictionary can contain dictionaries; this is called nested dictionaries.

```python
my_family = {
  "child1": {
    "name": "Emil",
    "year": 2004
  },
  "child2": {
    "name": "Tobias",
    "year": 2007
  }
}

# Access nested item
print(my_family["child1"]["name"]) # Output: Emil
```

---

## 🛠️ 8. Dictionary Methods Quick Reference

| Method | What it does |
| :--- | :--- |
| `clear()` | Removes all the elements from the dictionary |
| `copy()` | Returns a copy of the dictionary |
| `fromkeys()` | Returns a dictionary with the specified keys and value |
| `get()` | Returns the value of the specified key |
| `items()` | Returns a list containing a tuple for each key value pair |
| `keys()` | Returns a list containing the dictionary's keys |
| `pop()` | Removes the element with the specified key |
| `popitem()` | Removes the last inserted key-value pair |
| `setdefault()` | Returns the value of the specified key. If the key does not exist: insert the key, with the specified value |
| `update()` | Updates the dictionary with the specified key-value pairs |
| `values()` | Returns a list of all the values in the dictionary |

---

🚀 **Happy Coding!** Test these out by creating your own customized key-value pairs.

## 📝 License

This project is open-source and available under the [MIT License](LICENSE).

