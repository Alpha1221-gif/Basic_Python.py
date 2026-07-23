# ----CODE1----
def my_function(*kids):
  print("The youngest child is " + kids[2])
my_function("Emil", "Tobias", "Linus")
#output = The youngest child is Linus

# ----CODE2----
def my_function(*args):
  print("Type:", type(args))
  print("First argument:", args[0])
  print("Second argument:", args[1])
  print("All arguments:", args)
my_function("Emil", "Tobias", "Linus")
'''Type: <class 'tuple'>
First argument: Emil
Second argument: Tobias
All arguments: ('Emil', 'Tobias', 'Linus')'''

# ----CODE3----
def my_function(greeting, *names):
  for name in names:
    print(greeting, name)
my_function("Hello", "Emil", "Tobias", "Linus")
'''Hello Emil
Hello Tobias
Hello Linus'''

# ----CODE4----
def my_function(*numbers):
  total = 0
  for num in numbers:
    total += num
  return total
print(my_function(1, 2, 3)) #output = 6
print(my_function(10, 20, 30, 40)) #output = 100
print(my_function(5)) #output = 5

# ----CODE5----
def my_function(**kid):
  print("His last name is " + kid["lname"])
my_function(fname = "Tobias", lname = "Refsnes")
#output = His last name is Refsnes

# ----CODE6----
def my_function(**myvar):
  print("Type:", type(myvar))
  print("Name:", myvar["name"])
  print("Age:", myvar["age"])
  print("All data:", myvar)
my_function(name = "Tobias", age = 30, city = "Bergen")
'''Type: <class 'dict'>
Name: Tobias
Age: 30
All data: {'name': 'Tobias', 'age': 30, 'city': 'Bergen'}'''

# ----CODE7----
def my_function(title, *args, **kwargs):
  print("Title:", title)
  print("Positional arguments:", args)
  print("Keyword arguments:", kwargs)
my_function("User Info", "Emil", "Tobias", age = 25, city = "Oslo")
'''Title: User Info
Positional arguments: ('Emil', 'Tobias')
Keyword arguments: {'age': 25, 'city': 'Oslo'}'''

# ----CODE8----
def my_function(a, b, c):
  return a + b + c
numbers = [6, 7, 8]
result = my_function(*numbers) 
print(result) #output = 21