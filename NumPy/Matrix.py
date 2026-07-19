import numpy as np

# Creating matrix
# -------------------
arr1 = np.array([[1,2],[4,5]])
arr2 = np.array([[1,2],[4,5]])
print(arr1*arr2)

var1 = np.matrix([[1,2,3],[4,5,6],[7,8,9]])
var2 = np.matrix([[1,2,3],[4,5,6],[7,8,9]])
print(var1*var2)


# Functions in Matrix
# -----------------------
# Transpose
# --------------

arr1 = np.array([[1,2],[4,5]])
arr2 = np.transpose(arr1)
print(arr2)
print(arr1.T)

# Swapaxes
# --------------
# swapaxes() in NumPy is used to interchange (swap) two axes of an array.

# np.swapaxes(array, axis1, axis2) syntax

print("Swapaxes")
a = np.array([[1,2,3],
              [4,5,6]])

print(a.shape)
b=np.swapaxes(a,0,1)
print(b)
print(b.shape)

# inverse
# inverse of a matrix is a matrix when multiplied to original results in a identity matrix
inv = np.linalg.inv(arr1)
print(inv)


# Trace 
# -----------------

trace = np.trace(arr1)
print(trace)

# Rank
# -----------------
rank = np.linalg.matrix_rank(arr1)
print(rank)

# Power
# ----------

pow = np.linalg.matrix_power(arr1,2)
print(pow)
pow = np.linalg.matrix_power(arr1,0)
print(pow)
pow = np.linalg.matrix_power(arr1,-2)
print(pow)

# Determinant
# -------------

det = np.linalg.det(arr1)
print(det)

# for determinant and inverse square matrix is required (n*n)

# Eigenvalues and Eigenvectors
# -----------------
eigenvalues, eigenvectors = np.linalg.eig(arr1)
print("Eigenvalues:", eigenvalues)
print("Eigenvectors:", eigenvectors)
# .eig() function returns the eigenvalues and eigenvectors of a square matrix.
# The eigenvalues are returned as a 1D array,
# while the eigenvectors are returned as a 2D array where each column corresponds to an eigenvector.
# Eigenvalues: [-0.46410162  6.46410162]
# Eigenvectors:
# [[-0.80689822 -0.34372377]
#  [ 0.59069049 -0.9390708 ]]