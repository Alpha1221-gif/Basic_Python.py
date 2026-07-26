# 🐍 String Formatting with f-strings

Welcome! Python lets you inject variables directly into your text using **f-strings** (Formatted String Literals). They make your code cleaner, faster, and much easier to read! 🚀

---

## ⚡ The Basics
To create an f-string, simply put an `f` or `F` right before your opening quotation mark. Use curly brackets `{}` as placeholders for your variables.

```python
name = "Alex"
age = 22

# 📝 Example:
print(f"Hi, my name is {name} and I am {age} years old.")
# 👉 Output: Hi, my name is Alex and I am 22 years old.
```

---

## 🛠️ Types and Tricks of f-strings

Here are 4 simple ways you can use f-strings to power up your code:

### 1. 🧮 Math Expressions
You can perform quick calculations right inside the curly brackets.
```python
print(f"Next year, I will be {22 + 1} years old.")
# 👉 Output: Next year, I will be 23 years old.
```

### 2. 🔠 String Methods (Functions)
You can modify your text on the fly, like turning lowercase letters into capitals.
```python
mood = "happy"
print(f"I am feeling {mood.upper()}!")
# 👉 Output: I am feeling HAPPY!
```

### 3. 🎯 Formatting Decimals (Float Precision)
Keep long decimal numbers neat by limiting how many digits show after the dot using `:.2f` (for 2 decimal places).
```python
price = 19.995
print(f"The item costs ${price:.2f}")
# 👉 Output: The item costs $20.00
```

### 4. 🔢 Padding with Zeroes
You can force numbers to have a specific width by adding padding zeroes using `:03` (makes it 3 digits wide).
```python
rank = 7
print(f"Your ID is code_{rank:03}")
# 👉 Output: Your ID is code_007
```

---

## 💡 Quick Tips for Beginners
* ⚠️ **Quote Matching:** If your f-string uses double quotes `""`, use single quotes `''` inside the curly brackets (or vice versa) to avoid errors.
* ⚡ **Speed:** f-strings are the fastest way to format text in Python!

🚀 
**Happy Coding!** Practice these concepts by writing your own Strings variables.

## 📝 License

This project is open-source and available under the [MIT License](LICENSE).
