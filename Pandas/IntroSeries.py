import pandas as pd
print(pd.__version__)

# It has 2 types of data structure
# 1.Series (1D Array) Series is called 1-dimensional (1D) because it has only one axis (one dimension) of data.
# 2.Data Frame (full table)


ser = pd.Series([1,2,3,4,5])
print(ser)


ser1 = pd.Series([1,2,3],index=['a','b','c'])
print(ser1)
ser2 = pd.Series([1,2,3],index=['a','b','c'],dtype='float',name='Python Pandas')
print(ser2)

# Creating multi same elements
mser = pd.Series(12,index=[1,2,3,4,5]) # see here there is no square bracket in 12
print(mser)


# Creating through Dictionary
dic = {
    "name":["Sibasis","Ansuman","Bhaskar"],
    "mark":[12,17,11],
    "rank":[2,1,3]
}

dSer = pd.Series(dic)
print(dSer)



# Addition
a1 = pd.Series(12,index=[1,2,3,4,5])
a2 = pd.Series(12,index=[1,2,3,])

print(a1+a2) # here there will be 24,24,24,NaN,NaN
# But in My NumPy there was broadcasting Exception occurs

# Indexing and Slicing
# ----------------------
iser = ser[2]
print(iser)