# Collatz Sequence

## Project Description
The goal of this program was to implement a so-called Collatz sequence. The program takes any positive integer from the user and then generates subsequent values according to specific rules:
* If the number is even, divide it by 2.
* If the number is odd, multiply it by 3 and add 1.
* The program terminates when it reaches 1.

---


### Step 1 - Getting a Number from the User
```python
number = int(input("Please enter a positive integer: "))
```
* Asks the user to enter a number.
* Uses `input()` to retrieve the data and `int()` to convert it to an integer.
* **Why:** This is necessary because I will be performing mathematical operations later.

### Step 2 - Loop until 1 is reached
```python
while number != 1:
```
* Uses a `while` loop that runs as long as the number is not equal to 1.
* **Why:** The program is supposed to stop at that point according to the rules of the task.

### Step 3 - Printing the current value
```python
print(number, end=" ")
```
* Prints the current value of the number in each iteration.
* The `end=" "` parameter causes the numbers to be printed on a single line, separated by a space, instead of each on a new line.

### Step 4 - Checking if the number is even
```python
if number % 2 == 0:
    number = number // 2
```
* Checks if the number is even using the modulo operator `%`.
* If the remainder of division by 2 is 0, then the number is even and gets divided by 2.
* Uses `//` to ensure the result remains an integer.

### Step 5 -  Handling Odd Numbers
```python
else:
    number = 3 * number + 1
```
* If the number is not even, it must be odd.
* Applies the second condition: multiplies the number by 3 and adds 1.

### Step 6 - Printing the Final Value
```python
print(1)
```
* Prints the last value after the loop ends (when the number reaches 1).
* This completes the string and terminates the program as required.

---