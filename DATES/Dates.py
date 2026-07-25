# ----CODE1----
import datetime

# 1. Create a tuple containing date-time objects (including microseconds for %f)
mytuple = (
    datetime.datetime(2026, 12, 31, 17, 41, 0, 548513),
    datetime.datetime(2027, 5, 15, 9, 30, 0, 123456),
    datetime.datetime(2028, 8, 20, 23, 15, 45, 789012)
)

# 2. Get an iterator from the tuple using iter()
myit = iter(mytuple)

# 3. Fetch each date and apply the new formatting directives from your second table
# %c = Local version of date/time, %x = Local date, %X = Local time, %j = Day number, %f = Microsecond, %C = Century
print(next(myit).strftime("Local: %c | Date: %x | Time: %X | Day of Year: %j | Microsecond: %f | Century: %C")) 
#output = Local: Thu Dec 31 17:41:00 2026 | Date: 12/31/26 | Time: 17:41:00 | Day of Year: 365 | Microsecond: 548513 | Century: 20

print(next(myit).strftime("Local: %c | Date: %x | Time: %X | Day of Year: %j | Microsecond: %f | Century: %C")) 
#output = Local: Sat May 15 09:30:00 2027 | Date: 05/15/27 | Time: 09:30:00 | Day of Year: 135 | Microsecond: 123456 | Century: 20

print(next(myit).strftime("Local: %c | Date: %x | Time: %X | Day of Year: %j | Microsecond: %f | Century: %C")) 
#output = Local: Sun Aug 20 23:15:45 2028 | Date: 08/20/28 | Time: 23:15:45 | Day of Year: 233 | Microsecond: 789012 | Century: 20


# ==============================================================================
# LINE-BY-LINE EXPLANATION OF FUNCTIONS & CODE
# ==============================================================================
#
# FUNCTIONS & METHODS USED:
# 1. datetime.datetime() : Creates specific date-time objects with year, month, day, 
#                          hour, minute, second, and microsecond parameters.
# 2. iter()              : Creates an iterator stream from the provided tuple.
# 3. next()              : Grabs the next immediate datetime object from the stream.
# 4. .strftime()         : Translates dates into customized string patterns using 
#                          the code percentage tokens (%c, %x, %X, etc.).
#
# DIRECTIVES USED FROM THE NEW TABLE:
# - %f : Extracts the microsecond fractional string values (000000-999999).
# - %j : Computes the current chronological day number of that year (001-366).
# - %c : Formats an entire standardized local visual layout of the date and time.
# - %C : Identifies the specific numeric century digits (e.g., 20).
# - %x : Outputs a standard clean local numeric format string for just the date.
# - %X : Outputs a standard clean local numeric format string for just the time.
#
# CODE BREAKDOWN:
# - import datetime
#   Loads Python's built-in time keeping library framework.
#
# - mytuple = (...)
#   Bundles 3 microsecond-precise datetime nodes into an immutable array tuple.
#
# - myit = iter(mytuple)
#   Prepares an isolated iteration tracker state machine pointed at the tuple.
#
# - print(next(myit).strftime(...))
#   Advances the read index target, fetches the object, processes the string flags,
#   and instantly pipes the computed string sequence directly into the standard stdout.
# ==============================================================================
