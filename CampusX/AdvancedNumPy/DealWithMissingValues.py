import numpy as np
arr = np.array([1, 2, np.nan, 4, 5])
# np.nan is a float → whole array becomes float
print(np.isnan(arr))  # returns a boolean array where True is for np.nan
c = arr[np.isnan(arr)]  # returns the np.nan values
d = arr[~np.isnan(arr)]  # returns the non np.nan values
print(c)  # [nan]
print(d)  # [1. 2. 4. 5.]
