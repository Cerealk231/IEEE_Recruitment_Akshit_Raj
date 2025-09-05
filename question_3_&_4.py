import numpy as np

# Create 5x5 matrix with random integers between 1 and 100
matrix = np.random.randint(1, 101, size=(5, 5))

print("Original 5x5 Matrix:")
print(matrix)

# Calculate max, min, mean
max_val = matrix.max()
min_val = matrix.min()
mean_val = matrix.mean()

print("\nMaximum value:", max_val)
print("Minimum value:", min_val)
print("Mean value:", mean_val)

# Normalize values between 0 and 1
normalized_matrix = (matrix - min_val) / (max_val - min_val)
print("\nNormalized Matrix (0-1):")
print(normalized_matrix)

# Flatten to 1D array and sort
flattened_sorted = np.sort(matrix.flatten())
print("\nFlattened & Sorted Array:")
print(flattened_sorted)