# 🐍 Python Sets: A Beginner's Guide 📘

A **set** in Python is an unordered collection of unique items. They are written with curly brackets `{}`.

---

## 🔍 1. Access Set Items
You cannot access items in a set by referring to an index or a key. Instead, you loop through the set or check if a value is present.

```python
# ➕ Create a set
my_set = {"apple", "banana", "cherry"}

# 🔄 Loop through the set
for x in my_set:
    print(x)

# ❔ Check if an item exists
print("banana" in my_set)  # 🟢 Returns True
```

---

## 📥 2. Add Set Items
Once a set is created, you cannot change its items, but you can add new items using the `add()` method.

```python
my_set = {"apple", "banana", "cherry"}

# 🟢 Add a single item
my_set.add("orange")
print(my_set)  # {"apple", "banana", "cherry", "orange"}
```

---

## 🗑️ 3. Remove Set Items
To remove an item in a set, use the `remove()` or `discard()` methods.

```python
my_set = {"apple", "banana", "cherry"}

# 🛑 Remove an item using remove()
my_set.remove("banana")

# ⚠️ Remove an item using discard() (won't error if item is missing)
my_set.discard("apple")
```

---

## 🔄 4. Loop Sets
You can loop through the set items by using a `for` loop.

```python
my_set = {"apple", "banana", "cherry"}

# 🔁 Iterating over elements
for x in my_set:
    print(x)
```

---

## 🧲 5. Join Sets
There are several ways to join two or more sets in Python. The most common methods are `union()` and `update()`.

```python
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}

# 🔗 union() returns a new set with all items from both sets
set3 = set1.union(set2)

# ⚡ update() inserts the items in set2 into set1
set1.update(set2)
```

---

## ❄️ 6. Frozenset
A `frozenset` is simply an immutable (unchangeable) version of a Python set object. Elements remain the same after creation.

```python
# 🔒 Creating a frozenset
vowels = ('a', 'e', 'i', 'o', 'u')
f_set = frozenset(vowels)

# ❌ This will raise an error because frozensets cannot be changed:
# f_set.add('z') 
```

---

## 📋 7. Common Set Methods
Here is a quick reference table of essential set methods:

| ⚙️ Method | 📝 Description |
| :--- | :--- |
| `add()` | Adds an element to the set |
| `clear()` | Removes all the elements from the set |
| `copy()` | Returns a copy of the set |
| `difference()` | Returns a set containing the difference between two or more sets |
| `intersection()` | Returns a set that is the intersection of two other sets |
| `pop()` | Removes an element from the set |

🚀 
**Happy Coding!** Practice these concepts by writing your own Sets in python.   

## 📝 License

This project is open-source and available under the [MIT License](LICENSE).
