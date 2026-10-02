from matplotlib import axis
import numpy as np
# Sort in normal list in python
arr = [5, 2, 9, 1]
arr.sort() # This will sort the list in place, modifying the original list
print(arr)   # [1, 2, 5, 9]

new_arr = sorted(arr) # This will return a new sorted list, leaving the original list unchanged
print(new_arr)  # [1, 2, 5, 9]

arr.sort(reverse=True)# This will sort the list in descending order
print(arr)   # [9, 5, 2, 1]

arr = [(1, 3), (2, 1), (4, 2)]

arr.sort(key=lambda x: x[1]) # This will sort the list of tuples based on the second element of each tuple
print(arr)


# Sorting in numpy arrays
# ------------------------------------------

arr = np.array([5, 2, 9, 1])
sorted_arr = np.sort(arr) # This will return a new sorted array, leaving the original

# in 2D arrays, we can specify the axis along which to sort
# arr = np.random.randint(100, size=(4, 4))
arr = np.array([
    [3, 1, 9],
    [6, 8, 5]
])
print(arr)

sorted_arr = np.sort(arr, axis=0) 
print(sorted_arr)
# [[3 1 5]
#  [6 8 9]]

sorted_arr = np.sort(arr, axis=1) 
print(sorted_arr)
# [[1 3 9]
#  [5 6 8]]


# for reverse sort
# ----------------------------

# [3, 1, 9],
# [6, 8, 5]
# This is arr

reversed_row = np.sort(arr)[::-1] #reverses rows (by default it sorts along last axis)

# Shape: (2, 3)
# Axes:
# axis 0 → rows
# axis 1 → columns
# 👉 Last axis = 1

# [::-1]
print("Reversed Row Sort:")
print(reversed_row)
# [[5 6 8]
#  [1 3 9]]

reversed_col = np.sort(arr, axis=0)[::-1] #reverses columns 
print("Reversed Column Sort:")
print(reversed_col)
# [[6 8 9]
#  [3 1 5]]

print(sorted_arr)


# Append in NumPy arrays
# ------------------------------------------
arr = np.array([1, 2, 3])
new_arr = np.append(arr, 4) # This will return a new array with the new element added at the end
print(new_arr)  # [1, 2, 3, 4]
arr = np.array([
    [3, 1, 9],
    [6, 8, 5]
])
new_arr = np.append(arr,np.random.rand(arr.shape[0],1),axis=1) 
new_arr =np.append(arr,np.random.rand(1,arr.shape[1]),axis=0) 
print(new_arr)


# concatenate in NumPy arrays
# ------------------------------------------
# it helps many arrats to append at once, and also we can specify the axis along which to concatenate
a = np.arange(6).reshape(2,3)
b = np.arange(6,12).reshape(2,3)
d = np.arange(12,18).reshape(2,3)
c = np.concatenate((a, b), axis=0) # Concatenate along rows
print(c)
e = np.concatenate((a,b, d), axis=1) # Concatenate along columns
print(e)

# unique elements in numpy arrays
#  -------------------------------------------

arr = np.array([1, 2, 2, 3, 4, 4, 5])
unique = np.unique(arr) # This will return a new array containing only the unique elements from the original array
print(unique)  # [1, 2, 3, 4, 5]

# expand dimensions
# ---------------------------
#it is used to add a new axis to an array, which can be useful for broadcasting and reshaping operations
print("Expand Dimensions:")
a = np.array([1, 2, 3])
print(a.shape) # (3,) #No rows no columns, just a 1D array
b = np.expand_dims(a, axis=0) # 
print(b) # [[1 2 3]]
print(b.shape) # (1, 3)
c = np.expand_dims(a, axis=1)
print(c) # [[1] [2] [3]]
print(c.shape) # (3, 1)


# Where
# -------------------------------------------
a = np.array([1, 2, 3, 4, 5])
b = np.where(a > 3) # This will return the indices of the elements in the array that satisfy the condition
print(b)  # (array([3, 4]),) - indices of elements greater than 3

