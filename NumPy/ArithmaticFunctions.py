import numpy as np

var = np.array([1,2,3,5,2,1,3,4,6,7,6,4])

a = np.where(var/2==2)
print(a)

s = np.array([1,2,3,4,5,7,8,9])
pos = np.searchsorted(s,6,side="right")  #searchsorted works only under Binary search and it returns the place where the given e
# element can be inserted and side is the direction from where the searching will start
print(pos)

pos = np.searchsorted(s,[5,6,7])
print(pos)

# mp.sort() make the array sorted 1D or 2D


# Filter Array
# ------------------------
a = np.array([1,2,3,4])
f = [True,False,True,True]
print(a[f]) # [1,3,4]



# Join
# ------------------------

a=np.array([1,2,3,4])
b=np.array([5,6,7,8])

c=np.concatenate((a,b))
print(c)

# for 2D
a = np.array([[1,2],
              [3,4]])

b = np.array([[5,6],
              [7,8]])
print(np.concatenate((a,b),axis=0)) #along the axis 0 means vertically 1 means horizontally

# for 3D axis 0 means depth 1 means vertically and 2 means horizontaly


# Stack
# ---------------
# Unlike concatenate, which joins arrays along an existing axis, stack adds a new dimension.

a = np.array([1,2,3])
b = np.array([4,5,6])

result = np.stack((a,b))
print(result)
# [[1 2 3]
#  [4 5 6]]

# (2,3) #shape
print(np.stack((a,b), axis=1)) #along the axis 1

# | Feature           | concatenate      | stack              |
# | ----------------- | ---------------- | ------------------ |
# | Axis              | Existing axis    | New axis           |
# | Dimension change  | No               | Yes                |
# | Shape requirement | Same except axis | Exactly same shape |

# hstack ,vstack and dstack
# ------------------------

a = np.array([[1,2],
              [3,4]])

b = np.array([[5,6],
              [7,8]])

np.hstack((a,b)) #horizontal
# [[1 2 5 6]
#  [3 4 7 8]]

np.vstack((a,b)) #vertical
# [[1 2]
#  [3 4]
#  [5 6]
#  [7 8]]

np.dstack((a,b))  #depth
# [[[1 5]
#   [2 6]]

#  [[3 7]
#   [4 8]]]


# Split
# -------------
# np.split(array, sections, axis=0) format
a = np.array([1,2,3,4,5,6])

result = np.split(a, 3)
print(result)
print()
a = np.array([[1,2],
              [3,4],
              [5,6],
              [7,8]])

print(np.split(a,2))

a = np.array([[1,2,3,4],
              [5,6,7,8]])

print(np.split(a,2,axis=1))
# [[1 2]
#  [5 6]]

# [[3 4]
#  [7 8]]
# Here also vsplit hsplit and dsplit exists

# split at fixed positions
a = np.array([10,20,30,40,50])

np.split(a,[2,4])

# here [2,4] represents before indices 2 and 4 split should begin
# 1 split is like [:2],[2:4],[4:] 



# Shuffle
# ---------------
# modifies the original array
var = np.array([1,2,3,4,5])
np.random.shuffle(var)
print(var)

# unique
# ----------------

var = np.array([1,2,3,4,4,1,5,9])
u = np.unique(var)
print(u)

u = np.unique(var,return_index=True,return_counts=True) #counts give the no of counts for the unique elements repeated
print(u)

# Resize
# ------------------
re = np.resize(var,(2,4)) #resize the elements to newer dimenional format
print(re)

print(var)


# Flatten
# ---------------------------------
# In NumPy, flatten() is used to convert a multi-dimensional array into a one-dimensional (1D) array.
# It returns a copy of the array,
# array.flatten(order='C') syntax
# 'C' → row-wise (default)
# 'F' → column-wise

a = np.array([[1,2,3],
              [4,5,6]])

b = a.flatten()
print(b)
c=a.flatten(order='F')
print(c)

# Insert
# ---------------
a=np.array([1,2,3,4,5])
b = np.insert(a,2,19) #1st param is array 2nd is index and 3rd is value to be inserted
print(b)

# 2nd parameter can be tuple of multiple indexes
c=np.insert(a,(1,3,5),98)
print(c)

# for 2Dimensional
td = np.array([[1,2,3],[4,5,6]])
v1 = np.insert(td,2,5,axis=0) 
print(v1)
v1 = np.insert(td,2,5,axis=1) 
print(v1)
v1 = np.insert(td,2,[2,3],axis=1) # multiple data also can be inserted but make sure of the dimension

print(v1)

# Delete
a=np.array([1,2,3,4,5])
b=np.delete(a,1) #here 1 is the index of the array
print(b)
