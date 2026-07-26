# ----CODE1----
txt = f"The price is 34 dollar"
print(txt)  #output = The price is 34 dollar

# ----CODE2----
value = 34
x = f"The price is {value} dollar"
print(x) #output = The price is 34 dollar

# ----CODE3----
value = 34
y = f"The price is {value:.2f} dollar"#Display the price with 2 decimals:
print(y)  #output = The price is 34.00 dollar

# ----CODE4----
z = f"The price is {34:.2f} dollar"
print(z)  #output = The price is 34.00 dollar

# ----CODE5----
txt = f"The price is {29 * 59} dollars"
print(txt) #output = The price is 1711 dollars

# ----CODE6----
price = 39
txt = f"It is very {'Expensive' if price>50 else 'Cheap'}"

print(txt) 
#output = It is very Cheap

# ----CODE7----
fruit = "banana"
a = f"I love {fruit.upper()}"
print(a) #output = I love BANANA

# ----CODE8----
def myconverter(x):
    return x*3.045
txt = f"The plane is flying at a {myconverter(30000)} meter altitude"
print(txt)
#output = The plane is flying at a 91350.0 meter altitude

# ----CODE9----
price = 15000
z = f"The price is {price:,} dollars"
print(z)
#output = The price is 15,000 dollars

# ----CODE10----
price = 59
txt = "The price is {} dollar"
print(txt.format(price)) #output = The price is 59 dollar

# ----CODE11----
quantity = 3
no = 334
price = 100
g = "I want {} pieces of item number {} for {:.2f} dollars."
print(g.format(quantity,no,price))
#output = I want 3 pieces of item number 334 for 100.00 dollars.

# ----CODE12----
quantity = 3
no = 334
price = 100
g = "I want {0} pieces of item number {1} for {2:.2f} dollars."
print(g.format(quantity,no,price))
#output = I want 3 pieces of item number 334 for 100.00 dollars.

# ----CODE13----
age = 36
name = "John"
txt = "His name is {1}. {1} is {0} years old."
print(txt.format(age, name))
#output = His name is John. John is 36 years old.