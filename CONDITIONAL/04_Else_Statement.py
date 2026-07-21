# ----CODE1----
a = 200
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
else:
  print("a is greater than b")
#output =  a is greater than b

# ----CODE2----
a = 100
b = 67
if b > a:
  print("b is greater than a")
else:
  print("b is not greater than a")
  #output = b is not greater than a

# ----CODE3----  
temperature = 26
if temperature > 30:
  print("It's hot outside!")
elif temperature > 20:
  print("It's warm outside")
elif temperature > 10:
  print("It's cool outside")
else:
  print("It's cold outside!")
 #output = It's warm outside

# ----CODE4----
username = "Frank"
if len(username) > 0:
  print(f"Welcome, {username}!")
else:
  print("Error: Username cannot be empty")
  #output = Welcome, Frank!