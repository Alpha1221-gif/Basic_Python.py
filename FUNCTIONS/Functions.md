# 🐍 Python Functions Guide

A beginner-friendly guide to understanding functions and advanced function concepts in Python.

---

## 💻 1. Python Functions
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

## 📜 2. Python Arguments
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

## ⚙️ 3. Python *args and **kwargs
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

## 🧩 4. Python Scope
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

## 🎀 5. Python Decorators
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

## ⚡ 6. Python Lambda
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

## 🔁 7. Python Recursion
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

## 🔋 8. Python Generators
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
