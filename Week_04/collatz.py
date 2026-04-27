# collatz.py
# A program to implement a so-called Collatz sequence
# Author Monika Fras



# Step 1: Ask the user for a positive integer
number = int(input("Please enter a positive integer: "))

# Step 2: Keep looping until the number becomes 1
while number != 1:
    print(number, end=" ")

    # Step 3: Apply Collatz rules
    if number % 2 == 0:
        number = number // 2   # even
    else:
        number = 3 * number + 1  # odd

# Step 4: Print the final 1
print(1)