# replace with where
# --------------------------------------------
c = np.where(a > 3, a, 0) # This will return a new array where the elements that satisfy the condition are kept,
# and the others are replaced with 0

# 1st parameter is the condition,
# 2nd parameter is the value to keep if the condition is true,
# and 3rd parameter is the value to replace if the condition is false
print(c)  # [0, 0, 0, 4, 5]


# Argmax and Argmin
# -------------------------------------------
# return the indices of the maximum and minimum values in an array, respectively
arr = np.array([1, 3, 2, 5, 4])
max_index = np.argmax(arr) # This will return the index of the maximum value in the array
min_index = np.argmin(arr) # This will return the index of the minimum value in the array
print(max_index)  # 3 (index of the value 5)
print(min_index)  # 0 (index of the value 1)

# for 2D arrays, we can specify the axis along which to find the argmax and argmin
arr = np.array([
    [3, 1, 9],
    [6, 8, 5]
])
max_index_row = np.argmax(arr, axis=0) # This will return the indices of the maximum values along the columns
min_index_row = np.argmin(arr, axis=0) # This will return the indices of the minimum values along the columns
print(max_index_row)  # [1 1 0] (indices of the maximum values in each column)
print(min_index_row)  # [0 0 1] (indices of the minimum values in each column)

# Cumulative sum and cumulative product
# -------------------------------------------
# cumulative sum is the sum of all the previous elements in the array,
# and cumulative product is the product of all the previous elements in the array
arr = np.array([1, 2, 3, 4])
cumsum = np.cumsum(arr)
cumprod = np.cumprod(arr)
print(cumsum)  # [ 1  3  6 10] (cumulative sum)
print(cumprod)  # [ 1  2  6 24] (cumulative product)

# for 2D
a = np.array([
    [1, 2, 3],  
    [4, 5, 6]
])
cumsum = np.cumsum(a)
#it simply flattens the array and then computes the cumulative sum meaning normally for 
# all function where we need to give axis, if we dont give it will flatten the array and then perform the operation.

print(cumsum)  # [ 1  3  6 10 15 21] (cumulative sum of the flattened array)
cumsum_axis0 = np.cumsum(a, axis=0) # This will compute the cumulative sum along the columns
cumsum_axis1 = np.cumsum(a, axis=1) # This will compute the cumulative sum along the rows
print(cumsum_axis0)  # [[ 1  2  3] [ 5  7  9]] (cumulative sum along columns)
print(cumsum_axis1)  # [[ 1  3  6] [ 4  9 15]] (cumulative sum along rows)


# percentile
# -------------------------------------------
# The percentile function in NumPy is used to compute the nth percentile of the data along a specified axis.
# The nth percentile is the value below which n% of the data falls. For example, 
# the 50th percentile (also known as the median) is the value below which 50% of the data falls.

arr = np.array([12, 45, 78, 3, 90, 34, 67, 21, 56, 89,
                10, 44, 32, 76, 88, 54, 23, 65, 7, 99])
percentile = np.percentile(arr,100)
print(percentile)  
#100th percentile is the maximum value in the array, which is 99 in this case.
#50th percentile (median) is the value below which 50% of the data falls, which is 45 in this case.


# histogram
# --------------------------------------------
# The histogram function in NumPy is used to compute the histogram of a set of data.
# A histogram is a graphical representation of the distribution of a dataset.

arr = np.array([12, 45, 78, 3, 90, 34, 67, 21, 56, 89,
                10, 44, 32, 76, 88, 54, 23, 65, 7, 99])
hist, bin_edges = np.histogram(arr, bins=5) # This will compute the histogram of the data with 5 bins
print(hist)  # [4 5 5 4 2] (number of elements in each bin)
print(bin_edges)  # [ 3.  22.2 41.4 60.6 79.8 99.] (edges of the bins)
# bin_edges gives the edges of the bins, which can be used to understand the range of values in each bin.
# for example,
# the first bin includes values from 3 to 22.2, the second bin includes values from 22.2 to 41.4, and so on.

c = np.histogram(arr, bins=[0,10,20,30,40,50,60,70,80,90,100])
print(c)

