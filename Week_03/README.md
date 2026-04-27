# Account Number Hider

## Project Description
The goal of this program was to hide part of an account number for security purposes. The program retrieves the account number from the user and displays it so that only the last digits are visible, with the rest converted to the character `X`.

First, a basic version was created (for exactly 10 characters), followed by an extended version that works for any number length.

---

## Basic Version 



### Step 1 - Retrieving the Account Number
```python
account = input("Please enter an 10-digit account number: ")
```
* Asks the user to enter the account number.
* **Why:** I use `input()` because I want to treat the number as a string, not a number – this way, I don't lose any characters.

### Step 2 - Hiding the First 6 Characters
```python
hidden = "XXXXXX" + account[6:]
```
* Assumes the account number is exactly 10 characters long.
* `"XXXXXX"` replaces the first 6 characters.
* `account[6:]` retrieves everything from the 7th character to the end (i.e., the last 4 characters).

### Step 3 - Displaying the Result
```python
print(hidden)
```
* Displays the modified, secure account number.



---

## Extended Version (Extra)

### What's changed and why?
In this version, the program has been improved to work with account numbers of any length, not just 10 characters.



### Step 1 - Retrieving the Account Number
```python
account = input("Please enter an account number: ")
```
* **Why:** I removed the 10-character limit from the prompt to make the program more versatile.

### Step 2 - Calculating the Length
```python
length = len(account)
```
* Uses the `len()` function to check how many characters are in the entered account number.
* **Why:** This is necessary to know dynamically how many characters to hide.

### Step 3 - Hiding All Characters Except the Last 4
```python
hidden = "X" * (length - 4) + account[-4:]
```
* **"X" * (length - 4)** creates the appropriate number of `X` characters dynamically.
* **account[-4:]** retrieves the last 4 characters regardless of the total length.
* **Why:** This core logic allows the program to work flawlessly with any account number length.

### Step 4 - Displaying the Result
```python
print(hidden)
```
* Displays the final masked result to the user.

---

## Summary
The basic version was a great starting point, but the extended version is much more practical for real-world applications because works for any number. In basic version if user enters a shorter or longer number, the result may be incorrect.

---