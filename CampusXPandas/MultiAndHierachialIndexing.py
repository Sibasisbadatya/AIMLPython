import pandas as pd
import numpy as np

array = [
    ['North','South','North','South',],
    [2024,2025,2024,2025],
]


# Creating MultiIndex
# By creating MultiIndex from arrays we can apply Hierarchical Indexing to our DataFrame.
# Like we can represent 3Dimensional with the help of 2 dimensional DataFrame.

index = pd.MultiIndex.from_arrays(array, names=['Region', 'Year'])
# print(index)

# MultiIndex([('North', 2024),
#             ('SOuth', 2025),
#             ('North', 2024),
#             ('SOuth', 2025)],
#            names=['Region', 'Year'])
# Indexes are in tuple format and they are in pairs of Region and Year.

# print(type(index))
# <class 'pandas.MultiIndex'>

df = pd.DataFrame(
    np.random.randint(1,100,(4,2)),
    columns=['Sell1', 'Sell2'],
    index=index
)

# We are using random so results may be different when you run the code.
# print(df)

#              Sell1  Sell2
# Region Year
# North  2024       16        8
# SOuth  2025       40       95
# North  2024       43       53
# SOuth  2025       96       71

# Dimesnion 1 -> Region
# Dimesnion 2 -> Year
# Dimesnion 3 -> Sell1, Sell2

# Extra Index Level acts like a new dimension in the DataFrame. 
# It allows us to represent data in a more structured way, making it easier to analyze and manipulate. 
# We can perform operations on different levels of the index, 
# such as grouping by Region or Year, and we can also access specific subsets of the data based on the index values.


#              Sell1  Sell2
# Region Year
# North  2024       16        8
# SOuth  2025       40       95
# North  2024       43       53
# SOuth  2025       96       71

index = df.index
# print the index of the DataFrame
# print(index)

# MultiIndex([('North', 2024),
#             ('SOuth', 2025),
#             ('North', 2024),
#             ('SOuth', 2025)],
#            names=['Region', 'Year'])




columns = df.columns

# print the columns of the DataFrame
# print(columns)
# Index(['Sell1', 'Sell2'], dtype='str')


# Slice By Region
# ----------------------

north = df.loc['North']
# print(north)
#       Sell1  Sell2
# Year
# 2024     28     25
# 2024     27     85

# northAndSouth = df.loc['North':'South']
# print(northAndSouth)
# will not work because this slice will work if index are sorted
# ('North', 2024)
# ('North', 2025)
# ('South', 2024)
# ('South', 2025)

# Our order is
# ('North', 2024)
# ('South', 2025)
# ('North', 2024)
# ('South', 2025)

# Fix: Sort the MultiIndex 
# df = df.sort_index()



# Cross Section
# Cross section allows us to select data based on a specific level of the MultiIndex.
# For example, we can select all the data for the year 2024 across all regions
# ----------------------------------------------------------------------------------------

xs = df.xs('North',level='Region')
# print(xs)

#       Sell1  Sell2
# Year
# 2024     85      7
# 2024     29      7

# Slicing 
# ------------------------------------------------------------------------------

# year 2024 and all regions and all columns

# by df.loc and IndexSlice Method
alr24 = df.loc[pd.IndexSlice[:,2024],:]
# print(alr24)

#              Sell1  Sell2
# Region Year
# North  2024     62     51
#        2024     67     82

# by xs
alr24_xs = df.xs(2024, level='Year')
# print(alr24_xs)

#         Sell1  Sell2
# Region
# North      84     28
# North      93      8

# slice of Sell (Sell1)

# using loc
sell1 = df.loc[:, 'Sell1']
# print(sell1)

# Region  Year
# North   2024    75
# South   2025    29
# North   2024     9
# South   2025    77
# Name: Sell1, dtype: int32

# by xs
sell_xs = df.xs('Sell1', axis=1)
# print(sell_xs)

# Region  Year
# North   2024    77
# South   2025    16
# North   2024    60
# South   2025    88
# Name: Sell1, dtype: int32

# Accessing 2024 data of south
south_2024 = df.loc[('South', 2025)]
# print(south_2024)

#              Sell1  Sell2
# Region Year
# South  2025     36     24
#        2025     70     72

# by xs
south_2024_xs = df.xs(('South', 2025))
# print(south_2024_xs)
#              Sell1  Sell2
# Region Year
# South  2025     72     90
#        2025      2     43


# GROUP BY
# ------------------------------------------------------------------------------

regionGrouped = df.groupby(level='Region').sum()
# print(regionGrouped)

#         Sell1  Sell2
# Region
# North     123    101
# South      86     89

regionGrouped = df.groupby(level='Year').sum()
# print(regionGrouped)

#       Sell1  Sell2
# Year
# 2024     95     56
# 2025     46     74

# Resetting Index
# ------------------------------------------------------------------------------

reset_Index = df.reset_index()
# print(reset_Index)

#   Region  Year  Sell1  Sell2
# 0  North  2024     28     94
# 1  South  2025     27      5
# 2  North  2024     29     79
# 3  South  2025     83     95







