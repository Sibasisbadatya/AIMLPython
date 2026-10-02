import numpy as np

# speed and time
# -------------------------

# list
a = [i for i in range(1000000)]
b = [i for i in range(1000000,2000000)]
c=[]
import time
start = time.time()
for i in range(len(a)):
    c.append(a[i]+b[i])
# print(c)
print("Time taken for list: ", time.time() - start)

# numpy
a= np.arange(1000000)
b= np.arange(1000000,2000000)
start = time.time()
c = a + b
# print(c)
print("Time taken for numpy: ", time.time() - start)

# Result
# Time taken for list:  0.13322877883911133
# Time taken for numpy:  0.012811422348022461

# Internals of list

# a = [1, 2, 3, 4]

# Each element is a separate object
# Stored somewhere in memory
# List only stores addresses (pointers)

# List → [addr1, addr2, addr3, addr4]

# addr1 → 1
# addr2 → 2
# addr3 → 3
# addr4 → 4

# More memory used
# CPU has to jump around → slower

# How NumPy Array Works
# a = np.array([1, 2, 3, 4])
# [1 | 2 | 3 | 4]   (continuous memory)
# Everything is in one block
# CPU reads faster



# In terms of memory
# -------------------------

import sys
a = [i for i in range(1000000)]
print(sys.getsizeof(a))  # size of variable in bytes (8000112)

b = np.arange(1000000)
print(sys.getsizeof(b))  # size of variable in bytes (8000112)
# we get almost same size for both list and numpy(int 64 by default).bu in numpy we got flexibility to create arrays with different data types like int32 
c = np.arange(1000000, dtype=np.int32)
print(sys.getsizeof(c))  # size of variable in bytes (4000112)

