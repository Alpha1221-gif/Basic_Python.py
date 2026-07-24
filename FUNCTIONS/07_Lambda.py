'''lambda arguments : expression'''
# ----CODE1----
x = lambda a : a + 10
print(x(15)) #output = 25

# ----CODE2----
x = lambda a, b : a * b
print(x(5, 5)) #output = 25

# ----CODE3----
x = lambda a, b, c : a + b + c
print(x(25, 16, 12)) #output = 53

# ----CODE4----
def myfunc(n):
  return lambda a : a * n

mydoubler = myfunc(6)
print(mydoubler(11)) #output = 66

# ----CODE5----
def myfunc(n):
  return lambda a : a * n

mydoubler = myfunc(2)
mytripler = myfunc(3)

print(mydoubler(11)) #output = 22
print(mytripler(11)) #output = 33


# ----CODE6----
'''The map() function applies a function to every item in an iterable:'''
numbers = [1, 2, 3, 4, 5]
doubled = list(map(lambda x: x * 2, numbers))
print(doubled) 
#output = [2, 4, 6, 8, 10]

# ----CODE7----
'''The filter() function creates a list of items for which a function returns True:'''
numbers = [1, 2, 3, 4, 5, 6, 7, 8,9,10,11,12,13,14,15,16,17,18,19,20]
odd_numbers = list(filter(lambda x: x % 2 != 0, numbers))
print(odd_numbers)
#output = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]

# ----CODE8----
students = [("Emil", 25), ("Tobias", 29), ("Linus", 24),("Henry",21)]
sorted_students = sorted(students, key=lambda x: x[1])
print(sorted_students)
#output = [('Henry', 21), ('Linus', 24), ('Emil', 25), ('Tobias', 29)]