# ----CODE1----
print(20 > 6)
# output = True

# ----CODE2----
print(20 < 6)
# output = False

# ----CODE3----
print(20 == 6)
# output = False

# ----CODE4----
x = 100
y = 67

if x > y:
  print("x is greater than y")
else:
  print("x is not greater than y")
# output = x is greater than y

# ----CODE5----
x = 67
y = 100

if x > y:
  print("x is greater than y")
else:
  print("x is not greater than y")
# output = x is not greater than y

# ----CODE6----
print(bool("Write")) # output = True
print(bool(30)) # output = True

# ----CODE7----
bool("abc")
bool(123)
bool(["apple", "cherry", "banana"])
# output = True

# ----CODE8----
bool(False)
bool(None)
bool(0)
bool("")
bool(())
bool([])
bool({})
# output = False
