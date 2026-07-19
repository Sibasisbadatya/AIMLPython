# set is collection of unordered items
# eac item should unique and immutable items

collection = {1,2,3,"sibasis","sibasis"}
print(type(collection))
print(collection)
print(len(collection)) 
# 4

null_set=set()
print(null_set)

# Methods
# add(element to add)
# remove(element to remove)
# .clear() to make set empty
# pop() remove random value

# So set is mutable but its element is immutable


# union and intersection

set1={1,2,3}
set2 ={2,2,4,5}
set3 = set1.union(set2)
print(set3)
set4 = set1.intersection(set2)
print(set4)
