# ----CODE1----
def countdown(n):
  if n <= 0:
    print("Blast!")
  else:
    print(n)
    countdown(n - 1)

countdown(5)
'''5
4
3
2
1
Blast!'''

# ----CODE2----
def factorial(n):
  # Base case
  if n == 0 or n == 1:
    return 1
  # Recursive case
  else:
    return n * factorial(n - 1)

print(factorial(6)) #output = 720

# ----CODE3----
def sum_list(numbers):
  if len(numbers) == 0:
    return 0
  else:
    return numbers[0] + sum_list(numbers[1:])

my_list = [1, 2, 3, 4, 5, 6, 7]
print(sum_list(my_list))  #output = 28

# ----CODE4----
def find_max(numbers):
  if len(numbers) == 1:
    return numbers[0]
  else:
    max_of_rest = find_max(numbers[1:])
    return numbers[0] if numbers[0] > max_of_rest else max_of_rest

my_list = [3, 7, 2, 9, 1]
print(find_max(my_list)) #output = 9