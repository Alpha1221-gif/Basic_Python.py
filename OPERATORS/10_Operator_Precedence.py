# ----CODE01---- #
# Concept: Parentheses () - Forces precedence or groups expressions
x = (2 + 3) * 4
print(x) # output = 20

# ----CODE02---- #
# Concept: Exponentiation (**) - Raises a number to a power
x = 2 ** 3
print(x) # output = 8

# ----CODE03---- #
# Concept: Unary operators (+x, -x, ~x) - Modifies a single operand
x = 5
print(-x) # output = -5
print(~x) # output = -6 (Bitwise NOT: ~x = -x - 1)

# ----CODE04---- #
# Concept: Multiplicative operators (*, /, //, %) - Performs product, division, floor division, or remainder
x = 7
print(x // 3) # output = 2 (Floor division)
print(x % 3) # output = 1 (Modulus)

# ----CODE05---- #
# Concept: Additive operators (+, -) - Performs standard addition and subtraction
x = 10 - 4 + 2
print(x) # output = 8

# ----CODE06---- #
# Concept: Bitwise shifts (<<, >>) - Shifts bits left or right
x = 5 # Binary: 0101
print(x << 1) # output = 10 (Binary: 1010)
print(x >> 1) # output = 2 (Binary: 0010)

# ----CODE07---- #
# Concept: Bitwise AND (&) - Sets each bit to 1 if both bits are 1
x = 5 # Binary: 0101
y = 3 # Binary: 0011
print(x & y) # output = 1 (Binary: 0001)

# ----CODE08---- #
# Concept: Bitwise XOR (^) - Sets each bit to 1 if only one of two bits is 1
x = 5 # Binary: 0101
y = 3 # Binary: 0011
print(x ^ y) # output = 6 (Binary: 0110)

# ----CODE09---- #
# Concept: Bitwise OR (|) - Sets each bit to 1 if one of two bits is 1
x = 5 # Binary: 0101
y = 3 # Binary: 0011
print(x | y) # output = 7 (Binary: 0111)

# ----CODE10---- #
# Concept: Comparisons, identity, and membership - Evaluates relationship between values
x = [1, 2]
y = [1, 2]
print(x == y) # output = True (Equal values)
print(x is y) # output = False (Different memory objects)
print(1 in x) # output = True (Membership check)

# ----CODE11---- #
# Concept: Logical NOT (not) - Reverses the logical state of its operand
x = True
print(not x) # output = False

# ----CODE12---- #
# Concept: Logical AND (and) - Returns True if both statements are true
x = True
y = False
print(x and y) # output = False

# ----CODE13---- #
# Concept: Logical OR (or) - Returns True if one of the statements is true
x = True
y = False
print(x or y) # output = True
