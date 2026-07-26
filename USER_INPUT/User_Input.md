# 🐍 Understanding User Input in Python

As a beginner, getting information from a user makes your programs interactive and fun. Here is a simple guide to handling user input.

---

## 📥 1. The `input()` Function
The basic way to get text from a user is the `input()` function. 

### ⚙️ Syntax
```python
variable_name = input("Prompt message for the user: ")
```

### 💻 Example
```python
# Asking for a name
name = input("Enter your name: ")
print("Hello, " + name + "!")
```

---

## 🔢 2. Reading Numbers (Integer and Float)
By default, the `input()` function saves everything as **text** (a string). If you want to do math with the input, you must convert it.

### 📐 Converting to a Whole Number (Integer)
Use `int()` around the input function.

```python
# Asking for age
age = int(input("Enter your age: "))
next_year = age + 1
print("Next year you will be:", next_year)
```

### 🏷️ Converting to a Decimal Number (Float)
Use `float()` around the input function.

```python
# Asking for price
price = float(input("Enter the item price: "))
discounted_price = price * 0.90
print("Price after 10% discount:", discounted_price)
```

---

## 🛡️ 3. Handling Errors Safely
Sometimes users type letters when you expect a number. This causes your program to crash. You can prevent this by using `try` and `except`.

### 🦺 Example
```python
try:
    number = int(input("Type a whole number: "))
    print("Great! You typed:", number)
except ValueError:
    print("That was not a valid whole number!")
```

---

## 📋 Summary Checklist
* 💬 `input()` always captures text data.
* 🧩 Use `int(input())` for whole numbers.
* 💸 Use `float(input())` for decimal numbers.


