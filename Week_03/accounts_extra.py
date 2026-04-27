# accounts_extra.py
# A program to display 4 last digits from an account number (any lenght)
# Author Monika Fras


# Step 1: Ask the user to enter an account number
account = input("Please enter an account number: ")

# Step 2: Get the length of the account number
length = len(account)

# Step 3: Replace all but the last 4 characters with X
hidden = "X" * (length - 4) + account[-4:]

# Step 4: Print the result
print(hidden)