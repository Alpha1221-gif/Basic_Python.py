# 🐍 Python Date Methods for Beginners

Welcome! Working with dates and times in Python is very straightforward. Python uses a built-in tool called `datetime` to handle everything like a digital calendar.

---

## 📅 1. Getting Started

To work with dates, you must first bring Python's date tool into your code using the `import` command.

```python
# 🔓 Unlock the date and time tools
import datetime
```

---

## 🕒 2. Finding Today's Date and Time

You can easily grab the exact current moment using `now()`.

```python
# ⏱️ Get the current exact date and time
right_now = datetime.datetime.now()
print(right_now)  # Example output: 2026-07-25 17:11:00
```

---

## 🔍 3. Essential Methods (Extracting Data)

Once you have a date object, you can pull out individual pieces of information using these simple properties:

* **`.year`**: Extracts the 4-digit year (e.g., `2026`).
* **`.month`**: Extracts the month number (`1` for January, `12` for December).
* **`.day`**: Extracts the day of the month (`1` to `31`).
* **`.hour`**: Extracts the hour (`0` to `23`).
* **`.minute`**: Extracts the minutes (`0` to `59`).

### 📝 Example:
```python
import datetime
today = datetime.datetime.now()

print(today.year)   # Output: 2026
print(today.month)  # Output: 7
print(today.day)    # Output: 25
```

---

## 🛠️ 4. Creating a Custom Date

If you want to look at a specific calendar day in history or the future, you can build it yourself:

```python
# 🏗️ Create: Year, Month, Day
custom_date = datetime.datetime(2028, 12, 25)
print(custom_date)  # Output: 2028-12-25 00:00:00
```
---
🚀
**Happy Coding!** Practice these concepts by writing your own Python code.

## 📝 License

This project is open-source and available under the [MIT License](LICENSE).
