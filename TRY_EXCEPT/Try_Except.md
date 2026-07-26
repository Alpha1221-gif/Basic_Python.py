# 🐍 Python Try Except 🛠️ (Exception Handling Guide)

Exception handling allows your program to deal with unexpected errors gracefully instead of crashing unexpectedly. Think of it as a safety net for your code.

---

## 🧩 The Core Blocks

Here is how the main blocks work together to catch and handle errors:

| Block | Description |
| :--- | :--- |
| `try` | Lets you test a block of code for errors. |
| `except` | Lets you handle the error. |
| `else` | Lets you execute code when there is no error. |
| `finally` | Lets you execute code, regardless of the result of the try- and except blocks. |

---

## 🚀 The `raise` Keyword

As a Python developer, you can choose to throw an exception if a specific condition occurs. To do this, use the **`raise`** keyword.

* You can define what kind of error to raise, and the text to print to the user.
* It forces a specific exception to occur manually even if your code didn't naturally fail.

---

## 💻 Quick Code Templates

### 1. Basic Try-Except Example
```python
try:
    print(x)  # This will cause an error because x is not defined
except NameError:
    print("Variable x is not defined!")
except:
    print("Something else went wrong!")
```

### 2. Full Flow (Try, Except, Else, Finally)
```python
try:
    print("Hello World")
except:
    print("Something went wrong")
else:
    print("Nothing went wrong!")  # Runs because try block succeeded
finally:
    print("The 'try except' is finished")  # Always runs
```

### 3. Raising an Exception Manually
```python
x = -1

if x < 0:
    raise Exception("Sorry, no numbers below zero allowed!")
```

---

## 🛠️ Common Python Exceptions to Know

| Exception | When it happens |
| :--- | :--- |
| `TypeError` | An operation is applied to an object of inappropriate type (e.g., `5 + "apple"`) |
| `ValueError` | A function receives an argument of the right type but inappropriate value |
| `IndexError` | Trying to access a list index that does not exist |
| `KeyError` | Looking for a dictionary key that cannot be found |


🚀
**Happy Coding!** Practice these concepts by writing your own Python code.

## 📝 License

This project is open-source and available under the [MIT License](LICENSE).
