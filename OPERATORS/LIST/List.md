# 🐍 Python Lists: Ultimate Beginner's Guide

<img src="https://githubusercontent.com" alt="python" width="50" height="50"/>

Welcome to the beginner's guide to Python lists! A list is used to store multiple items in a single variable. Lists are ordered, changeable, and allow duplicate values.

> 💡 **Tip:** Python indexes start at `0`. The first item is always `[0]`.

---

## 🔍 1. Access List Items
You can access list items by referring to their index number inside square brackets `[]`.

```python
fruits = ["apple", "banana", "cherry"]

# Get the first item
print(fruits[0])  # Output: apple

# Get the last item (Negative indexing)
print(fruits[-1]) # Output: cherry
```

---

## 🔄 2. Change List Items
To change the value of a specific item, refer to its index number.

```python
fruits = ["apple", "banana", "cherry"]

# Change "banana" to "blueberry"
fruits[1] = "blueberry"
print(fruits) # Output: ['apple', 'blueberry', 'cherry']
```

---

## ➕ 3. Add List Items
You can add new items to a list using `append()` or `insert()`.

```python
fruits = ["apple", "banana"]

# Add an item to the END of the list
fruits.append("orange")
print(fruits) # Output: ['apple', 'banana', 'orange']

# Add an item at a SPECIFIC position
fruits.insert(1, "cherry")
print(fruits) # Output: ['apple', 'cherry', 'banana', 'orange']
```

---

## ❌ 4. Remove List Items
You can remove items using `remove()`, `pop()`, or the `del` keyword.

```python
fruits = ["apple", "banana", "cherry"]

# Remove a specific item by name
fruits.remove("banana")

# Remove an item by its index (removes 'cherry')
fruits.pop(1) 

# Delete the first item
del fruits[0]
```

---

## 🔁 5. Loop Through a List
You can loop through all the items in a list one by one using a `for` loop.

```python
fruits = ["apple", "banana", "cherry"]

for x in fruits:
    print(x)
# Output:
# apple
# banana
# cherry
```

---

## ⚡ 6. List Comprehension
List comprehension offers a shorter syntax when you want to create a new list based on the values of an existing list.

```python
fruits = ["apple", "banana", "cherry"]

# Shorter List Comprehension way
new_list = [x for x in fruits]
print(new_list) # Output: ['apple', 'banana', 'cherry']
```

---

## 📊 7. Sort a List
The `sort()` method will sort the list alphanumerically or ascending by default.

```python
fruits = ["cherry", "apple", "banana"]
fruits.sort()
print(fruits) # Output: ['apple', 'banana', 'cherry']

numbers = [4, 2, 1, 3]
numbers.sort()
print(numbers) # Output: [1, 2, 3, 4]
```

---

## 📋 8. Copy a List
You cannot copy a list simply by typing `list2 = list1`, because `list2` will only point to `list1`. Use `copy()` instead.

```python
fruits = ["apple", "banana", "cherry"]

# Make a copy
my_fruits = fruits.copy()
print(my_fruits) # Output: ['apple', 'banana', 'cherry']
```

---

## 🔗 9. Join Two Lists
The easiest way to join or combine two lists in Python is by using the `+` operator.

```python
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

# Join using +
list3 = list1 + list2
print(list3) # Output: ['a', 'b', 'c', 1, 2, 3]
```

---

## 🛠️ 10. Common List Methods Quick Reference

| Method | What it does |
| :--- | :--- |
| `append()` | Adds an element at the end of the list |
| `clear()` | Removes all the elements from the list |
| `copy()` | Returns a copy of the list |
| `count()` | Returns the number of elements with the specified value |
| `extend()` | Add the elements of a list to the end of the current list |
| `index()` | Returns the index of the first element with the specified value |
| `insert()` | Adds an element at the specified position |
| `pop()` | Removes the element at the specified position |
| `remove()` | Removes the item with the specified value |
| `reverse()` | Reverses the order of the list |
| `sort()` | Sorts the list |

---

🚀 **Happy Coding!** Feel free to clone this repository and practice these methods.
