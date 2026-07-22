# ----CODE1----
def my_function(name):
  print(name + " Refsnes")

my_function("Tommy") #output = Tommy Refsnes
my_function("Luther") #output = Luther Refsnes

# ----CODE2----
def my_function(name): # name is a parameter
  print("Hello", name)

my_function("Rocky") # "Emil" is an argument
#output = Hello Rocky

# ----CODE3----
def my_function(fname, lname):
  print(fname + " " + lname)

my_function("Emil", "Refsnes") #output = Emil Refsnes

# ----CODE4----
def my_function(name = "friend"):
  print("Hello", name)

my_function("Emil") #output = Hello Emil
my_function() #output = Hello friend

# ----CODE5----
def my_function(animal, name):
  print("I have a", animal)
  print("My", animal + "'s name is", name)

my_function(animal = "dog", name = "Tommy")
'''I have a dog
My dog's name is Tommy'''

# ----CODE6----
def my_function(animal, name):
  print("I have a", animal)
  print("My", animal + "'s name is", name)

my_function(name = "Tommy", animal = "dog")
'''I have a dog
My dog's name is Tommy'''

# ----CODE7----
def my_function(animal, name, age):
  print("I have a", age, "year old", animal, "named", name)

my_function("dog", name = "Buddy", age = 5)
#output = I have a 5 year old dog named Buddy

# ----CODE8----
def my_function(person):
  print("Name:", person["name"])
  print("Age:", person["age"])

my_person = {"name": "Emil", "age": 25}
my_function(my_person)
'''Name: Emil
Age: 25'''