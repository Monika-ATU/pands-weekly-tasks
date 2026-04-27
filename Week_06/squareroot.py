# squareroot.py
# A program to write a custom function that approximates the square root of a given positive number
# Author Monika Fras

# Step 1: Define the sqrt function using Newton's method
def sqrt(number):
    # Initial guess
    guess = number / 2

    # Improve the guess iteratively
    for _ in range(20):
        guess = (guess + number / guess) / 2

    return guess


# Step 2: Ask user for a positive floating-point number
num = float(input("Please enter a positive number: "))

# Step 3: Calculate square root using our function
result = sqrt(num)

# Step 4: Print the result (rounded to 2 decimal places)
print(f"The approximate square root of {num} is {result:.2f}")