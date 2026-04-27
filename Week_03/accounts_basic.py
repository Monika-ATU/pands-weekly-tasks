# accounts_basic.py
# A program to display 4 last digits from an 10 digit account number
# Author Monika Fras



# Step 1: Ask the user to enter a 10 digit account number
account = input("Please enter an 10 digit account number: ")

# Step 2: Replace the first 6 characters with X
hidden = "XXXXXX" + account[6:]

# Step:3 Print the result
print(hidden)