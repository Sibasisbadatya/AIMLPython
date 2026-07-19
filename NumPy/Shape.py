import numpy as np
# SHAPES
# ======================

# for 1D it says like (3,) meaning 1D and contains 3 elements
var = np.array([[1,2],[3,4]])
print(var.shape)

var = np.array([1,2,3,4],ndmin=6)
print(var)
print(var.shape)

# reshape
var1 = np.array([1,2,3,4])
print(var1.reshape(2,2)) # row*col should be same as arry.length
var2 = var1.reshape(2,2)
print(var2.shape)
# basic syntax array.reshape(dim1, dim2, dim3), dim1×dim2×dim3=total elements
arr = np.array([1,2,3,4,5,6,7,8])
arr3d = arr.reshape(2,2,2)
print(arr3d)

arr1 = arr3d.reshape(-1) # reshapes to 1D array
print(arr1.ndim)
print(arr1)