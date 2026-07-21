
username = "Admin"
is_logged_in = True
has_premium = False
is_suspended = False
# ----Code1----
# 1. Using 'and' (Both must be True)
if is_logged_in and has_premium:
    print(f"Welcome back {username}! Enjoy your premium features.")
else:
    print(f"Welcome {username}! Standard access granted.")


# ----CODE2----
# 2. Using 'or' (At least one must be True)
if username == "Admin" or has_premium:
    print("Access allowed: Special dashboard unlocked.")


# ----CODE3----
# 3. Using 'not' (Inverts the value)
if not is_suspended:
    print("Account check passed: System online.")
