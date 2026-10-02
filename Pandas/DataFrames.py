# dataFrames in 2D data structures
import pandas as pd

var = pd.DataFrame([1,2,3,4,5])
print(var)
print(type(var))


# Creating through Dictionary
dic = {
    "name":["Sibasis","Ansuman","Bhaskar"],
    "mark":[12,17,11],
    "rank":[2,1,3]
}

# Instead of arrays in different keys we can pass pd.series() also

dvar = pd.DataFrame(dic)
print(dvar)

dvar = pd.DataFrame(dic,columns=["name","rank"]) #for selected column name
print(dvar)

dvar = pd.DataFrame(dic,columns=["name","rank"],index=['a','b','c']) # for custom row name(index)
print(dvar)

# if for each key the length of data array is differnet then it will throw error

# Accessing elements
print(dvar['name']['a']) #here i have to pass 'a' because i have changed  the index with alohabetical order (**index=['a','b','c']**)