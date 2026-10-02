# Broadcastong
# --------------------------
import numpy as np
var1 = np.array([1,2,3,4])
var2 = np.array([2,3,4])
# here broadcasting will due to size mismatch

# Broadcasting is a mechanism that lets NumPy perform operations on arrays of 
# different shapes by automatically expanding the smaller array to match the larger one.

import numpy as np

a = np.array([1,2,3])
b = 2

print(a + b)

# what happens intenally
# [1 2 3]
# +
# [2 2 2]   ← broadcasted



# with different dimesnsions

a = np.array([[1],[2],[3]])
b = np.array([10,20,30])

print(a + b)

# a =          b =

# [[1]         [10 20 30]
#  [2]
#  [3]]

# Broadcasted:
# It automatically expands the smaller array across the larger array so element-wise operations can be performed.
# [[1 1 1]
#  [2 2 2]
#  [3 3 3]]

# +
# [[10 20 30]
#  [10 20 30]
#  [10 20 30]]

# Broadcasting Rules (Important)

# NumPy compares shapes from right to left.

# Two dimensions are compatible if:

# 1️⃣ They are equal, OR
# 2️⃣ One of them is 1

# Result shape will be the max of each compare

# like for 1*4 and 5*1 so max of(4 and 1) is 4 and max 0f(1 and 5) is 5 so result is 5*4