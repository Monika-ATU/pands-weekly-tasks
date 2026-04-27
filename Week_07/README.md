# Program es.py

## Project Description
The purpose of this program was to count the number of occurrences of the letter "e" in a text file. The program runs from the terminal and requires a filename as an argument when run. This allows it to be used on different files without changing the code.

---

### Step 1 - Check if filename was provided
```python
if len(sys.argv) < 2:
    print("Error: No filename provided.")
    exit()
```
* Checks if the user provided a filename in the terminal command.
* **Why:** If the user just types `python es.py`, the program alerts them that no filename was provided and exits. This prevents the program from crashing due to missing inputs.

### Step 2 - Get filename from command line
```python
filename = sys.argv
```
* Saves the file name passed in the terminal to the `filename` variable so it can be targeted for opening.

### Step 3 - Try to open and read the file safely
```python
try:
    with open(filename, "r") as file:
        content = file.read()
except FileNotFoundError:
    print("Error: File does not exist.")
    exit()
```
* Attempts to safely open the file and read its contents.
* **Why:** If the file does not exist or the name is typed incorrectly, the program catches the error, displays a clean message, and exits gracefully instead of crashing the terminal.

### Step 4 - Count number of 'e' characters
```python
count = content.count("e")
```
* Counts all occurrences of the lowercase letter "e" within the text.
* **Why:** This isolates specifically the lowercase character search required by the program logic.

### Step 5 - Output result
```python
print(f"Number of 'e' characters: {count}")
```
* Prints the calculated result in a readable format for the user.

---

## Example Execution
To run this program in your terminal or Cmder against a text file called `moby-dick.txt` (I created an empty file with this name, so the result will be zero, but when you enter any sentence the number changes, so the code is correct), use the following command:

```bash
python es.py moby-dick.txt
```

---