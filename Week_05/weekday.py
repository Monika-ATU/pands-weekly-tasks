# weekday.py
# Program to check whether today is a weekday or a weekend.
# Author Monika Fras

# Step 1: Import the datetime module
from datetime import datetime

# Step 2: Get today's date
today = datetime.today()

# Step 3: Get the day of the week (0 = Monday, 6 = Sunday)
day = today.weekday()

# Step 4: Check if it's a weekday
if day < 5:
    print("Yes, unfortunately today is a weekday.")
else:
    print("It is the weekend, yay!")