# ----CODE1----
import re
txt = "I Love to learn Python"
a = re.search("^I.*Python$",txt)
if(a):
    print("Yes It is present!")
else:
    print("Not present")    
#output =  Yes It is present! 

# ----CODE2----
import re
txt = "I Love to learn Python"
b =  re.findall("le",txt)
print(b) #output = ['le']

# ----CODE3----
import re

txt = "I Love to learn Python"
c = re.findall("Java", txt)
print(c) #output = []

# ----CODE4----
import re

txt = "I Love to learn Python"
d = re.search("\s", txt)

print("The first white-space character is located in position:", d.start())
#output = The first white-space character is located in position: 1

# ----CODE5----
import re

txt = "I Love to learn Python"
e = re.search("java", txt)
print(e)  #output = None

# ----CODE6----
import re

txt = "I Love to learn Python"
f = re.split("\s", txt)
print(f)
#output = ['I', 'Love', 'to', 'learn', 'Python']

# ----CODE7----
import re

txt = "I Love to learn Python"
g = re.split("\s", txt, 1)
print(g)
#output = ['I', 'Love to learn Python']

# ----CODE8----
import re

txt = "I Love to learn Python"
h = re.sub("\s", "_", txt)
print(h)  #output = I_Love_to_learn_Python

# ----CODE9----
import re

txt = "I Love to learn Python"
i = re.sub("\s", "_", txt,2)
print(i)  #output = I_Love_to learn Python

# ----CODE10----
import re

txt = "I Love to learn Python"
j = re.search("th", txt)
print(j) #this will print an object
#output = <re.Match object; span=(18, 20), match='th'>

# ----CODE11----
import re

txt = "The rain in Spain"
x = re.search(r"\bS\w+", txt)
print(x.span()) #output = (12, 17)

# ----CODE12----
import re

txt = "The rain in Spain"
x = re.search(r"\bS\w+", txt)
print(x.string)  #output = The rain in Spain

# ----CODE13----
import re

txt = "The rain in Spain"
x = re.search(r"\bS\w+", txt)
print(x.group()) #output = Spain