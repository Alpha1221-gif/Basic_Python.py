# ----CODE1----
def hello_call():
  print("Hello from a function")

hello_call() #output = Hello from a function
hello_call() #output = Hello from a function

# ----CODE2----
def fahrenheit_to_celsius(fahrenheit):
  return (fahrenheit - 32) * 5 / 9

print(fahrenheit_to_celsius(68)) #output = 20.0
print(fahrenheit_to_celsius(91)) #output = 32.77777777777778
print(fahrenheit_to_celsius(87)) #output = 30.555555555555557

# ----CODE3----
def hello_msg():
  return "Hello from a function"
print(hello_msg()) #output = Hello from a function