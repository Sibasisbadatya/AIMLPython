import pandas as pd
import numpy as np

df = pd.DataFrame({
    'A': [1, 2, np.nan],
    'B': [4, np.nan, np.nan],
    'C': [7, 8, 9]
})

# np.nan is a float reprsents missing,undefined or null data.

# print(df)

# adding a column
df['country'] = "IND ENG AUS".split()
# print(df)

# Adding a row
df.loc[3] = [10, 11, 12,"AUS"]
# print(df)

#       A     B   C country
# 0   1.0   4.0   7   India
# 1   2.0   NaN   8     Eng
# 2   NaN   NaN   9     Aus
# 3  10.0  11.0  12     AUS

indexed = df.set_index('country')
# print(df)

# Check if for NaN values
ndf = df.isna()
# print(ndf)
#        A      B      C  country
# 0  False  False  False    False
# 1  False   True  False    False
# 2   True   True  False    False
# 3  False  False  False    False

# check for not NaN values
ndf = df.notna()
# print(ndf)
#        A      B     C  country
# 0   True   True  True     True
# 1   True  False  True     True
# 2  False  False  True     True
# 3   True   True  True     True


# handling with missing values
# ---------------------------------------------------------------------
# df =

#       A     B   C country
# 0   1.0   4.0   7   India
# 1   2.0   NaN   8     Eng
# 2   NaN   NaN   9     Aus
# 3  10.0  11.0  12     AUS

# drop if nan exists
dropped0 = df.dropna() #drop the rows which have at least one NaN value
# print(dropped0)
#       A     B   C country
# 0   1.0   4.0   7   India
# 3  10.0  11.0  12     AUS
# Here default axis is 0. like .dropna(axis=0)

dropped1 = df.dropna(axis=1) #drop the columns which have at least one NaN value
# print(dropped1)
#     C country
# 0   7   India
# 1   8     Eng
# 2   9     Aus
# 3  12     AUS


# dropping with a threshold condition

thdrop = df.dropna(axis=0,thresh=3)
# tells keep the rows which have at least 3 non-NaN values
# print(thdrop)
thdrop1 = df.dropna(axis=1,thresh=3)
# tells keep the columns which have at least 3 non-NaN values
# print(thdrop1)




# Filling NaN values
# ------------------------------------------------------------------------

filledf = df.fillna(df['C'].mean())
# print(filledf)
#       A     B   C country
# 0   1.0   4.0   7   India
# 1   2.0   9.0   8     Eng
# 2   9.0   9.0   9     Aus
# 3  10.0  11.0  12     AUS


# Categorical Operations
# -------------------------------------------------------------------------------
# COnverting columns to category can increase memory efficiency

df['country'] = df['country'].astype('category')
# print(df)
# converted and original will look similar but the type got converted(changed)

categories = df['country'].cat.categories
# Shows all categories
# Index(['AUS', 'ENG', 'IND'], dtype='str')
# print(categories)


codes = df['country'].cat.codes
# print(codes)

# 0    2
# 1    1
# 2    0
# 3    0
# dtype: int8

# codes are per row not category
# Here see the type convrted to int8 from string which saves memory

data = {
    "employee_id": [101, 102, 103, 104, 105, 106, 107, 108],
    "name": ["Amit", "Ravi", "John", "Sara", "Ankit", "Priya", "David", "Neha"],
    "department": ["IT", "HR", "IT", "Finance", "HR", "IT", "Finance", "HR"],
    "country": ["India", "India", "USA", "UK", "India", "USA", "UK", "India"],
    "salary": [70000, 50000, 80000, 90000, np.nan, 75000, 88000, 52000],
    "experience": [3, 2, 5, 7, 1, 4, 6, 2],
    "rating": [4.5, 3.8, 4.2, 4.9, 3.5, 4.0, 4.7, np.nan]
}

cdf = pd.DataFrame(data)
# print(cdf)

