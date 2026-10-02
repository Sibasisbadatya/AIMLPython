import pandas as pd
import numpy as np
# Creating a Series
series = pd.Series([10, 20, 30, 40, 50])
# print(series)

# with labels
sl = pd.Series([10, 20, 30, 40, 50], index=['a', 'b', 'c', 'd', 'e'])
# print(sl)
# a    10
# b    20
# c    30
# d    40
# e    50


# DataFrames

df = pd.DataFrame({
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
    'Age': [25, 30, 35, 40, 45],
    'City': ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix']
})
# print(df)

# Head and Tail
# print(df.head(3)) #first 3 rows ,by default it shows first 5 rows
# print(df.tail(2)) #last 2 rows ,by default it shows last 5 rows


# PANDAS Data Types
# -----------------------------------------------------------------------------

# print(df.dtypes)
# Name      str
# Age     int64
# City      str
# dtype: object

# Here we can reduce the memory usage by converting the data types of the columns to more efficient types.
# for example in padas numbers by default take 64 bits but we can convert 8 or 16 where age range normally lies for humans.

df['Age'] = df['Age'].astype('int8')
# print(df.dtypes)

# Index Column and Labels in DataFrames
# ------------------------------------------------------------------------------
# Column Property
# print(df.columns) # it shows the column labels of the DataFrame.

# Row Identifier
# print(df.index) 

# it shows the row labels (index) of the DataFrame. By default, it is a RangeIndex starting from 0.
# RangeIndex(start=0, stop=5, step=1)


# Columns are labels for each vertical series in dataframe
# but labels are for both row and columns.


a = np.random.randint(1,100,20).reshape(5,4)

row_labels = ['row1', 'row2', 'row3', 'row4', 'row5']
column_labels = ['col1', 'col2', 'col3', 'col4']

pdata = pd.DataFrame(data=a,index=row_labels,columns=column_labels)
# print(pdata)

# Shape
# print(pdata.shape) # it shows the number of rows and columns in the DataFrame as a tuple (number_of_rows, number_of_columns).

# Description of DataFrame
# -------------------------------------------------------------------------------

# print(pdata.describe()) 

# it provides a statistical summary of the numerical columns in the DataFrame, 
# including count, mean, standard deviation, minimum, 25th percentile, median (50th percentile), 75th percentile, 
# and maximum values. It is useful for understanding the distribution and central tendency of the data.

# Accesing a single coulumn
# -----------------------------------------------------------------------------
# Will be a Series

# print(pdata['col1'])

# row1    15
# row2    19
# row3    72
# row4    29
# row5    17
# Name: col1, dtype: int32
# it returns the 'col1' column as a Series. 
# The output will be a pandas Series containing the values of the 'col1' column, along with the corresponding row labels (index).


# Multiple Columns Access
# - Will be a DataFrame

# print(pdata[['col1', 'col3']])

#       col1  col3
# row1    56    41
# row2     2    57
# row3    19    57
# row4    56    70
# row5     6    31


# Drop a Column 
# - inplace = True will drop the column permanently from the dataframe
# - inplace = False will return a new dataframe with the column dropped but original dataframe will remain unchanged
dropped = pdata.drop('col2', axis=1, inplace=False)
# print(dropped)
#       col1  col3  col4
# row1     9    68    53
# row2    57    91    26
# row3    33    48    84
# row4    58    38    85
# row5    37    63    89
# print(pdata)

# Drop a Row
# - inplace = True will drop the row permanently from the dataframe
# - inplace = False will return a new dataframe with the row dropped but original dataframe will remain unchanged

dropped_row = pdata.drop('row3', axis=0, inplace=False)

# print(dropped_row)


# Selecting Rows
# -----------------------------------------------------------------------------

# label based selection (loc) and position based selection (iloc)

# print(pdata.loc['row2']) 

# col1    40
# col2    96
# col3    25
# col4    78
# Name: row2, dtype: int32

# print(pdata.loc[['row2','row4']]) #multiple index



# print(pdata.iloc[1])

# col1    14
# col2    45
# col3     7
# col4    70
# Name: row2, dtype: int32

# print(pdata.iloc[1,2]) #multiple index


# Slicing by rows
# -----------------------------------------------------------------------------
# print(pdata.loc['row2':'row4']) # it includes both row2 and row4
# print(pdata.iloc[1:4]) # it includes row2 and row3 but not row4

# Slicing by columns
# -----------------------------------------------------------------------------
# print(pdata.loc[:, 'col2':'col4']) # it includes both col2 and col4

#       col2  col3  col4
# row1    77    65    65
# row2    49    27     5
# row3    57    37    89
# row4    82    74    12
# row5    51    20    17

# print(pdata.iloc[:, 1:4]) # it includes col2 and col3 but not col4

