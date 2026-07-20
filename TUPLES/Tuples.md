# 🧮 Python Tuples: Ultimate Beginner's Guide

<img src="https://githubusercontent.com" alt="python" width="50" height="50"/>

Welcome to the beginner's guide to Python tuples! A tuple is used to store multiple items in a single variable. Unlike lists, tuples are **ordered** and **unchangeable** (immutable). They are written with round brackets `()`.

> 💡 **Important:** Because tuples are unchangeable, you cannot add, remove, or modify items once the tuple is created.

---

## 🔍 1. Access Tuples
You can access tuple items by referring to their index number inside square brackets `[]`.

```python
fruits = ("apple", "banana", "cherry")

# Get the first item
print(fruits[0])  # Output: apple

# Get the last item (Negative indexing)
print(fruits[-1]) # Output: cherry
```

---

## 🔄 2. Update Tuples
Tuples cannot be changed directly. However, you can convert the tuple into a list, change the list, and convert it back into a tuple.

```python
fruits = ("apple", "banana", "cherry")

# Convert to list to make a change
fruits_list = list(fruits)
fruits_list[1] = "kiwi"

# Convert back to tuple
fruits = tuple(fruits_list)
print(fruits) # Output: ('apple', 'kiwi', 'cherry')
```

---

## 📦 3. Unpack Tuples
When we create a tuple, we normally assign values to it. This is called "packing". We can also extract the values back into variables, which is called "unpacking".

```python
fruits = ("apple", "banana", "cherry")

# Unpacking into individual variables
(green, yellow, red) = fruits

print(green)  # Output: apple
print(yellow) # Output: banana
print(red)    # Output: cherry
```

---

## 🔁 4. Loop Tuples
You can loop through the tuple items by using a `for` loop.

```python
fruits = ("apple", "banana", "cherry")

for x in fruits:
    print(x)
# Output:
# apple
# banana
# cherry
```

---

## 🔗 5. Join Tuples
To join two or more tuples, you can use the `+` operator.

```python
tuple1 = ("a", "b", "c")
tuple2 = (1, 2, 3)

# Join using +
tuple3 = tuple1 + tuple2
print(tuple3) # Output: ('a', 'b', 'c', 1, 2, 3)
```

---

## 🛠️ 6. Tuple Methods Quick Reference
Tuples have only two built-in methods because they cannot be modified.

| Method | What it does |
| :--- | :--- |
| `count()` | Returns the number of times a specified value occurs in a tuple |
| `index()` | Searches the tuple for a specified value and returns its position |

```python
numbers = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)

# Count how many times 7 appears
x = numbers.count(7)
print(x) # Output: 2

# Find the first position of 8
y = numbers.index(8)
print(y) # Output: 3
```

---

🚀 **Happy Coding!** Practice these concepts by writing your own tuple variables.
