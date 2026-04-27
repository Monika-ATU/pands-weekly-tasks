# es.py
# Program to count the number of occurrences of the letter "e" in a text file
# Author Monika Fras


import sys

# Step 1: Check if filename was provided
if len(sys.argv) < 2:
    print("Error: No filename provided.")
    exit()

# Step 2: Get filename from command line
filename = sys.argv[1]

# Step 3: Try to open and read the file safely
try:
    with open(filename, "r") as file:
        content = file.read()
except FileNotFoundError:
    print("Error: File does not exist.")
    exit()

# Step 4: Count number of 'e' characters
count = content.count("e")

# Step 5: Output result
print(f"Number of 'e' characters: {count}")