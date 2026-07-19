# Pandas

import pandas as pd

# pandas is made up top of numpy
# Whenever data is in 2D or in tabular structure, we can use pandas
# It is used for data manipulation and analysis
# It is used for data cleaning and data preprocessing
# It is used for data visualization

# Pandas support heterogeneous data unlike numpy which support homogeneous data

# provide easy syntax for filtering, grouping, merging, reshaping, and pivoting data

# In Numpy we use the data structure called ndArray.
# In Pandas we use the data structure called DataFrame and Series


# Series is a one-dimensional array-like object that can hold any data type
# ----------------------------------------------------------------------------
# A Series is a one-dimensional labeled array that can hold any data type
# (integers, strings, floating-point numbers, etc.). It is similar to a column in a spreadsheet 
# or a database table. 
# Each element in a Series has an associated index, 
# which can be used to access and manipulate the data.

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

# Label for them are called indexes.

# DataFrame
# ----------------------------------------------------------------------------
# 2D table with rows and columns
# it is labelled ,flexible with data types(numbers,text and dates etc)
# Mutable


# Data cleaning -> handling missing values (fillna,dropna)

# Data Selection and filtering -> use labels(loc) and position(iloc)
# in ML we have to deal with so many datas so it better to select useful data and 
# filter out the unwanted data

# Aggregation and Grouping -> groupby,sum,mean

# Merging and Joining -> merge,join,concat
# beacuse we deal with multiple files and datser so we merge and join to combine them.

#Reshaping and Pivoting -> pivot,pivot_table,melt

# I/O Operations -> read_csv, to_csv, read_excel, to_excel(CSV,excel,json)


url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'

columns = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'class']

df = pd.read_csv(url,header=None, names=columns,index_col=False)
# we dont have header then we can provide custom header name (columns)

# print(df.head())

# .head() is used to display the first few rows of the DataFrame. By default, it shows the first 5 rows, 
# but you can specify the number of rows to display by passing an argument to the head() method.
# For example, df.head(10) will display the first 10 rows of the DataFrame.

# print(df.info())

# print(df.dtypes())
# it shows the data types of each column in the DataFrame.
# It is useful for understanding the structure of the data and for identifying any potential issues with data types that may 
# need to be addressed during data cleaning or analysis.

# PANDAS vs NUMPY
# ----------------------------------------------------------------------------
# if dimension of data>2 use numpy
# if dimesnion is 2D and numerical and have to perfome mathematical operation use numpy
# for hetero genous 2D data use pandas


# Practical Rule in ML
# ----------------------------------------------------------------------------
# Start with pandas for data cleaning and data preprocessing then convert to numerical data by encoding techniques
# and then convert to numpy array for mathematical operations and model training.



# Will Pandas work when data is larger than memory?
# Pandas is designed to work with data that can fit into memory. 
# If the dataset is larger than the available memory, it may lead to performance issues or even crashes. 
# However, there are some techniques and libraries that can help you work with larger datasets in pandas,
# such as using Dask or Polars,pySpark etc, which provide out-of-core computation capabilities.
# Additionally, you can also consider using databases or distributed computing frameworks like Apache Spark for handling large datasets.

# Dask- A library thet extends pandas to work with larger-than-memory datasets by parallelizing operations across multiple cores
# or distributed chunk processing.

# Polars:Written in Rust with lazy execution and streaming.
# PySpark: A Python API for Apache Spark, which is a distributed computing framework that can handle large datasets across 
# clusters of computers.
# same works as chunk processing (parallel and sequential).


# Creation of DataFrame
# ----------------------------------------------------------------------------
# from dictionary
data = {
        'Name': ['Alice', 'Bob', 'Charlie'],
        'Age': [25, 30, 35],
        'City': ['New York', 'Los Angeles', 'Chicago']
        }

df = pd.DataFrame(data)
# print(df)
print(type(df['Name'])) #<class 'pandas.Series'>
print(type(df['Name'].values)) #<class 'numpy.ndarray'> like numpy array but it is not numpy array
# it is pandas Series values which is of type numpy array

# So Series are internally stored as numpy arrays, but they are not the same as numpy arrays.


# DataFrames Arguments
pd.DataFrame(
    data=None, #actual content of dataframe
    index=None, #Row labels (default is 0,1,2,...)
    columns=None, #Column labels (default is inferred from data)
    dtype=None, #Data type to force, otherwise inferred from data
    copy=False #Default is False. If True, it copies the data.(memory inefficient)
    # If False, it tries to avoid copying when possible.
    )

# creates a dataframe instance

# Creation with list of  dictionaries
data = [
    {'Name': 'Alice', 'Age': 25, 'City': 'New York'},
    {'Name': 'Bob', 'Age': 30, 'City': 'Los Angeles'},
    {'Name': 'Charlie', 'Age': 35, 'City': 'Chicago'}
]
# Here each value of dictonary's key is of type pd.Series


df = pd.DataFrame(data)
# print(df) 


# Creation with list of lists
data = [
    ['Alice', 25, 'New York'],
    ['Bob', 30, 'Los Angeles'],
    ['Charlie', 35, 'Chicago']
]
# Here each list is of type pd.Series

lof = pd.DataFrame(data,columns=['Name','Age','City'])
# print(lof)


# From Numpy Array
import numpy as np
data = np.array([['Alice', 25, 'New York'],
                 ['Bob', 30, 'Los Angeles'],
                 ['Charlie', 35, 'Chicago']])
# Here each list is of type pd.Series
df = pd.DataFrame(data, columns=['Name', 'Age', 'City'])
# print(df)

# From Pandas Series
data = {
    'Name': pd.Series(['Alice', 'Bob', 'Charlie']),
    'Age': pd.Series([25, 30, 35]),
    'City': pd.Series(['New York', 'Los Angeles', 'Chicago'])
}

df = pd.DataFrame(data)
# print(df)