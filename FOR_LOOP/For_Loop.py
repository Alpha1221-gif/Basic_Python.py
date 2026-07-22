# ----CODE1----
fruits = ["apple", "banana", "cherry"]
for i in fruits:
  print(i)
'''apple
banana
cherry'''

# ----CODE2----
for x in "apple":
  print(x)
'''a
p
p
l
e'''

# ----CODE3----
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
  if x == "banana":
    break
'''apple
banana'''
# ----CODE4----
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    break
  print(x)
#output = apple

# ----CODE5----
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    continue
  print(x)
'''apple
cherry'''

# ----CODE6----
for x in range(5):
  print(x)
'''0
1
2
3
4'''

# ----CODE7----
for x in range(1, 5):
  print(x)
'''1
2
3
4'''

# ----CODE8----
for x in range(1, 20, 3):
  print(x)
'''1
4
7
10
13
16
19'''

# ----CODE9----
for x in range(6):
  print(x)
else:
  print("Finally finished!")
'''0
1
2
3
4
5
Finally finished!'''

# ----CODE10----
adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
  for y in fruits:
    print(x, y)
'''red apple
red banana
red cherry
big apple
big banana
big cherry
tasty apple
tasty banana
tasty cherry'''
