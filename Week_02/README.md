#  Euro Cent Calculator

##  Project Description
The goal of this program was to create a simple calculator that adds two cent amounts and displays the result in a readable format – in euros and cents (e.g., **€2.45** instead of **245**).

---


### Step 1 - Ask for the first amount in cents
```python
Amount_01 = int(input("Enter first amount (in cents): "))
```
* Asks the user to enter the first amount.
* Uses `input()` to get data and `int()` to convert text to an integer.
* **Why:** We need numbers for mathematical operations, not text.

### Step 2 - Ask for the second amount in cents
```python
Amount_02 = int(input("Enter second amount (in cents): "))
```
* Repeats the process for the second value.
* **Why:** This allows the program to sum two different numbers.

### Step 3 - Add the two amounts
```python
total = Amount_01 + Amount_02
```
* Adds both amounts and stores the result in the `total` variable.
* **Why:** This is the core operation of our calculator.

### Step 4 - Convert total to euros and cents
```python
euros = total // 100
cents = total % 100
```
* Handles the main logic of the program.
* `// 100` (integer division) gives the number of whole euros.
* `% 100` (modulo) gives the remainder, which represents the cents.

### Step 5 - Displaying the Result
```python
print(f"The total is €{euros}.{cents:02d}")
```
* Displays the final amount to the user.
* Uses an **f-string** to easily insert variables.
* The `:02d` format forces cents to always display as two digits (e.g., `05` instead of `5`).

---