#       col2  col3  col4
# row1    77    65    65
# row2    49    27     5
# row3    57    37    89
# row4    82    74    12
# row5    51    20    17

# Subsetting by condition
# -----------------------------------------------------------------------------
arr = np.random.randint(1,100,20).reshape(5,4)
row_labels =['A','B','C','D','E']
column_labels =['W','X','Y','Z']
pdata = pd.DataFrame(data=arr,index=row_labels,columns=column_labels)

# element at row B to col Y
element = pdata.loc['B', 'Y']
# 1st is row and 2nd is column


# Subset comprising of row  B and D and columns X and Z
# -----------------------------------------------------------------------------
element_subset = pdata.loc[['B', 'D'], ['X', 'Z']]


# Subsetting based on condition
# -----------------------------------------------------------------------------
# condition that value >40
print(pdata>40) #returns boolean values table

booldf = pdata>40
datas = pdata[booldf]
# print(datas)
# #returns the values which are greater than 40 and rest will be NaN

df = pd.DataFrame({
    "Age": [21, 25, 30, 28, 22],
    "Height": [170, 165, 180, 175, 168],  # cm
    "Weight": [65, 70, 80, 75, 60]        # kg
})

# filter height >170
fheight = df[df['Height'] > 170]
# print(fheight)

#    Age  Height  Weight
# 2   30     180      80
# 3   28     175      75

# filter height >170 and weight >70
fheight_weight = df[(df['Height'] > 170) & (df['Weight'] > 70)]
print(fheight_weight)
#    Age  Height  Weight
# 2   30     180      80
# 3   28     175      75


arr = np.random.randint(1,100,20).reshape(5,4)
row_labels =['A','B','C','D','E']
column_labels =['W','X','Y','Z']
pdata = pd.DataFrame(data=arr,index=row_labels,columns=column_labels)

# Resetting Index
# -----------------------------------------------------------------------------
# Meaning resetiing row index from custom labels to default 0,1,2,3,4

# print(pdata.index)
# Index(['A', 'B', 'C', 'D', 'E'], dtype='str')

dropped_data = pdata.reset_index()

# print(dropped_data)
#   index   W   X   Y   Z
# 0     A  10  48  65  90
# 1     B  94  92  94  40
# 2     C  41  44  88  74
# 3     D  74   5  19  39
# 4     E  32  61  50   9

# to remove 1 extra added column Index

dropped_data = pdata.reset_index(drop=True)

# print(dropped_data)
#     W   X   Y   Z
# 0  41  53  79  73
# 1  32  52  68   3
# 2  52  28   5   9
# 3  54  98  38  30
# 4  58  19  16  37



# Adding a new row
# -----------------------------------------------------------------------------
pdata.loc['F'] = [10, 20, 30, 40]
# print(pdata)

#     W   X   Y   Z
# A  98  26  48  32
# B  28  95  28  17
# C  88  13  95  50
# D  47  89  37  40
# E  10  89  60  58
# F  10  20  30  40

# Adding a new column
# -----------------------------------------------------------------------------
pdata['NewCol'] = [1, 2, 3, 4, 5, 6]
# print(pdata)

#     W   X   Y   Z  NewCol
# A  98  26  48  32       1
# B  28  95  28  17       2
# C  88  13  95  50       3
# D  47  89  37  40       4
# E  10  89  60  58       5
# F  10  20  30  40       6

df = pd.DataFrame({
    "Age": [21, 25, 30, 28, 22],
    "Height": [170, 165, 180, 175, 168],  # cm
    "Weight": [65, 70, 80, 75, 60]        # kg
})

# Adding a new column based on existing columns
# -----------------------------------------------------------------------------
df['BMI'] = df['Weight'] / (df['Height'] / 100) ** 2
# print(df)
#    Age  Height  Weight        BMI
# 0   21     170      65  22.491349
# 1   25     165      70  25.711662
# 2   30     180      80  24.691358
# 3   28     175      75  24.489796
# 4   22     168      60  21.258503


# Set one column as index
# -----------------------------------------------------------------------------
indexed_df = df.set_index('Age', inplace=False)
# print(indexed_df)

# print(indexed_df['Age']) # it will give error because Age is no longer a column but it is now index

# Age is no longer a column
    #  Height  Weight        BMI
# Age
# 21      170      65  22.491349
# 25      165      70  25.711662
# 30      180      80  24.691358
# 28      175      75  24.489796
# 22      168      60  21.258503




# Rename the index of row and column
indexed_df.index = ['A', 'B', 'C', 'D', 'E']
indexed_df.columns = ['Height_cm', 'Weight_kg', 'BMI_value']
# print(indexed_df)

#    Height_cm  Weight_kg  BMI_value
# A        170         65  22.491349
# B        165         70  25.711662
# C        180         80  24.691358
# D        175         75  24.489796
# E        168         60  21.258503