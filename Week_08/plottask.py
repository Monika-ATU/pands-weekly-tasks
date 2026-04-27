# plottask.py
# The purpose of this program was to generate visual data using Python
# Author Monika Fras

import numpy as np
import matplotlib.pyplot as plt

# Step 1: Generate Normal Distribution data
# 1000 values with mean = 5 and standard deviation (std_dev) = 2
mean = 5
std_dev = 2
data = np.random.normal(mean, std_dev, 1000)

# Step 2: Generate function data for h(x) = x^3 with range from 0 to 10
x = np.linspace(0, 10, 100)
y = x**3

# Step 3: Plotting both on one set of axes
plt.figure(figsize=(8, 6))

# Histogram (normalized so it fits with the curve better)
plt.hist(data, bins=30, density=True, alpha=0.6, color='blue', label='Normal Distribution')

# Function plot
plt.plot(x, y, color='red', label='h(x) = x^3')

# Step 4: Adding labels and legend
plt.title("Histogram and Function Plot")
plt.xlabel("X values")
plt.ylabel("Density / Function Value")
plt.legend()
plt.grid(True)

# Step 5: Save the plot as PNG
plt.savefig("plottask.png")

# Step 6: Show the plot
plt.show()