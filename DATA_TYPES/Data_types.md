# 🐍 Python Data Types for Beginners

Data types tell Python what kind of value a variable holds. Python detects these automatically!

---

## 📝 1. Text Type (Strings)
Used for text, words, or sentences. Always wrap them in quotes.
* **Code Name:** `str`
* **Visual Key:** `" "` or `' '`
* **Example:** `user_name = "Alice"`

---

## 🔢 2. Numeric Types
Used for math, counting, and calculations.

### Whole Numbers
* **Code Name:** `int` (Integer)
* **Example:** `age = 25`

### Decimal Numbers
* **Code Name:** `float` (Floating point)
* **Example:** `price = 19.99`

---

## ⚖️ 3. Boolean Type
Used for logical conditions, true/false switches, and decision making.
* **Code Name:** `bool`
* **Example:** `is_online = True`
* **Important:** Always capitalize **True** and **False**.

---

## 📋 4. Sequence Types
Used to store collections of multiple items in a single variable.

### Lists (Changeable)
* **Code Name:** `list`
* **Visual Key:** `[ ]`
* **Example:** `shopping_list = ["apple", "banana", "milk"]`

### Tuples (Permanent / Cannot be changed)
* **Code Name:** `tuple`
* **Visual Key:** `( )`
* **Example:** `screen_resolution = (1920, 1080)`

---

## 🗺️ 5. Mapping Type (Dictionaries)
Stores data in **key: value** pairs, just like looking up a word definition.
* **Code Name:** `dict`
* **Visual Key:** `{ }`
* **Example:** `car_info = {"brand": "Ford", "year": 2024}`

---

## 🔍 How to Check a Data Type
You can use the built-in `type()` function to ask Python what data type a variable is.

```python
# Copy and run this in your editor
my_number = 100
print(type(my_number))  # Outputs: <class 'int'>
##'''
📝 License

This project is open-source and available under the [MIT License](LICENSE)
