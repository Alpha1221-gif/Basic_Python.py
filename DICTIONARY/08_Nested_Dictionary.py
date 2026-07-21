# ----CODE1----
myfamily = {
  "child1" : {
    "name" : "Alice",
    "year" : 1997
  },
  "child2" : {
    "name" : "Toretto",
    "year" : 2001
  },
  "child3" : {
    "name" : "Andrew",
    "year" : 2009
  }
}

# ----CODE2----
child1 = {
  "name" : "Alice",
  "year" : 1997
}
child2 = {
  "name" : "Toretto",
  "year" : 2001
}
child3 = {
  "name" : "Andrew",
  "year" : 2009
}

myfamily = {
  "child1" : child1,
  "child2" : child2,
  "child3" : child3
}

# ----CODE3----
print(myfamily["child2"]["name"]) #output = Toretto

# ----CODE4----
for x, obj in myfamily.items():
  print(x)

  for y in obj:
    print(y + ':', obj[y])
'''child1
name: Alice
year: 1997
child2
name: Toretto
year: 2001
child3
name: Andrew
year: 2009'''    