# advantage of array over list

# consumes less memory
# fast compared to python list
# convinient to use
# wide mathematical operations


# List [1,2,3,4]

# Array [1 2 3 4]

import numpy as np

x=np.array([1,2,3,4])
print(x)
print(type(x))

y=[1,2,3,4]
print(y)
print(type(y))

# NumPyArray VS Python List
# python list can consist of many data types but not in numpy array
# numpy array works as matrix format which is help for image processing which works as matrics form
# numpy array has less modification functionas as  compared to list
# numpy array consumes less memory
# %timeit gives time taken for 1 line execution and %%time for full programme in jupyter ot google collab

# np.arange(start, stop, step) in NumPy
# Default start = 0
# Step = 1


# Functions of NumPy arrays

# create array .create(list)
a=np.array([1,2,3])
print(type(a))  
# <class 'numpy.ndarray'>

# dimensions in array
# to check dimensions -> .ndim
print(a.ndim) # 1

# creating 2 dimension
arr2 = np.array([[1,2,3,4],[1,2,3,4]]) # all should be same data type and indivisual list must have proper dimension
print(arr2)
print(arr2.ndim) # 2

# creating 3D
arr3 = np.array([[[1,2,3,4],[1,2,3,4],[1,2,3,4]]])
print(arr2)
print(arr3.ndim) #3

# we call 1D as vector, 2D as matrix and 3D as tensor

#creating in dynamic dimension
arrn = np.array([1,2,3,4],ndmin=10)
print(arrn)


# Creation of NumPy Array
# ---------------------------------

print("ZEROS")
# Zeros
zeros = np.zeros(4)
zeros1 = np.zeros((3,4))  # 1st param is dimension second is element

# Ones
ones = np.ones(4)

print(zeros)
print(zeros1)
print(ones)

# Empty
empty = np.empty(4) #The values inside are uninitialized(random/garbage values) (whatever was already in that memory).
print(empty)

# Range Values
range = np.arange(4)
print(range)

# Diagonal Values  creates identity matrix
diag = np.eye(3)
print("Diagonal Eyes")
print(diag)

customDiag = np.eye(3,5) # row*col
print(customDiag)

# Linespace
linspc = np.linspace(0,10,num=5)  #Here it give s 5 elements evenly spaced starting from 1 to 10 
print(linspc)

#Creating With Random Numbers
# --------------------------------------------

# rand() used to generate a random value btn (0 to 1)
randNo = np.random.rand()
randNo = np.random.rand(4) # 4 random no in 1 dimension
randNo = np.random.rand(2,3) # random no in 2*3 dimenssion
print(randNo)
randNo

# randn() used to generate a value close to 0 may be +ve or -ve and same as rand()

# ranf() used to generate random values from [0,1) include 0 and exclude 1

# randint() generate random integer values from given range (minValue,maxValue,total_num)
randInt = np.random.randint(2,100,10) 






