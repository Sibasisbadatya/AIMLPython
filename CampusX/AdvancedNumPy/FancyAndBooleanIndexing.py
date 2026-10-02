import numpy as np
a = np.arange(12).reshape(4,3)

# [[ 0  1  2]
#  [ 3  4  5]
#  [ 6  7  8]
#  [ 9 10 11]]

# Here in normal indexing and slicing we can extract or select 1st row,2nd or 2nd,4th basically with some pattern

# But what if we want to select 1st and 3rd row and 4th row, we can do that with fancy indexing
# Fancy Indexing
# -------------------------
# Here we pass one list where we just specify the index of the rows we want to select
print(a[[0,2,3]])
# [[ 0  1  2]
#  [ 6  7  8]
#  [ 9 10 11]]

a = np.arange(24).reshape(4,6)

# [[ 0  1  2  3  4  5]
#  [ 6  7  8  9 10 11]
#  [12 13 14 15 16 17]
#  [18 19 20 21 22 23]]

# for 1st ,3rd and 4th
print(a[:,[1,3,4]])  # simply put : in row

# [[ 1  3  4]
#  [ 7  9 10]
#  [13 15 16]
#  [19 21 22]]


# Boolean Indexing
# -------------------------
# indexing for a condition, for example we want to select all the elements which are greater than 10
a = np.random.randint(1,100,24).reshape(4,6)
print(a>50) #returns the boolean array 
# [[False False False  True  True False]
#  [False  True  True False  True  True]
#  [ True False False False False False]
#  [ True False False False  True  True]]

print(a[a>50]) #returns the elements which are greater than 50

# [94 65 98 85 76 64 96 63 64] // here the boolean array got masked to original array and only the elements which are 
# True got selected and returned as output.

# for numbers not divisible by 7
print(a[a%7!=0])  #returns the elements which are not divisible by 7 or print(a[~(a%7==0)]) 

# above o/p are from randomly generated array, so it will be different for you when you run the code.

