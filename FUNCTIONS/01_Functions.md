# 🐍 Python Functions Guide

A beginner-friendly guide to understanding functions and advanced function concepts in Python.

---

# 💻 1. Python Functions
A function is a reusable block of code that only runs when it is called. You can pass data (parameters) into a function, and it can return data as a result.

### Syntax
```python
def function_name():
    # Code to execute
    pass
```

### Example
```python
def greet():
    print("Hello, World!")

# Calling the function
greet()
```

---

# 📜 2. Python Arguments
Arguments are information passed into functions. You specify them inside the parentheses when defining the function.

### Syntax
```python
def function_name(parameter1, parameter2):
    # Code using parameters
    pass
```

### Example
```python
def greet_user(name):
    print(f"Hello, {name}!")

# "Alice" is the argument passed to the function
greet_user("Alice")
```

---

# ⚙️ 3. Python *args and **kwargs
When you don't know how many arguments will be passed into your function, you use `*args` for positional arguments and `**kwargs` for keyword arguments.

### Syntax
```python
def function_name(*args, **kwargs):
    # args is treated as a tuple
    # kwargs is treated as a dictionary
    pass
```

### Example
```python
def total_sum(*args):
    return sum(args)

def user_profile(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print(total_sum(1, 2, 3, 4))
user_profile(name="Bob", age=25, city="New York")
```

---
## 🐍 Python Cheat Sheet: `*args` vs `**kwargs`

Both `*args` and `**kwargs` allow a function to accept a dynamic number of arguments. This means you do not need to know how many inputs a user will pass when you first write the function.

---

## 📊 Direct Comparison

| Feature | 📥 `*args` | 🏷️ `**kwargs` |
| :--- | :--- | :--- |
| **Full Name** | Positional Arguments | Keyword Arguments |
| **The Magic Symbol** | Single asterisk: `*` | Double asterisk: `**` |
| **Data Format** | Just values (e.g., `1, 2, "apple"`) | Named pairs (e.g., `a=1, b=2, fruit="apple"`) |
| **Python Data Type** | 📦 **Tuple** (ordered, unchangeable) | 🗂️ **Dictionary** (key-value pairs) |

---

## 📥 ->. Understanding `*args`

Use `*args` when you want to pass a list of unlabeled values to a function. Python automatically packs all these extra values into a single tuple.

```python
def sum_numbers(*args):
    print(f"📦 Inside args: {args}")  # Check the data type
    return sum(args)

# You can pass as many numbers as you want!
result = sum_numbers(10, 20, 30, 40)
print(f"✅ Result: {result}")

# Output:
# 📦 Inside args: (10, 20, 30, 40)
# ✅ Result: 100
```

---

## 🏷️ ->. Understanding `**kwargs`

Use `**kwargs` when you want to pass labeled inputs (names/keywords) to a function. Python packs these named inputs into a dictionary where the label becomes the key.

```python
def introduce_user(**kwargs):
    print(f"🗂️ Inside kwargs: {kwargs}")  # Check the data type
    for key, value in kwargs.items():
        print(f"🔹 {key}: {value}")

# Pass named parameters
introduce_user(name="Alice", age=25, city="New York")

# Output:
# 🗂️ Inside kwargs: {'name': 'Alice', 'age': 25, 'city': 'New York'}
# 🔹 name: Alice
# 🔹 age: 25
# 🔹 city: New York
```

---

## ⚠️ ->. Crucial Rules for Beginners

* **💡 The names are just a convention:** The magic comes entirely from the asterisks (`*` and `**`). You could write `*numbers` or `**user_profile`. However, standard Python formatting dictates using `args` and `kwargs` so other developers can read your code easily.
* **🛑 Order Matters:** If you combine normal arguments, `*args`, and `**kwargs` in a single function, you must place them in this exact order to avoid a `SyntaxError`:

```python
# 🏛️ The Correct Structural Order
def my_function(regular_argument, *args, **kwargs):
    pass
```
---
# 🧩 4. Python Scope
Scope determines where a variable can be seen or accessed. 
* **Local Scope:** Variables created inside a function belong only to that function.
* **Global Scope:** Variables created in the main body of the Python code can be accessed anywhere.

### Example
```python
# Global variable
x = 10 

def my_function():
    # Local variable
    y = 5  
    print(y) # Works
    print(x) # Works

my_function()
# print(y) # Error: y is not defined globally
```

---

# 🎀 5. Python Decorators
A decorator allows you to modify or extend the behavior of a function without permanently changing its code. It wraps another function.

### Syntax
```python
@decorator_name
def my_function():
    pass
```

### Example
```python
def simple_decorator(func):
    def wrapper():
        print("Before the function runs.")
        func()
        print("After the function runs.")
    return wrapper

@simple_decorator
def say_hello():
    print("Hello!")

say_hello()
```

---

# ⚡ 6. Python Lambda
A lambda function is a small, anonymous (nameless) function. It can take any number of arguments but can only have a single expression.

### Syntax
```python
lambda arguments: expression
```

### Example
```python
# A lambda function that adds 10 to a number
add_ten = lambda x: x + 10

print(add_ten(5)) # Outputs 15
```

---

# 🔁 7. Python Recursion
Recursion happens when a function calls itself. It is useful for breaking down complex problems into smaller, identical problems. It always needs a **base case** to stop looping forever.

### Example
```python
def factorial(n):
    # Base case: stop when n is 1
    if n == 1:
        return 1
    # Recursive case: function calls itself
    else:
        return n * factorial(n - 1)

print(factorial(5)) # Outputs 120 (5 * 4 * 3 * 2 * 1)
```

---

# 🔋 8. Python Generators
Generators are functions that return an iterator tool using the `yield` keyword instead of `return`. They produce items one at a time only when requested, which saves a lot of computer memory.

### Syntax
```python
def my_generator():
    yield value
```

### Example
```python
def count_up_to(max_num):
    count = 1
    while count <= max_num:
        yield count
        count += 1

counter = count_up_to(3)

print(next(counter)) # Outputs 1
print(next(counter)) # Outputs 2
print(next(counter)) # Outputs 3
```

🚀
**Happy Coding!** Practice these concepts by writing your own Functions.
## 📝 License

This project is open-source and available under the [MIT License](LICENSE).
