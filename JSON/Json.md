# 📝 Learning JSON as a Beginner

JSON stands for **J**ava**S**cript **O**bject **N**otation. It is a simple text format used to store and share data. Think of it like a digital shopping list or a profile card that computers can easily read.

---

## 🚀 Why Use JSON?
* 👁️ **Easy to read:** Humans can understand it at a glance.
* ⚡ **Lightweight:** It uses very little text, making it fast to send over the internet.
* 🌍 **Universal:** Almost every programming language understands it.

---

## 📏 The Basic Rules (Syntax)
To make a valid JSON file, you must follow these rules:
1. 🔑 **Data is in pairs:** It uses ` "key": "value" ` pairs.
2. 📍 **Commas separate data:** Use a comma `,` to separate multiple pieces of data.
3. 📦 **Curly braces hold objects:** Curly braces `{}` surround a single item or profile.
4. 📜 **Square brackets hold lists:** Square brackets `[]` surround a list of items.
5. 🔤 **Always use double quotes:** Keys and text values *must* use double quotes `"`. Single quotes `'` will cause an error.

---

## 🗂️ JSON Data Types
JSON can store different types of information:
* ✍️ **String (Text):** `"John Doe"`
* 🔢 **Number:** `25` or `98.6`
* ⚖️ **Boolean (True/False):** `true` or `false`
* 🕳️ **Null (Empty):** `null`

---

## 💻 Simple Example
Here is a JSON profile of a student:

```json
{
  "name": "Alex",
  "age": 20,
  "isStudent": true,
  "hobbies": ["reading", "gaming", "coding"]
}
```

### 🔍 Breaking down the example:
* `"name"` is the key, and `"Alex"` is the text value.
* `"age"` has a number value, so it does not need quotes.
* `"isStudent"` uses a true/false value.
* `"hobbies"` uses square brackets because it is a list of multiple things.