#    employee_id   name department country   salary  experience  rating
# 0          101   Amit         IT   India  70000.0           3     4.5
# 1          102   Ravi         HR   India  50000.0           2     3.8
# 2          103   John         IT     USA  80000.0           5     4.2
# 3          104   Sara    Finance      UK  90000.0           7     4.9
# 4          105  Ankit         HR   India      NaN           1     3.5
# 5          106  Priya         IT     USA  75000.0           4     4.0
# 6          107  David    Finance      UK  88000.0           6     4.7
# 7          108   Neha         HR   India  52000.0           2     NaN

# Grouping and Aggregation
# -------------------------------------------------------------------------------
grouped = cdf.groupby('department') 
# print(grouped)

# “groupby without aggregation = no visible result”
groupedMean = grouped.salary.mean()
# print(groupedMean)

# Finance    89000.0
# HR         51000.0
# IT         75000.0

# like wise we call any aggregate functions here

# print(grouped.describe())
#                  count        mean       std    min     25%    50%     75%    max  count  ...        max  count      mean       std  min    25%   50%    75%  max
# department                                                                                ...                                                                    
# Finance            2.0  105.500000  2.121320  104.0  104.75  105.5  106.25  107.0    2.0  ...        7.0    2.0  4.800000  0.141421  4.7  4.750  4.80  4.850  4.9
# HR                 3.0  105.000000  3.000000  102.0  103.50  105.0  106.50  108.0    2.0  ...        2.0    2.0  3.650000  0.212132  3.5  3.575  3.65  3.725  3.8
# IT                 3.0  103.333333  2.516611  101.0  102.00  103.0  104.50  106.0    3.0  ...        5.0    3.0  4.233333  0.251661  4.0  4.100  4.20  4.350  4.5

# [3 rows x 32 columns]


# Concatanation 
# -------------------------------------------------------------------------------
df1 = pd.DataFrame({
    "emp_id": [101, 102, 103],
    "name": ["Amit", "Ravi", "John"],
    "salary": [70000, 50000, 80000]
})

df2 = pd.DataFrame({
    "emp_id": [104, 105],
    "name": ["Sara", "Neha"],
    "salary": [90000, 60000]
})

concated = pd.concat([df1,df2],axis=0)
# print(concated)
# default is along axis = 0
#    emp_id  name  salary
# 0     101  Amit   70000
# 1     102  Ravi   50000
# 2     103  John   80000
# 0     104  Sara   90000
# 1     105  Neha   60000

concated1 = pd.concat([df1,df2],axis=1)
# print(concated1)
#    emp_id  name  salary  emp_id  name   salary
# 0     101  Amit   70000   104.0  Sara  90000.0
# 1     102  Ravi   50000   105.0  Neha  60000.0
# 2     103  John   80000     NaN   NaN      NaN




# Merging and Joining
# -------------------------------------------------------------------------------

employees = pd.DataFrame({
    "emp_id": [101, 102, 103, 104, 105],
    "name": ["Amit", "Ravi", "John", "Sara", "Neha"],
    "dept_id": [1, 2, 1, 3, 2],
    "salary": [70000, 50000, 80000, 90000, 60000]
})


departments = pd.DataFrame({
    "dept_id": [1, 2, 3, 4],
    "dept_name": ["IT", "HR", "Finance", "Marketing"]
})

bonus = pd.DataFrame({
    "emp_id": [101, 103, 104, 106],  
    "bonus": [5000, 7000, 6000, 4000]
})

# Syntax of merge
# ------------------------------------------------------------------------
# pd.merge(
#     leftDataFrame,
#     rightDataFrame,
#     how='inner', # type of merge
#     on='key_column', # column name on which merge is to be performed
#     left_on='left_key_column', # if key column name is different in left dataframe
#     right_on='right_key_column' # if key column name is different in right dataframe
#     left_index=True, # if key column is index in left dataframe
#     right_index=True # if key column is index in right dataframe
#     suffixes=('_left', '_right') # to handle overlapping column names in left and right dataframes
# )


