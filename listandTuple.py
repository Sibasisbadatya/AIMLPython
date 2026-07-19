# 1. List in Python

# A list is an ordered and mutable collection.
# Ordered → elements keep their order
# Mutable → values can be changed
# Allows duplicate values

my_list = [1, 2, 3, 4]
nums = [10, 20, 30]

print(nums[0])   # access element
nums[1] = 50     # modify element

print(nums)

nums = [1,2,3]

nums.append(4)     # add element
nums.remove(2)     # remove element
nums.pop()         # remove last
nums.insert(1,10)  # insert at index


# 2. Tuple in Python

# A tuple is an ordered but immutable collection.
# Ordered
# Immutable → cannot change after creation
# Allows duplicates

nums = (10, 20, 30)

print(nums[1])
# nums[1] = 50
# TypeError: 'tuple' object does not support item assignment

# Why Tuples Exist
# Tuples are used when data should not change.

# Tuple Packing & Unpacking
point = (10,20)

x, y = point

print(x)
print(y)