# corrcoeff
# --------------------------------------------
# np.corrcoef() is used to find the correlation between variables
# +1 indicates a perfect positive correlation,
# -1 indicates a perfect negative correlation,
# and 0 indicates no correlation.

salary = np.array([50000, 60000, 55000, 80000, 75000])
experience = np.array([1, 2, 3, 4, 5])
correlation = np.corrcoef(salary, experience)
print(correlation)
# represented as
#             salary    experience
# salary      1.0          0.85518611
# experience  0.85518611   1.0

# Isin
# --------------------------------------------
# The np.isin() function in NumPy is used to check if elements of one array are present in another array.
arr1 = np.array([1, 2, 3, 4, 5])
arr2 = np.array([3, 4, 5, 6, 7])
isin_result = np.isin(arr1, arr2) # This will return a boolean array indicating 
# whether each element of arr1 is present in arr2
print(isin_result)  # [False False  True  True  True] (3, 4, and 5 are present in arr2)
print(arr1[isin_result])  # [3 4 5] (elements of arr1 that are present in arr2)

# so here the isin_result(boolean array) is used to index arr1, 
# which returns the elements of arr1 that are present in arr2.

# Flip
# --------------------------------------------
# The np.flip() function in NumPy is used to reverse the order of elements in an array along a specified axis.
arr = np.array([[1, 2, 3],
                [4, 5, 6]])
flipped_arr = np.flip(arr, axis=0) # This will flip the array along the first axis (rows)
print(flipped_arr)  # [[4 5 6] [1 2 3]] (rows are flipped)
flipped_arr = np.flip(arr, axis=1) # This will flip the array along the second axis (columns)
print(flipped_arr)  # [[3 2 1] [6 5 4]] (columns are flipped)   


# Put
# --------------------------------------------
# The np.put() function in NumPy replaces specifice elements of array with given values of given array
# based on specified indices. 
# It modifies the original array in place.
# Array works on indexed flattened array.
arr = np.array([1, 2, 3, 4, 5])
np.put(arr,[0,1],[1000,2000]) # This will replace the elements at indices 0 and 1 with 1000 and 2000, respectively
# 1st parameter is the array to modify,
# 2nd parameter is the indices of the elements to replace,
# 3rd parameter is the values to put at the specified indices
print(arr)  # [1000 2000    3    4    5] (elements at indices 0 and 1 are replaced with 1000 and 2000)


# Delete
# --------------------------------------------
# returns the new array with the specified subarray deleted.
arr = np.array([1, 2, 3, 4, 5])
deleted_arr = np.delete(arr, [0, 1]) # This will return a new array with the elements at indices 0 and 1 deleted
# 1st parameter is the array to modify,
# 2nd parameter is the indices of the elements to delete
print(arr)  # [1 2 3 4 5] (original array remains unchanged)
print(deleted_arr)  # [3 4 5] (elements at indices 0 and 1 are deleted)



# Set FUnctuions
# --------------------------------------------
# np.union1d()
# this function returns the unique, sorted array of values that are in either of the two input arrays'.

# np.intersect1d()
# this function returns the unique, sorted array of values that are in both of the input arrays.

# np.setdiff1d()
# this function returns the unique, sorted array of values that are in the first input array but not in the second input array.

# np.setxor1d()
# this function returns the unique, sorted array of values that are in either of the input arrays but not in both (the symmetric difference of the two arrays).
# all elements - elements in both arrays(np,intersect1d) = elements in either of the arrays but not in both (np.setxor1d)


# Clip
# --------------------------------------------
# The np.clip() function in NumPy is used to limit the values in an array to a specified range.
arr = np.array([1, 2, 3, 4, 5])
clipped_arr = np.clip(arr, 2, 4) # This will return a new array where all values less than 2 are set to 2, and all values greater than 4 are set to 4
print(clipped_arr)  # [2 2 3 4 4] (values less than 2 are set to 2, and values greater than 4 are set to 4)
clipped_arr = np.clip(arr,a_min=2, a_max=4)
# another way to write
