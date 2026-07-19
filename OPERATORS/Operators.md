# 🐍 Python Operators: The Complete Blueprint

Operators are special symbols in Python used to perform operations on variables and values. They are the gears that drive logic, math, and data manipulation in your code.

---

## 1. 🧮 Arithmetic Operators
Used with numeric values to perform common mathematical operations.

* `+` **Addition**: Adds values (`5 + 3 = 8`)
* `-` **Subtraction**: Subtracts values (`5 - 3 = 2`)
* `*` **Multiplication**: Multiplies values (`5 * 3 = 15`)
* `/` **Division**: Divides values, always returns a float (`5 / 2 = 2.5`)
* `%` **Modulus**: Returns the remainder (`5 % 2 = 1`)
* `**` **Exponentiation**: Power calculation (`5 ** 2 = 25`)
* `//` **Floor Division**: Divides and rounds down to nearest whole number (`5 // 2 = 2`)

```python
x = 10
y = 3
print(x % y)   # Output: 1
print(x // y)  # Output: 3
```

---

## 2. 📝 Assignment Operators
Used to assign values to variables. Shortcut operators combine arithmetic and assignment.

* `=` **Assign**: `x = 5`
* `+=` **Add & Assign**: `x += 3` (Same as `x = x + 3`)
* `-=` **Subtract & Assign**: `x -= 3` (Same as `x = x - 3`)
* `*=` **Multiply & Assign**: `x *= 3` (Same as `x = x * 3`)
* `/=` **Divide & Assign**: `x /= 3` (Same as `x = x / 3`)

```python
score = 10
score += 5  # Adds 5 to score
print(score)  # Output: 15
```

---

## 3. ⚖️ Comparison Operators
Used to compare two values. They always return a Boolean value (`True` or `False`).

* `==` **Equal to**: `x == y`
* `!=` **Not equal to**: `x != y`
* `>` **Greater than**: `x > y`
* `<` **Less than**: `x < y`
* `>=` **Greater than or equal to**: `x >= y`
* `<=` **Less than or equal to**: `x <= y`

```python
print(10 > 20)   # Output: False
print(5 != 3)    # Output: True
```

---

## 4. 🧠 Logical Operators
Used to combine conditional statements.

* `and` **Returns True** if both statements are true (`x < 5 and x < 10`)
* `or` **Returns True** if at least one statement is true (`x < 5 or x < 4`)
* `not` **Reverse the result**, returns False if the result is true (`not(x < 5)`)

```python
age = 25
has_license = True

if age >= 18 and has_license:
    print("You can drive! 🚗")
```

---

## 5. 🔍 Identity Operators
Used to compare objects, not if they are equal, but if they are actually the exact same object in memory.

* `is` **Returns True** if both variables point to the same object
* `is not` **Returns True** if both variables point to different objects

```python
list_a = [1, 2, 3]
list_b = [1, 2, 3]
list_c = list_a

print(list_a == list_b)  # Output: True (Values are identical)
print(list_a is list_b)  # Output: False (Different memory locations)
print(list_a is list_c)  # Output: True (Same memory location)
```

---

## 6. 🎟️ Membership Operators
Used to test if a sequence (like a string, list, or tuple) is present in an object.

* `in` **Returns True** if the sequence is found in the object
* `not in` **Returns True** if the sequence is not found in the object

```python
fruits = ["apple", "banana", "cherry"]

print("banana" in fruits)      # Output: True
print("orange" not in fruits)  # Output: True
```

---

## 7. ⚙️ Bitwise Operators
Used to perform bit-level operations directly on binary numbers.

* `&` **AND**: Sets each bit to 1 if both bits are 1
* `|` **OR**: Sets each bit to 1 if one of two bits is 1
* `^` **XOR**: Sets each bit to 1 if only one of two bits is 1
* `~` **NOT**: Inverts all the bits
* `<<` **Zero fill left shift**: Shift left by pushing zeros in from the right
* `>>` **Signed right shift**: Shift right by pushing copies of the leftmost bit in from the left

```python
# Binary: 5 = 0101, 3 = 0011
print(5 & 3)  # Output: 1 (Binary: 0001)
print(5 | 3)  # Output: 7 (Binary: 0111)
```

---

## 8. 🔀 Ternary Operator (Conditional Expressions)
Python does not have a formal `? :` operator like C++ or Java. Instead, it uses a single-line `if-else` expression.

* **Syntax**: `value_if_true if condition else value_if_false`

```python
status = "Adult" if age >= 18 else "Minor"
print(status)
```

---

## 9. 🏅 Operator Precedence
Precedence determines the order in which operations are executed. Operators at the top of this list happen first. You can always use **parentheses `()`** to force Python to evaluate an expression first.

| Precedence | Operator | Description |
| :--- | :--- | :--- |
| **1 (Highest)** | `()` | Parentheses |
| **2** | `**` | Exponentiation |
| **3** | `+x`, `-x`, `~x` | Unary plus, minus, and bitwise NOT |
| **4** | `*`, `/`, `//`, `%` | Multiplication, division, floor division, modulus |
| **5** | `+`, `-` | Addition and subtraction |
| **6** | `<<`, `>>` | Bitwise shift operators |
| **7** | `&` | Bitwise AND |
| **8** | `^` | Bitwise XOR |
| **9** | `\|` | Bitwise OR |
| **10** | `==`, `!=`, `>`, `>=`, `<`, `<=`, `is`, `is not`, `in`, `not in` | Comparisons, Identity, and Membership |
| **11** | `not` | Logical NOT |
| **12** | `and` | Logical AND |
| **13 (Lowest)**| `or` | Logical OR |

```python
# Example of precedence
result = 10 + 5 * 2  # Multiplication happens first (5 * 2 = 10), then addition
print(result)        # Output: 20

forced_result = (10 + 5) * 2  # Parentheses happen first
print(forced_result)          # Output: 30
```

## 📝 License

This project is open-source and available under the [MIT License](LICENSE).
