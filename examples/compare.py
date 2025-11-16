import matplotlib.pyplot as plt
import math
import numpy as np

# 1. The Exact Method (Dynamic Programming)
def get_exact_partitions(n):
    partitions = [0] * (n + 1)
    partitions[0] = 1
    for i in range(1, n + 1):
        for j in range(i, n + 1):
            partitions[j] += partitions[j - i]
    return partitions

# 2. The Approximation Method (Hardy-Ramanujan)
def get_approx_partitions(n):
    if n == 0: return 1
    # Hardy-Ramanujan Formula
    constant = 1 / (4 * n * math.sqrt(3))
    exponent = math.pi * math.sqrt((2 * n) / 3)
    return constant * math.exp(exponent)

# --- Configuration ---
TARGET = 10000  # We use 100 so the graph is readable
x_values = list(range(1, TARGET + 1))

# Generate Data
exact_y = get_exact_partitions(TARGET)[1:] # Slice [1:] to match x_values
approx_y = [get_approx_partitions(x) for x in x_values]

# --- The "3b1b" Style Plotting ---
plt.style.use('dark_background') # The dark theme
plt.figure(figsize=(10, 6))

# Plot Exact (Blue dots)
plt.plot(x_values, exact_y, 'o', color='#4AF626', markersize=4, label='Exact (DP)', alpha=0.8)

# Plot Approx (Yellow line)
plt.plot(x_values, approx_y, '-', color='#FFD700', linewidth=2, label='Ramanujan Approx')

# Formatting
plt.title(f"Integer Partitions: Exact vs Approximation (N=1 to {TARGET})", fontsize=14, color='white')
plt.xlabel("Target Number (N)", fontsize=12)
plt.ylabel("Number of Ways (Log Scale)", fontsize=12)
plt.yscale('log') # Crucial! The numbers grow too fast for a linear scale
plt.grid(True, which="both", ls="-", alpha=0.2)
plt.legend()

plt.show()