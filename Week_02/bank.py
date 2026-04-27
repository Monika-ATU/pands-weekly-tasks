# bank.py
# A program for adding amounts in cents
# Author Monika Fras


# Step 1: Ask for the first amount in cents
Amount_01 = int(input("Enter first amount (in cents): "))

# Step 2: Ask for the second amount in cents
Amount_02 = int(input("Enter second amaunt (in cents): "))

# Step 3: Add the two amounts
total = Amount_01 + Amount_02

# Step 4: Convert total to euros and cents
euros = total // 100  # Whole euros
cents = total % 100   # Remaining cents

# Step 5: Print the result in a readable format
print(f"The total is €{euros}.{cents:02d}")