# Inner Merge
# -----------------------------------------------------------------------
innerdata = pd.merge(employees, departments, on='dept_id', how='inner')
# print(innerdata)
#    emp_id  name  dept_id  salary dept_name
# 0     101  Amit        1   70000        IT
# 1     102  Ravi        2   50000        HR
# 2     103  John        1   80000        IT
# 3     104  Sara        3   90000   Finance
# 4     105  Neha        2   60000        HR

left = pd.merge(employees, departments, on='dept_id', how='left')
# print(left)

#    emp_id  name  dept_id  salary dept_name
# 0     101  Amit        1   70000        IT
# 1     102  Ravi        2   50000        HR
# 2     103  John        1   80000        IT
# 3     104  Sara        3   90000   Finance
# 4     105  Neha        2   60000        HR

right = pd.merge(employees, departments, on='dept_id', how='right')
# print(right)

#    emp_id  name  dept_id   salary  dept_name
# 0   101.0  Amit        1  70000.0         IT
# 1   103.0  John        1  80000.0         IT
# 2   102.0  Ravi        2  50000.0         HR
# 3   105.0  Neha        2  60000.0         HR
# 4   104.0  Sara        3  90000.0    Finance
# 5     NaN   NaN        4      NaN  Marketing

# on on parameter we can pass key array also

employees = pd.DataFrame({
    "emp_id": [101, 102, 103, 104, 105],
    "name": ["Amit", "Ravi", "John", "Sara", "Neha"],
    "dept_id": [1, 2, 1, 3, 2],
    "salary": [70000, 50000, 80000, 90000, 60000]
})


departments = pd.DataFrame({
    "dept_id": [1, 2, 3, 4],
    "dept_name": ["IT", "HR", "Finance", "Marketing"]
})

bonus = pd.DataFrame({
    "emp_id": [101, 103, 104, 106],  
    "bonus": [5000, 7000, 6000, 4000]
})

# Outer Merge
# LEFT ∪ RIGHT (Union of both tables)
# -----------------------------------------------------------------------
outer = pd.merge(employees, departments, on='dept_id', how='outer')
# print(outer)

#    emp_id  name  dept_id   salary  dept_name
# 0   101.0  Amit        1  70000.0         IT
# 1   103.0  John        1  80000.0         IT
# 2   102.0  Ravi        2  50000.0         HR
# 3   105.0  Neha        2  60000.0         HR
# 4   104.0  Sara        3  90000.0    Finance
# 5     NaN   NaN        4      NaN  Marketing

outerNone = pd.merge(employees, departments, how='outer')
# print(outerNone)
# if no key column is specified then it will merge on all the common columns which are dept_id in this case

#    emp_id  name  dept_id   salary  dept_name
# 0   101.0  Amit        1  70000.0         IT
# 1   103.0  John        1  80000.0         IT
# 2   102.0  Ravi        2  50000.0         HR
# 3   105.0  Neha        2  60000.0         HR
# 4   104.0  Sara        3  90000.0    Finance
# 5     NaN   NaN        4      NaN  Marketing


import pandas as pd

employees = pd.DataFrame({
    "emp_id": [101, 102, 103],
    "name": ["Amit", "Ravi", "John"]
}).set_index("emp_id")

bonus = pd.DataFrame({
    "emp_id": [102, 103, 104],
    "bonus": [5000, 7000, 6000]
}).set_index("emp_id")

# Joining
# -----------------------------------------------------------------------
left = employees.join(bonus)
# print(left)

#         name   bonus
# emp_id
# 101     Amit     NaN
# 102     Ravi  5000.0
# 103     John  7000.0

right = bonus.join(employees)
# print(right)

#         bonus  name
# emp_id
# 102      5000  Ravi
# 103      7000  John
# 104      6000   NaN