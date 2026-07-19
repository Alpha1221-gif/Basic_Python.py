# ----CODE1----
# Concept: capitalize() - Converts the first character to upper case
a = "hello, moon"
print(a.capitalize())
#output = Hello, moon


# ----CODE2----
# Concept: casefold() - Converts string into lower case (stronger than lower())
b = "Hello WORLD"
print(b.casefold())
#output = hello world


# ----CODE3----
# Concept: center() - Returns a centered string
c = "moon"
print(c.center(10, "-"))
#output = ---moon---


# ----CODE4----
# Concept: count() - Returns the number of times a specified value occurs in a string
d = "banana"
print(d.count("a"))
#output = 3


# ----CODE5----
# Concept: encode() - Returns an encoded version of the string
e = "My name is Ståle"
print(e.encode())
#output = b'My name is St\xc3\xa5le'


# ----CODE6----
# Concept: endswith() - Returns true if the string ends with the specified value
f = "Hello, world!"
print(f.endswith("!"))
#output = True


# ----CODE7----
# Concept: expandtabs() - Sets the tab size of the string
g = "H\te\tl\tl\to"
print(g.expandtabs(2))
#output = H e l l o


# ----CODE8----
# Concept: find() - Searches the string for a specified value and returns the position
h = "Hello, welcome to my world."
print(h.find("welcome"))
#output = 7


# ----CODE9----
# Concept: format() - Formats specified values in a string
i = "For only {price:.2f} dollars!"
print(i.format(price = 49))
#output = For only 49.00 dollars!


# ----CODE10----
# Concept: format_map() - Formats specified values in a string using a dictionary
j = {'x': 'John', 'y': 'Peter'}
print("{x} and {y}".format_map(j))
#output = John and Peter


# ----CODE11----
# Concept: index() - Searches the string for a specified value and returns the position
k = "Hello, welcome to my world."
print(k.index("welcome"))
#output = 7


# ----CODE12----
# Concept: isalnum() - Returns True if all characters in the string are alphanumeric
l = "Company12"
print(l.isalnum())
#output = True


# ----CODE13----
# Concept: isalpha() - Returns True if all characters in the string are in the alphabet
m = "CompanyX"
print(m.isalpha())
#output = True


# ----CODE14----
# Concept: isascii() - Returns True if all characters in the string are ascii characters
n = "Company123"
print(n.isascii())
#output = True

# ----CODE15----
# Concept: isdecimal() - Returns True if all characters in the string are decimals
a = "1234"
print(a.isdecimal())
#output = True


# ----CODE16----
# Concept: isdigit() - Returns True if all characters in the string are digits
b = "50083"
print(b.isdigit())
#output = True


# ----CODE17----
# Concept: isidentifier() - Returns True if the string is a valid identifier
c = "my_variable1"
print(c.isidentifier())
#output = True


# ----CODE18----
# Concept: islower() - Returns True if all characters in the string are lower case
d = "hello moon"
print(d.islower())
#output = True


# ----CODE19----
# Concept: isnumeric() - Returns True if all characters in the string are numeric
e = "12345"
print(e.isnumeric())
#output = True


# ----CODE20----
# Concept: isprintable() - Returns True if all characters in the string are printable
f = "Hello! #1"
print(f.isprintable())
#output = True


# ----CODE21----
# Concept: isspace() - Returns True if all characters in the string are whitespaces
g = "   "
print(g.isspace())
#output = True


# ----CODE22----
# Concept: istitle() - Returns True if the string follows the rules of a title
h = "Hello And Welcome"
print(h.title().istitle())
#output = True


# ----CODE23----
# Concept: isupper() - Returns True if all characters in the string are upper case
i = "MOON"
print(i.isupper())
#output = True


# ----CODE24----
# Concept: join() - Joins the elements of an iterable to the end of the string
j = ("John", "Peter", "Vicky")
print("#".join(j))
#output = John#Peter#Vicky


# ----CODE25----
# Concept: ljust() - Returns a left justified version of the string
k = "banana"
print(k.ljust(10), "is my favorite fruit.")
#output = banana     is my favorite fruit.


# ----CODE26----
# Concept: lower() - Converts a string into lower case
l = "Hello World"
print(l.lower())
#output = hello world


# ----CODE27----
# Concept: lstrip() - Returns a left trim version of the string
m = "     banana     "
print(m.lstrip())
#output = banana     


# ----CODE28----
# Concept: maketrans() - Returns a translation table to be used in translations
n = "Hello Sam!"
mytable = n.maketrans("S", "P")
print(n.translate(mytable))
#output = Hello Pam!


# ----CODE29----
# Concept: partition() - Returns a tuple where the string is parted into three parts
o = "I could eat bananas all day"
print(o.partition("bananas"))
#output = ('I could eat ', 'bananas', ' all day')


# ----CODE30----
# Concept: replace() - Returns a string where a specified value is replaced with a specified value
p = "I like apples"
print(p.replace("apples", "oranges"))
#output = I like oranges

# ----CODE31----
# Concept: rfind() - Searches the string for a specified value and returns the last position
a = "Mi casa, su casa."
print(a.rfind("casa"))
#output = 12


# ----CODE32----
# Concept: rindex() - Searches the string for a specified value and returns the last position
b = "Mi casa, su casa."
print(b.rindex("casa"))
#output = 12


# ----CODE33----
# Concept: rjust() - Returns a right justified version of the string
c = "banana"
print(c.rjust(20))
#output =               banana


# ----CODE34----
# Concept: rpartition() - Returns a tuple where the string is parted into three parts
d = "I could eat bananas all day, bananas are good"
print(d.rpartition("bananas"))
#output = ('I could eat bananas all day, ', 'bananas', ' are good')


# ----CODE35----
# Concept: rsplit() - Splits the string at the specified separator, and returns a list
e = "apple, banana, cherry"
print(e.rsplit(", "))
#output = ['apple', 'banana', 'cherry']


# ----CODE36----
# Concept: rstrip() - Returns a right trim version of the string
f = "     banana     "
print(f.rstrip())
#output =      banana


# ----CODE37----
# Concept: split() - Splits the string at the specified separator, and returns a list
g = "welcome to the jungle"
print(g.split())
#output = ['welcome', 'to', 'the', 'jungle']


# ----CODE38----
# Concept: splitlines() - Splits the string at line breaks and returns a list
h = "Thank you for the music\nWelcome to the show"
print(h.splitlines())
#output = ['Thank you for the music', 'Welcome to the show']


# ----CODE39----
# Concept: startswith() - Returns true if the string starts with the specified value
i = "Hello, welcome to my world."
print(i.startswith("Hello"))
#output = True


# ----CODE40----
# Concept: strip() - Returns a trimmed version of the string
j = "     banana     "
print(j.strip())
#output = banana


# ----CODE41----
# Concept: swapcase() - Swaps cases, lower case becomes upper case and vice versa
k = "Hello My Name Is PETER"
print(k.swapcase())
#output = hELLO mY nAME iS peter


# ----CODE42----
# Concept: title() - Converts the first character of each word to upper case
l = "Welcome to my world"
print(l.title())
#output = Welcome To My World


# ----CODE43----
# Concept: translate() - Returns a translated string
m = "Hello Sam!"
mytable = m.maketrans("S", "P")
print(m.translate(mytable))
#output = Hello Pam!


# ----CODE44----
# Concept: upper() - Converts a string into upper case
n = "Hello my friends"
print(n.upper())
#output = HELLO MY FRIENDS


# ----CODE45----
# Concept: zfill() - Fills the string with a specified number of 0 values at the beginning
o = "50"
print(o.zfill(10))
#output = 0000000050
