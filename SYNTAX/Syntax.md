# Python Syntax Introduction

Welcome to Python! This guide introduces the core rules of writing Python code. 

---

## 🚀 Interactive Challenge: Fix the Code

Python relies heavily on **clean formatting** and **indentation**. Look at the broken code below and try to spot the errors based on the rules in this file.

```python
# 🚫 BROKEN CODE - CAN YOU FIX IT?
def greet_user(name)
print("Hello, " + name)
  print("Welcome to Python!")
    print("Let's learn syntax.")
```

*👇 Read the rules below to find out how to fix it!*

---

## 📋 Core Syntax Rules

### 1. Line Breaks vs. Semicolons
* Python does **not** require a semicolon (`;`) at the end of a line.
* A new line signifies the end of a statement.

```python
# True Python style
x = 5
y = 10

# C-style (Allowed but discouraged)
x = 5; y = 10;
```

### 2. Python Indentation (Crucial!)
* Python uses **indentation** (spaces) to define a block of code.
* Other languages use curly braces `{}`; Python uses whitespace.
* Standard practice is **4 spaces** per indent level.

```python
# Correct Indentation
if 5 > 2:
    print("Five is greater than two!")

# Syntax Error (No indentation)
if 5 > 2:
print("This will crash!")
```

### 3. Creating Variables
* Variables are created the moment you assign a value.
* You do **not** need to declare a data type.

```python
age = 25          # Integer
name = "Alice"    # String
is_coding = True  # Boolean
```

### 4. Writing Comments
* Use the hash character (`#`) for single-line comments.
* Use triple quotes (`"""`) for multi-line docstrings.

```python
# This is a single-line comment

"""
This is a multi-line comment.
Python ignores these text blocks.
"""
print("Comments keep code readable!")
```

---

## 🏆 Solution to the Challenge

Here is the corrected version of the broken code from the top of the file:

```python
# ✅ CORRECTED CODE
def greet_user(name):              # Added missing colon (:)
    print("Hello, " + name)        # Indented 4 spaces
    print("Welcome to Python!")    # Aligned with the previous line
    print("Let's learn syntax.")   # Aligned with the previous line
```

### Key Takeaways
1. Always add a colon (`:`) after defining functions, loops, or conditionals.
2. Keep all lines inside the same code block at the exact same indentation level.

## 📝 License

This project is open-source and available under the [MIT License](LICENSE).