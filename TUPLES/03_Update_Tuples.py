# ----CODE1----
x = ("Honda","BMW","Mercedes","Nissan","Toyata")
y = list(x)
y[2] = "Audi"
x = tuple(y)
print(x) #output = ('Honda', 'BMW', 'Audi', 'Nissan', 'Toyata')

# ----CODE2----
x = ("Honda","BMW","Mercedes","Nissan","Toyata")
y = list(x)
y.append("Jaguar")
x = tuple(y)
print(x) #output = ('Honda', 'BMW', 'Mercedes', 'Nissan', 'Toyata', 'Jaguar')

# ----CODE3----
x = ("Honda","BMW","Mercedes","Nissan","Toyata")
y = ("Jaguar",)
x += y
print(x) #output = ('Honda', 'BMW', 'Mercedes', 'Nissan', 'Toyata', 'Jaguar')

# ----CODE4----
x = ("Honda","BMW","Mercedes","Nissan","Toyata")
y = list(x)
y.remove("Nissan")
x = tuple(y)
print(x) #output = ('Honda', 'BMW', 'Mercedes', 'Toyata')

# ----CODE5----
x = ("Honda","BMW","Mercedes","Nissan","Toyata")
del x
print(x) #output = NameError: name 'x' is not defined(error come means we cannot delete)

