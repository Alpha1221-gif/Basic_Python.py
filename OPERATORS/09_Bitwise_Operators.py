# ----CODE01---- #
# Concept: Bitwise AND (&) - Sets each bit to 1 if both bits are 1
x = 5  # Binary: 0101
y = 3  # Binary: 0011
print(x & y)
# output = 1 (Binary: 0001)

# ----CODE02---- #
# Concept: Bitwise OR (|) - Sets each bit to 1 if one of two bits is 1
x = 5  # Binary: 0101
y = 3  # Binary: 0011
print(x | y)
# output = 7 (Binary: 0111)

# ----CODE03---- #
# Concept: Bitwise XOR (^) - Sets each bit to 1 if only one of two bits is 1
x = 5  # Binary: 0101
y = 3  # Binary: 0011
print(x ^ y)
# output = 6 (Binary: 0110)

# ----CODE04---- #
# Concept: Bitwise NOT (~) - Inverts all the bits
x = 5  # Binary: 0101
print(~x)
# output = -6 (Binary: ...11111010 due to two's complement)

# ----CODE05---- #
# Concept: Zero fill left shift (<<) - Shift left by pushing zeros in from the right
x = 5  # Binary: 0101
print(x << 2)
# output = 20 (Binary: 00010100)

# ----CODE06---- #
# Concept: Signed right shift (>>) - Shift right by pushing copies of the leftmost bit from the left
x = 5  # Binary: 0101
print(x >> 2)
# output = 1 (Binary: 00000001)
