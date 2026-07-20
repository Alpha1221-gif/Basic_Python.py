# ----CODE1---- #
list1 = ["mango", "papaya", "peach"]
list2 = list1.copy()
print(list2) #output = ['apple', 'banana', 'cherry']

# ----CODE2---- #
list1 = ["mango", "papaya", "peach"]
list2 = list(list1)
print(list2) #output = ['mango', 'papaya', 'peach']

# ----CODE3---- #
list1 = ["mango", "papaya", "peach"]
list2 = list1[:]
print(list2) #output = ['mango', 'papaya', 'peach']