import numpy as np
# Indexing
# ---------------

var = np.array([1,2,3,4])
print(var[0])
print(var[-1])

var = np.array([[1,2,3],[4,5,6]])
print(var[0])
print(var[0][1])
print(var[0,1])

var = np.array([[[1,2],[3,4]]])
print(var[0,1,0])


# Slicing
# ----------------

a = np.array([1,2,3,4,5,6,7,8])
print(a[1:3])
print(a[2:])
print(a[:7])
print(a[::2]) #see [a:b:c] here a is start b is end and c is steps result [1 3 5 7]

# for 2D array
var = np.array([[1,2,3,4,5],[4,5,6,7,8]])
print(var[1,1:5:2])

# Iteration in python

var = [[[1,2,3],[4,5,6]]]
for i in var:
    for j in i:
        for k in j:
            print(k)
# Here it takes too much code to iterate



# nditer in NumPy is an iterator used to efficiently loop over elements of a NumPy array.
# It is more powerful and flexible than a normal for loop because it can:

    # Work with multi-dimensional arrays
    # Control read/write behavior
    # Change iteration order
    # Work with multiple arrays simultaneously
    # It is mainly used when you want fine control over how arrays are traversed.

for i in np.nditer(var):
    print(i)
    

# np.nditer(var, flags=None, op_flags=None)

# | Parameter  | Meaning                         |
# | ---------- | ------------------------------- |
# | `array`    | NumPy array to iterate          |
# | `flags`    | Controls iteration behavior     |
# | `op_flags` | Controls read/write permissions |

# By default nditer is read-only.
# ----------------------------------
arr = np.array([1,2,3,4])

for x in np.nditer(arr, op_flags=['readwrite']):
    x[...] = x * 2

print(arr)

# x[...] modifies the original element.


# Iterating Multiple Arrays Together
# ---------------------------------------

a = np.array([1,2,3])
b = np.array([4,5,6])

for x, y in np.nditer([a, b]):
    print(x, y)
    
    # Controlling Iteration Order
# -----------------------------------

arr = np.array([[1,2],[3,4]])

for x in np.nditer(arr):
    print(x)
# Default: Row-major (C-order)

# to do in column major(Fortan Order)
for x in np.nditer(arr, order='F'):
    print(x)

# np.ndenumerate()  return (index,value)
# ---------------------

arr = np.array([[10,20],[30,40]])

for index, value in np.ndenumerate(arr):
    print(index, value)

# ndenumerate nd-> n dimension enumerate -> enumerate the elements with index and value
# (0, 0) 10
# (0, 1) 20
# (1, 0) 30
# (1, 1) 40