# ----CODE1----
a = None
print(a) #output = None

# ----CODE2----
b = None
print(type(b)) #output = <class 'NoneType'>

# ----CODE3----
result = None
if result is None:
    print("No result yet")
else:
    print("Result is ready")  #output = No result yet

# ----CODE4----
result = None
if result is not None:
  print("Result is ready")
else:
  print("No result yet")  #output = No result yet


