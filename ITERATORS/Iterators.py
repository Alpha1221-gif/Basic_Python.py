# ----CODE1----
mytuple = ("apple", "banana", "cherry")
myit = iter(mytuple)

print(next(myit)) #output = apple
print(next(myit)) #output = banana
print(next(myit)) #output = cherry

# ----CODE2----
mystr = "cherry"
myit = iter(mystr)

print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
'''c
h
e
r
r
y'''

# ----CODE3----
mytuple = ("apple", "banana", "cherry")

for x in mytuple:
  print(x) 
'''apple
banana
cherry'''

# ----CODE4----
mystr = "cheery"

for x in mystr:
  print(x)
'''c
h
e
r
r
y'''

# ----CODE5----
class MyNumbers:
  def __iter__(self):
    self.a = 1
    return self

  def __next__(self):
    x = self.a
    self.a += 1
    return x

myclass = MyNumbers()
myiter = iter(myclass)

print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
'''1
2
3
4'''

# ----CODE6----
class MyNumbers:
  def __iter__(self):
    self.a = 1
    return self

  def __next__(self):
    if self.a <= 10:
      x = self.a
      self.a += 1
      return x
    else:
      raise StopIteration

myclass = MyNumbers()
myiter = iter(myclass)

for x in myiter:
  print(x)
'''1
2
3
4
5
6
7
8
9
10'''  