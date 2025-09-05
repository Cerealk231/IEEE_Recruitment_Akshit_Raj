import numpy as np

#question 3
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

# question 4
middle_matrix = matrix[1:4, 1:4]   # slicing rows 1-3 and cols 1-3
print("\nMiddle 3x3 Matrix:")
print(middle_matrix)

# Extract first row of middle matrix
first_row = middle_matrix[0, :]
print("\nFirst Row of Middle 3x3:", first_row)

# Extract last column of middle matrix
last_col = middle_matrix[:, -1]
print("Last Column of Middle 3x3:", last_col)

# Compute dot product
dot_product = np.dot(first_row, last_col)
print("\nDot Product of First Row and Last Column:", dot_product)
