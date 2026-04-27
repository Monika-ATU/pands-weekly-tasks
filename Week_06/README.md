# The squareroot.py Program

## Project Description
The goal of this program was to write a custom function that approximates the square root of a given positive number. I didn't use built-in functions like `math.sqrt()` or `x ** 0.5`; I created my own solution. I used the Newton-Raphson method for the calculations.

---

## A Brief Overview of the Newton-Raphson Method
The Newton-Raphson method is a way to approximate the square root without using built-in functions. It works simply:
* We start with a guess (e.g., half a number),
* then repeatedly improve it to become increasingly accurate.

Each correction is calculated using the formula:
`guess = (guess + number / guess) / 2`

**What does \frac mean?**
`\frac` is a fraction notation in mathematical format (LaTeX). For example `\frac{a}{b}` simply means `a` divided by `b`.

In our formula, this means:
* First, we calculate the `number / guess`,
* add it to `guess`,
* and then divide the whole thing by 2.

So in Python, it looks like this:
```python
guess = (guess + number / guess) / 2
```
After a few iterations, the result quickly approaches the true root.

---


### Step 1 - Defining the sqrt function
```python
def sqrt(number):
    guess = number / 2

    for _ in range(20):
        guess = (guess + number / guess) / 2

    return guess
```
I create my own `sqrt` function that:
* starts with a simple guess (`number / 2`)
* improves the result by a factor of 20 using the Newton-Raphson method (I assumed that 20 times would give a fairly accurate result)
* returns the final approximate square root

### Step 2 - Getting a number from the user
```python
num = float(input("Please enter a positive number: "))
```
I get the number from the user and convert it to float so it can contain decimals.

### Step 3 - Calculating the square root
```python
result = sqrt(num)
```
I call the `sqrt` function to calculate the approximate square root of the given number.

### Step 4 - Displaying the result
```python
print(f"The approximate square root of {num} is {result:.2f}")
```
I display the result and round it to 2 decimal places.

---