# 🐍 🔄 Learning Python While Loops

Loops let you repeat a block of code over and over again. A `while` loop keeps running as long as a specific condition stays `True`. 

---

## 💡 What is a While Loop?

Think of a `while` loop like an alarm clock snooze button. It will keep ringing *while* you are still asleep. The moment you wake up, it stops!

### 📝 Basic Syntax

```python
while condition_is_true:
    # Code to run repeatedly
    # Change the condition here so the loop can stop
```

---

## 🚀 Simple Example: Counting to 3

Here is how you print numbers from 1 to 3 using a `while` loop.

```python
# 1. Start with a starting number
count = 1

# 2. Set the condition
while count <= 3:
    print(count)
    
    # 3. Change the count so it doesn't run forever!
    count = count + 1 
```

### 🧠 How Python reads this code:
1. Is `1 <= 3`? Yes! Prints `1`. Count becomes `2`.
2. Is `2 <= 3`? Yes! Prints `2`. Count becomes `3`.
3. Is `3 <= 3`? Yes! Prints `3`. Count becomes `4`.
4. Is `4 <= 3`? No! The loop stops.

---

## 🚨 The Infinite Loop Danger

If you forget to change your variable inside the loop, your code will run forever and crash your computer!

```python
# ❌ BAD CODE EXAMPLE:
count = 1
while count < 5:
    print("Help! I am stuck!")
    # Missing: count = count + 1
```
*Tip: If your code gets stuck running forever, press `Ctrl + C` in your terminal to force it to stop.*

---

## 🛠️ Two Secret Weapons: Break and Continue

You can control loops using two special keywords: `break` and `continue`.

### 🛑 1. Break (Stop Everything)
Use `break` to exit a loop immediately, even if the condition is still true.

```python
while True:
    answer = input("Type 'exit' to quit: ")
    if answer == 'exit':
        break # This exits the loop instantly!
```

### ⏭️ 2. Continue (Skip to the Next Turn)
Use `continue` to skip the rest of the current turn and jump straight back to the top of the loop.

```python
number = 0
while number < 5:
    number += 1
    if number == 3:
        continue # Skips printing the number 3!
    print(number)
```

---

## 🔑 Key Points to Remember

1. **Need a starting point:** Always create your tracking variable *before* the loop starts.
2. **Don't forget to update:** Always change your variable inside the loop to avoid infinite loops.
3. **Indentation matters:** All code inside the loop must be pushed to the right by 4 spaces.

🚀 **Happy Coding!** Feel free to clone this repository and practice these methods.


## 📝 License

This project is open-source and available under the [MIT License](LICENSE).
   
