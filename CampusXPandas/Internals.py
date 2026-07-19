# Uses Numpy Arrays for speed

# Columnar Storage
# --------------------------------------------------------------------------------------------------
# DataFrames are stored in column wise nor row wise
# Benifits of columnar storage:


# 1. Faster data access: When you access a column, pandas can quickly retrieve the
#    data for that column without having to read through the entire dataset. 
#    because here in dataframe each row is a Series which is a column according to tabular structure.


# 2. Memory Efficiency: Columnar storage can be more memory efficient, especially when
#    you have many columns with missing values. It can store only the non-missing values
#    for each column, which can save memory.

# | Name | Age | Salary |
# | ---- | --- | ------ |
# | A    | 25  | NaN    |
# | B    | 30  | NaN    |
# | C    | 35  | 70000  |

# 🔴 Row storage:
# [A,25,null], [B,30,null], [C,35,70000]
# 👉 Stores null again and again ❌


# 🟢 Column storage:
#     Salary → [null, null, 70000]
# 👉 Can compress nulls easily ✅
# 👉 Saves memory




# 3. Better Compression: Columnar storage can often be compressed more effectively than
#    row-wise storage, which can further reduce memory usage and improve performance.

# Example
# Salary → [50000, 50000, 50000, 50000]

# 👉 Can store as:

# 50000 × 4

# Row storage:
# [A,25,50000], [B,30,50000], ...
# 👉 Hard to compress ❌


# Column storage:
    # Salary → repeated values
# 👉 Can compress easily ✅
    
# 4. Optimized for Analytical Queries: Columnar storage is particularly well-suited for
#    analytical queries that involve aggregations and filtering on specific columns, as it can quickly access the relevant data.

# 4. Optimized for Analytical Queries

# 👉 Best for SUM, AVG, COUNT, filtering
# example SELECT AVG(Salary) FROM table;
# Row storage:
# Reads Name, Age, Salary ❌
# 🟢 Column storage:
# Reads only Salary ✅


# 5. Improved Performance with Large Datasets: For large datasets, columnar storage can
#    significantly improve performance, as it allows for more efficient data retrieval and processing.


# Array Manager
# -----------------------------------------------------------------------------------
# Groups of columns are stored together in contiguous blocks of memory, 
# which allows for efficient access and manipulation of data.
# This is particularly beneficial for operations that involve multiple columns,
# as it minimizes the need for data copying and allows for faster computations.

# Due to which different columns which are of different datatypes can be stored together in the same dataframe
# without any performance issues.


# Label Aware Indexing
# -----------------------------------------------------------------------------------
# Pandas provides label-aware indexing, which allows you to access data using labels 
# (column names and row indices) rather than just integer-based indexing.
# This makes it easier to work with data, as you can refer to columns and rows by their names rather than
# having to remember their positions in the dataset.

# C Accelaration
# -----------------------------------------------------------------------------------
# Pandas is built on top of C and Cython, which allows for efficient execution of operations.
# Many of the core operations in pandas are implemented in C, which can provide significant performance benefits
# compared to pure Python implementations.