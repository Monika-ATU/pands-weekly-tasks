# Program weekday.py

## Project Description
The purpose of this program was to check whether today is a weekday or a weekend. The program requires no user input – it retrieves the current date and displays the appropriate message based on it. I used the built-in `datetime` module to accomplish this task.

---

### Step 1 - Importing the datetime module
```python
from datetime import datetime
```
* Imports the `datetime` module because it allows me to work with the current date and time in Python.
* **Why:** Without it, I would not have access to information about today's date.

### Step 2 - Getting the Current Date
```python
today = datetime.today()
```
* Gets the current date and stores it in the `today` variable.
* **Why:** This ensures that the program always runs dynamically and is not dependent on manually entering the date.

### Step 3 - Checking the Day of the Week
```python
day = today.weekday()
```
* The `.weekday()` method returns a number from 0 to 6 representing the day of the week:
  * 0 = Monday
  * 1 = Tuesday
  * 2 = Wednesday
  * 3 = Thursday
  * 4 = Friday
  * 5 = Saturday
  * 6 = Sunday
* **Why:** This allows me to easily check whether it is a weekday or a weekend.

### Step 4 - Checking the Condition and Displaying the Result
```python
if day < 5:
    print("Yes, unfortunately today is a weekday.")
else:
    print("It is the weekend, yay!")
```
* Checks the value of the `day` variable.
* If it is less than 5, it means a workday (Monday through Friday).
* If it is 5 or 6, it means a weekend (Saturday or Sunday).
* **Why:** Based on this, I print the appropriate message.

---