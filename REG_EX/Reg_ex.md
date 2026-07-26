# 🐍 Python RegEx 🔍 (Regular Expressions Guide)

Regular Expressions, or **Regex**, are powerful tools used to match, search, and manipulate text based on specific patterns. Think of it as a superpowered "Find and Replace" tool built right into your code.

---

## 🧩 Metacharacters & Core Concepts

Metacharacters are characters with a special meaning. Here is a breakdown of the essential characters used to build regex patterns:

| Character | Description | Example |
| :--- | :--- | :--- |
| `[]` | A set of characters | `"[a-m]"` |
| `\` | Signals a special sequence (can also be used to escape special characters) | `"\d"` |
| `.` | Any character (except newline character) | `"he..o"` |
| `^` | Starts with | `"^hello"` |
| `$` | Ends with | `"planet$"` |
| `*` | Zero or more occurrences | `"he.*o"` |
| `+` | One or more occurrences | `"he.+o"` |
| `?` | Zero or one occurrences | `"he.?o"` |
| `{}` | Exactly the specified number of occurrences | `"he.{2}o"` |
| `\|` | Either or | `"falls\|stays"` |
| `()` | Capture and group | *Used to isolate a section of a pattern* |

---

## 🔍 Special Sequences

A special sequence is a `\` followed by one of the characters in the list below, and has a special meaning:

| Character | Description | Example |
| :--- | :--- | :--- |
| `\A` | Returns a match if the specified characters are at the beginning of the string | `"\AThe"` |
| `\b` | Returns a match where the specified characters are at the beginning or at the end of a word<br>*(the "r" in the beginning is making sure that the string is being treated as a "raw string")* | `r"\bain"`<br>`r"ain\b"` |
| `\B` | Returns a match where the specified characters are present, but NOT at the beginning (or at the end) of a word<br>*(the "r" in the beginning is making sure that the string is being treated as a "raw string")* | `r"\Bain"`<br>`r"ain\B"` |
| `\d` | Returns a match where the string contains digits (numbers from 0-9) | `"\d"` |
| `\D` | Returns a match where the string DOES NOT contain digits | `"\D"` |
| `\s` | Returns a match where the string contains a white space character | `"\s"` |
| `\S` | Returns a match where the string DOES NOT contain a white space character | `"\S"` |
| `\w` | Returns a match where the string contains any word characters (characters from a to Z, digits from 0-9, and the underscore \_ character) | `"\w"` |
| `\W` | Returns a match where the string DOES NOT contain any word characters | `"\W"` |
| `\Z` | Returns a match if the specified characters are at the end of the string | `"Spain\Z"` |

---

## 🗂️ Sets

A set is a set of characters inside a pair of square brackets `[]` with a special meaning:

| Set | Description |
| :--- | :--- |
| `[arn]` | Returns a match where one of the specified characters (`a`, `r`, or `n`) is present |
| `[a-n]` | Returns a match for any lower case character, alphabetically between `a` and `n` |
| `[^arn]` | Returns a match for any character EXCEPT `a`, `r`, and `n` |
| `[0123]` | Returns a match where any of the specified digits (`0`, `1`, `2`, or `3`) are present |
| `[0-9]` | Returns a match for any digit between `0` and `9` |
| `[0-5][0-9]` | Returns a match for any two-digit numbers from `00` and `59` |
| `[a-zA-Z]` | Returns a match for any character alphabetically between `a` and `z`, lower case OR upper case |
| `[+]` | In sets, `+`, `*`, `.`, `\|`, `()`, `$`, `{}`, has no special meaning, so `[+]` means: return a match for any `+` character in the string |

---

## 🐍 Python RegEx Functions

In Python, you can use the built-in `re` module to work with regular expressions. The module offers a set of functions that allows us to search a string for a match:

| Function | Description |
| :--- | :--- |
| `findall` | Returns a list containing all matches |
| `search` | Returns a Match object if there is a match anywhere in the string |
| `split` | Returns a list where the string has been split at each match |
| `sub` | Replaces one or many matches with a string |

---

## 🏳️ Python RegEx Flags

You can add flags to the pattern when using regular expressions to modify how the engine interprets your text matching:

| Flag | Shorthand | Description |
| :--- | :--- | :--- |
| `re.ASCII` | `re.A` | Returns only ASCII matches |
| `re.DEBUG` | *None* | Returns debug information |
| `re.DOTALL` | `re.S` | Makes the `.` character match all characters (including newline character) |
| `re.IGNORECASE` | `re.I` | Case-insensitive matching |
| `re.MULTILINE` | `re.M` | Returns matches at the start/end of each line |
| `re.NOFLAG` | *None* | Specifies that no flag is set for this pattern |
| `re.UNICODE` | `re.U` | Returns Unicode matches. This is default from Python 3. For Python 2: use this flag to return only Unicode matches |
| `re.VERBOSE` | `re.X` | Allows whitespaces and comments inside patterns. Makes the pattern more readable |

---

## 🚀 Simple Example: Matching a Phone Number

Let's break down a pattern that matches a simple 3-digit phone prefix like `123-456`:

`\d\d\d-\d\d\d`

* `\d\d\d` looks for exactly three numbers.
* `-` looks for a literal hyphen.
* `\d\d\d` looks for three more numbers.


---

## 🛠️ Great Tools to Practice
* [Regex101](https://regex101.com) - Visualizes and explains your regex in real-time.
* [Regexr](https://regexr.com) - Great cheat sheets and interactive testing.


🚀
**Happy Coding!** Practice these concepts by writing your own Python code.

## 📝 License

This project is open-source and available under the [MIT License](LICENSE).
