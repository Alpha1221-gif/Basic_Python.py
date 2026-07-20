# ----CODE1----
tup = ("Honda","BMW","Mercedes","Nissan","Toyata")
for i in tup:
    print(i) 
'''Honda
   BMW
   Mercedes
   Nissan
   Toyata
    '''

# ----CODE2----
tup = ("Honda","BMW","Mercedes","Nissan","Toyata")
for i in range(len(tup)):
    print(tup[i])
#output = same as above

# ----CODE3----  
tup = ("Honda","BMW","Mercedes","Nissan","Toyata")
i = 0
while i <len(tup):
    print(tup[i])
    i+=1
#output = same as above    