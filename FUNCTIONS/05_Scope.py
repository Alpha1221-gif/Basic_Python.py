# ----CODE1----
def myfunc():
  x = 27
  print(x)
myfunc() #output = 27

# ----CODE2---- (Local Scope)
def myfunc():
  x = 300
  def myinnerfunc():
    print(x)
  myinnerfunc()
myfunc()  #output = 300

# ----CODE3---- (Global Scope)
x = 333
def myfunc():
  print(x)
myfunc()  #output = 333
print(x)  #output = 333

# ----CODE4---- (Local and Global Scope)
x = 300

def myfunc():
  x = 200
  print(x)
myfunc()  #output = 200
print(x)  #output = 300

# ----CODE5----
def myfunc():
  global x
  x = 300

myfunc()
print(x) #output = 300

# ----CODE6----
x = 300

def myfunc():
  global x
  x = 200
myfunc()
print(x) #output = 200

# ----CODE7---- (Non local)
def myfunc1():
  x = "Jane"
  def myfunc2():
    nonlocal x
    x = "hello"
  myfunc2()
  return x

print(myfunc1()) #output = hello


'''Python follows the LEGB rule when looking up variable names, and searches for them in this order:

-> Local - Inside the current function
-> Enclosing - Inside enclosing functions (from inner to outer)
-> Global - At the top level of the module
-> Built-in - In Python's built-in namespace'''