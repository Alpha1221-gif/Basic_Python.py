# 🐍 If...Else: Ultimate Beginner's Guide 🔀🛣️

Welcome to the beginner's guide to Python conditional statements! Decision-making structures require that the programmer specifies one or more conditions to be evaluated or tested by the program.

> 💡 **Tip:** Python relies on indentation (whitespace at the beginning of a line) to define scope in the code. Other programming languages often use curly brackets `{}` for this purpose.

---

## 🔍 1. Python If
An `if` statement is written by using the `if` keyword. It executes a block of code only if a specified condition is true.

```python
a = 33
b = 200

if b > a:
    print("b is greater than a") # Output: b is greater than a
```

---

## 🔄 2. Python Elif
The `elif` keyword is Python's way of saying "if the previous conditions were not true, then try this condition".

```python
a = 33
b = 33

if b > a:
    print("b is greater than a")
elif a == b:
    print("a and b are equal") # Output: a and b are equal
```

---

## ❌ 3. Python Else
The `else` keyword catches anything which isn't caught by the preceding conditions.

```python
a = 200
b = 33

if b > a:
    print("b is greater than a")
elif a == b:
    print("a and b are equal")
else:
    print("a is greater than b") # Output: a is greater than b
```

---

## ⚡ 4. Shorthand If
If you have only one statement to execute, you can put it on the same line as the `if` statement. You can also write short `if...else` statements on a single line (Ternary Operators).

```python
a = 200
b = 33

# Short Hand If
if a > b: print("a is greater than b")

# Short Hand If...Else
print("A") if a > b else print("B")
```

---

## 🔀 5. Logical Operators
Logical operators (`and`, `or`, `not`) are used to combine conditional statements.

```python
a = 200
b = 33
c = 500

# The 'and' operator
if a > b and c > a:
    print("Both conditions are True")

# The 'or' operator
if a > b or a > c:
    print("At least one condition is True")
```

---

## 🪆 6. Nested If
You can have `if` statements inside `if` statements, this is called *nested* `if` statements.

```python
x = 41

if x > 10:
    print("Above ten,")
    if x > 20:
        print("and also above 20!")
    else:
        print("but not above 20.")
```

---

## 🛑 7. Pass Statement
`if` statements cannot be empty, but if you for some reason have an `if` statement with no content, put in the `pass` statement to avoid getting an error.

```python
a = 33
b = 200

if b > a:
    pass # Code compiles without errors
```

---

🚀 **Happy Coding!** Try modifying the values of `a` and `b` to see how different blocks run.

## 📝 License

This project is open-source and available under the [MIT License](LICENSE).
