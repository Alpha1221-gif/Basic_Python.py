# Learning Python Match Case Statements 🐍

If you know how `if` statements work, you are ready to learn about `match` statements! 

Python added this feature in version 3.10. It is a cleaner way to handle multiple conditions instead of writing a long chain of `if-elif-else` statements.

---

## 💡 What is Match Case?

Think of a `match` statement like a switchboard. You look at a single variable, and Python checks a list of "cases" to see which one fits perfectly. 

### Basic Syntax

```python
match variable_to_check:
    case value_1:
        # Code to run if variable equals value_1
    case value_2:
        # Code to run if variable equals value_2
    case _:
        # Code to run if nothing else matches (the backup plan!)
```

*Note: The underscore `_` acts as a wildcard. It means "anything else."*

---

## 🚀 Simple Example: Choosing a Snack

Imagine you want to print a message based on your favorite fruit.

### The Old Way (If-Elif-Else)
```python
fruit = "apple"

if fruit == "apple":
    print("Apples are crunchy!")
elif fruit == "banana":
    print("Bananas are sweet!")
else:
    print("I do not know that fruit.")
```

### The New Way (Match-Case)
```python
fruit = "apple"

match fruit:
    case "apple":
        print("Apples are crunchy!")
    case "banana":
        print("Bananas are sweet!")
    case _:
        print("I do not know that fruit.")
```

---

## 👥 Combining Multiple Options

You can use the pipe symbol `|` to mean **"OR"** if you want multiple choices to do the same thing.

```python
day = "Saturday"

match day:
    case "Saturday" | "Sunday":
        print("It is the weekend! 🎉")
    case _:
        print("Time to work! 💼")
```

---

## 🔑 Key Points to Remember

1. **No indentation errors:** Every `case` must line up perfectly under the `match` word.
2. **First match wins:** Python looks from top to bottom. It runs the *first* matching case it finds and skips the rest.
3. **The `_` is your safety net:** Always include the `case _:` at the bottom so your code does not crash if an unexpected value comes up.

🚀 **Happy Coding!** Feel free to clone this repository and practice these methods.


## 📝 License

This project is open-source and available under the [MIT License](LICENSE).
