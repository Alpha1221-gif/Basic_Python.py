import math

# Initializing variables for the examples
age = 36
name = "John"
large_number = 1234567
pi_value = 3.14159265
nan_value = float('nan')
large_float = 1234567.89
percentage = 0.75

# ----CODE1----
# Concept: Left alignment (<)
# Explanation: Left-aligns the output text within the available character width. 
# It adds padding spaces to the right side of the value if it is shorter than the specified width.
txt1 = "Left align:   |{1:<10}| is {0}."
print(txt1.format(age, name))

# ----CODE2----
# Concept: Right alignment (>)
# Explanation: Right-aligns the output text within the available character width. 
# It adds padding spaces to the left side of the value to fill the empty space.
txt2 = "Right align:  |{1:>10}| is {0}."
print(txt2.format(age, name))

# ----CODE3----
# Concept: Center alignment (^)
# Explanation: Centers the output text within the allocated character width. 
# It distributes padding spaces as evenly as possible to both the left and right sides.
txt3 = "Center align: |{1:^10}| is {0}."
print(txt3.format(age, name))

# ----CODE4----
# Concept: Sign positioning (=)
# Explanation: Forces the math sign (+ or -) to be placed at the leftmost position 
# of the field while keeping the numerical digits right-aligned, pushing padding spaces in between.
txt4 = "Sign left:    |{0:=+10}|"
print(txt4.format(age))

# ----CODE5----
# Concept: Plus sign requirement (+)
# Explanation: Explicitly forces the output to display a sign indicator (+ or -) 
# for all numbers, showing a plus sign for positive numbers and a minus sign for negative numbers.
txt5 = "Plus sign:    {1} is {0:+}."
print(txt5.format(age, name))

# ----CODE6----
# Concept: Minus sign default (-)
# Explanation: Displays a minus sign strictly for negative numerical values only. 
# This is the standard default behavior in Python where positive numbers show no sign prefix.
txt6 = "Minus sign:   {1} is {0:-}."
print(txt6.format(age, name))

# ----CODE7----
# Concept: Leading space placeholder ( )
# Explanation: Inserts a leading blank space character before positive numbers, 
# while maintaining a standard minus sign before negative numbers, aligning stacked data columns nicely.
txt7 = "Space sign:   {1} is |{0: }|."
print(txt7.format(age, name))

# ----CODE8----
# Concept: Comma thousands separator (,)
# Explanation: Automatically injects a comma as a thousands separator element 
# for large numbers, improving overall readability for large values (e.g., 1,234,567).
txt8 = "Comma sep:    {1} saved ${2:,}."
print(txt8.format(age, name, large_number))

# ----CODE9----
# Concept: Underscore thousands separator (_)
# Explanation: Automatically places an underscore as a thousands separator divider element. 
# This is an alternative layout standard for formatting huge numbers or code-friendly outputs.
txt9 = "Underscore:   {1} saved ${2:_}."
print(txt9.format(age, name, large_number))

# ----CODE10----
# Concept: Binary conversion (b)
# Explanation: Automatically converts an integer into its equivalent base-2 binary representation text.
txt10 = "Binary:       {0} in binary is {0:b}."
print(txt10.format(age))

# ----CODE11----
# Concept: Unicode conversion (c)
# Explanation: Directly converts an integer value into its corresponding character mapping based on Unicode rules.
txt11 = "Unicode char: Code 65 is {0:c}."
print(txt11.format(65))

# ----CODE12----
# Concept: Decimal conversion (d)
# Explanation: Forces an integer value to display explicitly in standard base-10 decimal integer formatting.
txt12 = "Decimal:      {0} in decimal is {0:d}."
print(txt12.format(age))

# ----CODE13----
# Concept: Scientific notation lowercase (e)
# Explanation: Formats a numerical value using mathematical scientific exponential notation 
# with a lowercase "e" component separating the base and exponent values.
txt13 = "Scientific e: {2} in lower-e is {2:e}."
print(txt13.format(age, name, large_number))

# ----CODE14----
# Concept: Scientific notation uppercase (E)
# Explanation: Formats a numerical value using mathematical scientific exponential notation 
# with an uppercase "E" component separating the base and exponent values.
txt14 = "Scientific E: {2} in upper-E is {2:E}."
print(txt14.format(age, name, large_number))

# ----CODE15----
# Concept: Fixed-point lowercase (f)
# Explanation: Displays a number as a standard floating-point fixed decimal string. 
# Special non-numeric states display as standard lowercase 'inf' or 'nan'.
txt15 = "Fix point lower: {1} is {0} years old, Pi is {2:f}."
print(txt15.format(age, name, pi_value))

# ----CODE16----
# Concept: Fixed-point uppercase (F)
# Explanation: Displays a number as a fixed decimal string. Special non-numeric states 
# are automatically forced into uppercase block outputs like 'INF' or 'NAN'.
txt16 = "Fix point upper: Invalid age value is {0:F}."
print(txt16.format(nan_value))

# ----CODE17----
# Concept: General formatting lowercase (g)
# Explanation: Automatically chooses between fixed-point or scientific notation based on scale. 
# It drops insignificant trailing zeros, keeping string outputs brief with lowercase characters.
txt17 = "General lower:   Large float is {0:g}."
print(txt17.format(large_float))

# ----CODE18----
# Concept: General formatting uppercase (G)
# Explanation: Automatically selects between fixed-point or scientific notation based on size. 
# It drops trailing zeros and forces scientific output text to use an uppercase 'E' character.
txt18 = "General upper:   Large float is {0:G}."
print(txt18.format(large_float))

# ----CODE19----
# Concept: Octal conversion (o)
# Explanation: Directly transforms a base-10 integer into its equivalent base-8 octal notation format text string.
txt19 = "Octal:           {1}'s age {0} in octal is {0:o}."
print(txt19.format(age, name))

# ----CODE20----
# Concept: Hexadecimal lowercase (x)
# Explanation: Converts an integer into its equivalent base-16 hexadecimal text string, 
# rendering character values (a-f) completely in lowercase format.
txt20 = "Hex lower:       {1}'s age {0} in hex is {0:x}."
print(txt20.format(age, name))

# ----CODE21----
# Concept: Hexadecimal uppercase (X)
# Explanation: Converts an integer into its equivalent base-16 hexadecimal text string, 
# rendering character values (A-F) completely in uppercase format.
txt21 = "Hex upper:       {1}'s age {0} in hex is {0:X}."
print(txt21.format(age, name))

# ----CODE22----
# Concept: Number formatting (n)
# Explanation: Automatically formats a number while applying localized thousands separator and decimal 
# character settings based on the current computer's regional locale parameters.
txt22 = "Number format:   {1}'s score is {2:n}."
print(txt22.format(age, name, large_float))

# ----CODE23----
# Concept: Percentage conversion (%)
# Explanation: Multiplies a numerical float fraction by 100, renders it as a decimal 
# layout value, and automatically appends a percentage symbol (%) at the end of the text.
txt23 = "Percentage:      {1} completed {2:%} of the task."
print(txt23.format(age, name, percentage))
