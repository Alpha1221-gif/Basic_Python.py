# 🐍  Understanding Variables in Python

A variable is a container used to store data values in a computer program. Think of a variable as a labeled storage box. You put data inside the box, label it with a name, and use that name whenever you need the data later.

---

## 1. Creating a Variable
In Python, you do not need to declare or command a variable into existence before using it. You create one the very moment you assign a value to it using the **`=`** assignment operator.

```python
# 'age' is the variable name, and 25 is the value stored inside it
age = 25

# 'name' is the variable name, and "Alice" is the text stored inside it
name = "Alice"

print(age)
print(name)
```

---

## 2. Dynamic Typing
Python is **dynamically typed**. This means Python automatically detects what kind of data you are storing, so you do not have to specify the type yourself. 

You can also change the type of data stored in a variable at any time by simply giving it a new value.

```python
x = 10       # Python knows x is an integer (whole number)
x = "Hello"  # Now x is a string (text)
```

---

## 3. Basic Data Types for Beginners
Variables can store different kinds of data. Here are the four primary types you will use as a beginner:

| Data Type | Description | Example Code |
| :--- | :--- | :--- |
| **String (`str`)** | Text wrapped in quotes | `city = "New York"` |
| **Integer (`int`)** | Whole numbers without decimals | `items = 5` |
| **Float (`float`)** | Numbers with a decimal point | `price = 19.99` |
| **Boolean (`bool`)** | Logical values: either `True` or `False` | `is_logged_in = True` |

### Checking Data Types
You can use the built-in `type()` function to check what kind of data a variable holds:

```python
score = 94.5
print(type(score))  # Output: <class 'float'>
```

---

## 4. Rules for Naming Variables
Python has strict rules about what names you can give your variables:

* **Allowed characters**: Use only letters, numbers, and underscores (`a-z`, `A-Z`, `0-9`, `_`).
* **Start rule**: Names must start with a letter or an underscore. They **cannot** start with a number.
* **Case sensitivity**: Python is case-sensitive. `age`, `Age`, and `AGE` are treated as three separate variables.
* **No Keywords**: You cannot use Python's reserved words (like `if`, `for`, `print`, or `while`) as variable names.

### Examples of Names
* ✅ **Valid**: `user_name`, `total2`, `_temp_value`
* ❌ **Invalid**: `2user` (starts with a number), `user-name` (contains a hyphen), `user name` (contains spaces)

### Best Practice: Snake Case
When making variable names with multiple words, separate the words with an underscore. This style is called **snake_case** and makes your code much easier to read.

```python
# Good readability
player_high_score = 5000 
```
## 📝 License

This project is open-source and available under the [MIT License](LICENSE).
