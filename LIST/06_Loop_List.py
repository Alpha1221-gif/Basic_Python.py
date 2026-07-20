# ----CODE1---- #
list = ["Iron man", "Hulk", "Doctor strange","Captian America","Black panther"]
for i in list:
 print(i)
'''Iron man (output)
    Hulk
    Doctor strange
    Captian America
    Black panther'''

# ----CODE2---- #
list = ["Iron man", "Hulk", "Doctor strange","Captian America","Black panther"]
for i in range(len(list)):
 print(list[i])
#output = Same as above

# ----CODE3---- #
list = ["Iron man", "Hulk", "Doctor strange","Captian America","Black panther"]
i = 0
while i <len(list):
 print(list[i])
 i += 1
#output = Same as above

# ----CODE4---- #
list = ["Iron man", "Hulk", "Doctor strange","Captian America","Black panther"]
[print(i) for i in list]
#output = Same as above

