# ----CODE1----
x = "amazing"

def myfunc():
  print("Python is " + x)

myfunc() #output =  Python is amazing

# ----CODE2----
x = "amazing"

def myfunc():
  x = "fantastic"
  print("Python is " + x) #output = Python is fantastic

myfunc()

print("Python is " + x) #output = Python is amazing

# ----CODE3----
def myfunc():
  global x
  x = "amazing"

myfunc()

print("Python is " + x) #output = Python is amazing

# ----CODE4----
x = "awesome"

def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x) #output = Python is fantastic