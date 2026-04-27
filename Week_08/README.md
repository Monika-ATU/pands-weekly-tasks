# Program plottask.py

## Project Description
The purpose of this program was to generate visual data using Python. It creates a plot that combines a histogram of 1,000 random values from a normal distribution with a graphed curve of the function h(x) = x³. Finally, it saves the visual as a PNG image file.

---

### Step 1 - Generate Normal Distribution data
```python
# 1000 values with mean = 5 and standard deviation (std_dev) = 2
mean = 5
std_dev = 2
data = np.random.normal(mean, std_dev, 1000)
```
* Generates an array of 1,000 random floating-point numbers.
* **Why:** This creates simulated data centered around a mean of 5 with a standard deviation of 2 to create a classic bell curve.

### Step 2 - Generate function data for h(x) = x³ with range from 0 to 10
```python
x = np.linspace(0, 10, 100)
y = x**3
```
* Generates 100 evenly spaced numbers between 0 and 10, and cubes them.
* **Why:** This provides smooth coordinates to plot a clean non-linear curve.

### Step 3 - Plotting both on one set of axes
```python
plt.figure(figsize=(8, 6))

# Histogram (normalized so it fits with the curve better)
plt.hist(data, bins=30, density=True, alpha=0.6, color='blue', label='Normal Distribution')

# Function plot
plt.plot(x, y, color='red', label='h(x) = x^3')
```
* Sets the canvas size and draws both the histogram bars and the line graph.
* **Why:** `density=True` scales the histogram bars down so they share a comparable vertical axis with the curve.

### Step 4 - Adding labels and legend
```python
plt.title("Histogram and Function Plot")
plt.xlabel("X values")
plt.ylabel("Density / Function Value")
plt.legend()
plt.grid(True)
```
* Adds a title, axis labels, a legend box, and background grid lines.
* **Why:** This ensures the graph is readable and professionally presented.

### Step 5 - Save the plot as PNG
```python
plt.savefig("plottask.png")
```
* Exports the generated chart as a static image file to your computer.
* **Why:** This allows you to view or share the plot without running the Python script again.

### Step 6 - Show the plot
```python
plt.show()
```
* Opens an interactive pop-up window displaying the generated visual.

---

#### Chat GPT link
Below is a link to the query in the Chat GPT which was the basis for further work on the code
https://chatgpt.com/s/t_69efacc0bc388191b32473aebf95f41e