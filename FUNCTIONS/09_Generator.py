# ----CODE1----
def my_generator():
  yield 1
  yield 2
  yield 3
  yield 4
  yield 5
  yield 6
  yield 7
  yield 8

for value in my_generator():
  print(value)
'''1
2
3
4
5
6
7
8'''  

# ----CODE2---- 
def count_up_to(n):
  count = 1
  while count <= n:
    yield count
    count += 1

for num in count_up_to(6):
  print(num)
'''1
2
3
4
5
6'''  

# ----CODE3----
def simple_gen():
  yield "Emil"
  yield "Tobias"
  yield "Linus"

gen = simple_gen()
print(next(gen))
print(next(gen))
print(next(gen))
'''Emil
Tobias
Linus'''

# ----CODE4----
def fibonacci():
  a, b = 0, 1
  while True:
    yield a
    a, b = b, a + b

gen = fibonacci()
for _ in range(10):
  print(next(gen))
'''0
1
1
2
3
5
8
13
21
34'''

# ----CODE5----
'''The send() method allows you to send a value to the generator:'''

def echo_generator():
  while True:
    received = yield
    print("Received:", received)

gen = echo_generator()
next(gen) 
gen.send("Hello") #output = Received: Hello

# ----CODE6----
'''The close() method stops the generator:'''

def my_gen():
  try:
    yield 1
    yield 2
    yield 3
  finally:
    print("Generator closed")

gen = my_gen()
print(next(gen))
gen.close()
'''1
Generator closed'''