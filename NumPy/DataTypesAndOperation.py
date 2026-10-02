
import numpy as np
# Data Types

var = np.array([1,2,3,4])
print(var.dtype) 

var = np.array([1.0,3,4])
print(var.dtype) 

# Changing of data type

dar = np.array([1,2,3,4])
print(dar.dtype) 

complex = np.array([1,2,3,4],dtype=complex) #print as complex data type
print(complex)

arr = np.array([1+2j, 3+4j])
print(arr)


dar = np.array([1,2,3,4],dtype=np.int8)
print(dar.dtype) # but make sure that all elements will be in range from (-2^7 - 2^7-1) or else it will give the o/p within that range only


far = np.array([1,2,3,4],dtype=np.float16)
print(far.dtype) 
print(far)


# OPERATIONS
# ------------------------

# Addition of single array
arr1 = np.array([1,2,3,4])
arr2 = arr1+3
print(arr2)
# Addition of 2 array

arr1 = np.array([1,2,3,4])
arr2 = np.array([2,3,4,5])
arr3 = arr1+arr2 # lenght must be same
print(arr3)

arr4 = np.add(arr1,arr2)
print(arr4) #same ad arr1 + arr2

# Same for .subtraction ,/ .devide ,% .mod ,* .multiply , 1/a .reciprocal(), ** .power()  and same for 2D arrays


# MAX and MIN
# ----------------------------
maxarr = np.array([1,20,3,4])
print(np.min(maxarr))
print(np.max(maxarr))

print(np.argmin(maxarr)) # position of min
print(np.argmax(maxarr))

# for 2 dimensional array
# axis0 -> column ,axis1 -> row
arr2d = np.array([[1,2,31,4],[1,20,3,4]])
print(np.max(arr2d,axis=0)) # gives 1d array of max elements along each axis=0 ->each column
print(np.max(arr2d,axis=1))

# square root

print(np.sqrt(arr2d))

# sina and cos value
print(np.sin(maxarr))
print(np.cos(maxarr))

# cumulative sum

print(np.cumsum(maxarr))