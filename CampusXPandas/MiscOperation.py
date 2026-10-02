
import pandas as pd

def testFunc(x):
    model_name = "_".join(x.split())
    return model_name.lower()

data = {
    "model_name": [
        "Logistic Regression",
        "Decision Tree",
        "Random Forest",
        "XGBoost",
        "LightGBM",
        "KNN",
        "Naive Bayes",
        "SVM",
        "CNN",
        "LSTM"
    ],
    "execution_time": [0.5, 0.8, 2.3, 3.1, 2.8, 1.2, 0.6, 1.9, 4.5, 5.0],
    "model_size": [2.3, 5.6, 45.2, 60.1, 55.8, 8.4, 1.2, 12.3, 120.5, 150.7],
    "accuracy": [0.82, 0.78, 0.89, 0.91, 0.90, 0.76, 0.74, 0.88, 0.93, 0.92],
    "f1_score": [0.80, 0.75, 0.87, 0.90, 0.89, 0.74, 0.72, 0.86, 0.92, 0.91],
    "precision": [0.81, 0.76, 0.88, 0.91, 0.90, 0.75, 0.73, 0.87, 0.93, 0.92],
    "recall": [0.79, 0.74, 0.86, 0.89, 0.88, 0.73, 0.71, 0.85, 0.91, 0.90]
}

df = pd.DataFrame(data)
# print(df)


# Apply
# ------------------------------
# apply function does apply a function along the axis of the DataFrame (either rows or columns) 
# and returns a new DataFrame with the results.
changedCol = df['model_name'].apply(testFunc)
# print(changedCol)

# 0    logistic_regression
# 1          decision_tree
# 2          random_forest
# 3                xgboost
# 4               lightgbm
# 5                    knn
# 6            naive_bayes
# 7                    svm
# 8                    cnn
# 9                   lstm

# Same we can do by map() also
mappedCol = df['model_name'].map(testFunc)
# print(mappedCol)
# 0    logistic_regression
# 1          decision_tree
# 2          random_forest
# 3                xgboost
# 4               lightgbm
# 5                    knn
# 6            naive_bayes
# 7                    svm
# 8                    cnn
# 9                   lstm
# Name: model_name, dtype: str

# Map Vs Apply
# ------------------------------
# Map works only for series and it is for element wise but apply works for both
# series and dataframe and it is for row wise or column wise.


# using lambda function
# ------------------------------

lambdaCol = df['model_name'].apply(lambda x: "_".join(x.split()).lower())
# print(lambdaCol)

# 0    logistic_regression
# 1          decision_tree
# 2          random_forest
# 3                xgboost
# 4               lightgbm
# 5                    knn
# 6            naive_bayes
# 7                    svm
# 8                    cnn
# 9                   lstm
# Name: model_name, dtype: str


# Sort values by parameter
sorted = df.sort_values(by='accuracy', ascending=False)
#by default is is ascending
# print(sorted)

#             model_name  execution_time  model_size  accuracy  f1_score  precision  recall
# 8                  CNN             4.5       120.5      0.93      0.92       0.93    0.91
# 9                 LSTM             5.0       150.7      0.92      0.91       0.92    0.90
# 3              XGBoost             3.1        60.1      0.91      0.90       0.91    0.89
# 4             LightGBM             2.8        55.8      0.90      0.89       0.90    0.88
# 2        Random Forest             2.3        45.2      0.89      0.87       0.88    0.86
# 7                  SVM             1.9        12.3      0.88      0.86       0.87    0.85
# 0  Logistic Regression             0.5         2.3      0.82      0.80       0.81    0.79
# 1        Decision Tree             0.8         5.6      0.78      0.75       0.76    0.74
# 5                  KNN             1.2         8.4      0.76      0.74       0.75    0.73
# 6          Naive Bayes             0.6         1.2      0.74      0.72       0.73    0.71




# Date And Time
# -------------------------------

# TimeStamp
# Creates Date Time Format from a string

# 1.pd.Timestamp() can parse a wide variety of date formats, including:
time = pd.Timestamp('2024-06-01')
# print(time)
#2024-06-01 00:00:00
dateTime = pd.Timestamp('2024-06-01 12:30:45')
# print(dateTime)
#2024-06-01 12:30:45

customTime = pd.Timestamp(year=2024, month=6, day=1, hour=12, minute=30, second=45)
# print(customTime)
# 2024-06-01 12:30:45

# pd.to_datetime() is a more flexible function that can convert various types of input into a Timestamp.
# It can handle strings, lists, arrays, and even entire DataFrames or Series.
# output --> for scaler input it will give Timestamp, DateTimeIndex for list or array input .
# Series of datetime64 dtype (if series input)


timestamp1 = pd.to_datetime('2024-06-01')
# print(timestamp1)
# 2024-06-01 00:00:00

timestamp2 = pd.to_datetime(['2024-06-01', '2024-07-01', '2024-08-01'])
# print(timestamp2)
# DatetimeIndex(['2024-06-01', '2024-07-01', '2024-08-01'], dtype='datetime64[ns]', freq=None)

# print(type(timestamp2))
# <class 'pandas.core.indexes.datetimes.DatetimeIndex'>

# print(type(timestamp2[0]))
# <class 'pandas._libs.tslibs.timestamps.Timestamp'>
# internally it uses numpy datetime64 dtype to store the datetime values,
# but it provides additional functionality and methods specific to pandas.


timestamp3 = pd.to_datetime(pd.Series(['2024-06-01', '2024-07-01', '2024-08-01']))
# print(timestamp3)

# 0   2024-06-01
# 1   2024-07-01
# 2   2024-08-01
# dtype: datetime64[us]


# from epoch values
# --------------------------------
# Epoch time is the number of seconds that have elapsed since January 1, 1970 (UTC).
epoch_time = 1700000000
timestamp_from_epoch = pd.to_datetime(epoch_time,unit='s')
# print(timestamp_from_epoch)


# TimeDelta
# --------------------------------
# TimeDelta represents a duration, the difference between two dates or times.
# It can be created using pd.Timedelta() function, which takes various parameters to specify the duration.
# For example, to create a TimeDelta of 5 days:
time_delta = pd.Timedelta(days=5)
# print(time_delta)
# 5 days and 9 hrs
time_delta = pd.Timedelta(days=5, hours=9)
# print(time_delta)
# 5 days 09:00:00

start = pd.Timestamp(year=2026, month=1, day=1, hour=10)
end = pd.Timestamp(year=2026, month=1, day=10)

fiveDay9hr = start + pd.Timedelta(days=5, hours=9)
# print(fiveDay9hr)
# 2026-01-06 19:00:00


# DataFrame with DateTime columns

data = {
    "date": ["2025-06-21", "2025-06-22", "2025-06-23"],
    "value": [10, 20, 30]
}

df = pd.DataFrame(data)

# print(df)
#          date  value
# 0  2025-06-21     10
# 1  2025-06-22     20
# 2  2025-06-23     30

df['date'] = pd.to_datetime(df['date'])
# print(df)

# so datetime64[ns] is the dtype of the date column after conversion.but TImeStamp is of each element.
# Numpy provide this datatype datetime64 to represent date and time.

# Pandas Date Time = Numpy datetime64 + pandas Timestamp+extra time related functionality and methods. 








# Date Range
# --------------------------------
ts1 = pd.Timestamp('2024-06-01')
ts2 = pd.Timestamp('2024-06-10')
date_range = pd.date_range(start=ts1, end=ts2, freq='D')
# print(date_range)

# DatetimeIndex(['2024-06-01', '2024-06-02', '2024-06-03', '2024-06-04',
#                '2024-06-05', '2024-06-06', '2024-06-07', '2024-06-08',
#                '2024-06-09', '2024-06-10'],
#               dtype='datetime64[us]', freq='D')

# | freq         | Meaning                 |
# | ------------ | ----------------------- |
# | `D`          | Daily                   |
# | `H`          | Hourly                  |
# | `T` or `min` | Minute                  |
# | `S`          | Second                  |
# | `M`          | Month end               |
# | `MS`         | Month start             |
# | `W`          | Weekly                  |
# | `B`          | Business days (Mon–Fri) |

s = pd.Series(pd.date_range('2025-01-01', periods=5, freq='D'))
# print(s)

# 0   2025-01-01
# 1   2025-01-02
# 2   2025-01-03
# 3   2025-01-04
# 4   2025-01-05
# dtype: datetime64[us]

td = pd.Series([pd.Timedelta(hours=i) for i in range(5)])
# print(td)

# 0   0 days 00:00:00
# 1   0 days 01:00:00
# 2   0 days 02:00:00
# 3   0 days 03:00:00
# 4   0 days 04:00:00
# dtype: timedelta64[us]


df = pd.DataFrame({
    'A':s,
    'B':td
})
# print(df)

#            A               B
# 0 2025-01-01 0 days 00:00:00
# 1 2025-01-02 0 days 01:00:00
# 2 2025-01-03 0 days 02:00:00
# 3 2025-01-04 0 days 03:00:00
# 4 2025-01-05 0 days 04:00:00

df['C'] = df['A'] + df['B']
# print(df)

#            A               B                   C
# 0 2025-01-01 0 days 00:00:00 2025-01-01 00:00:00
# 1 2025-01-02 0 days 01:00:00 2025-01-02 01:00:00
# 2 2025-01-03 0 days 02:00:00 2025-01-03 02:00:00
# 3 2025-01-04 0 days 03:00:00 2025-01-04 03:00:00
# 4 2025-01-05 0 days 04:00:00 2025-01-05 04:00:00

# Filter in DateTime
# --------------------------------

data = {
    "date": ["2025-06-21", "2025-06-22", "2025-06-23", "2025-06-24"],
    "value": [10, 20, 30, 40]
}

df = pd.DataFrame(data)
df["date"] = pd.to_datetime(df["date"])

# . Filter by exact date
exactDate = df[df["date"] == "2025-06-22"]

# print(exactDate)

#         date  value
# 1 2025-06-22     20

# Filter by date range (VERY IMPORTANT 🔥)
drange = df[(df["date"] >= "2025-06-22") & (df["date"] <= "2025-06-23")]
# print(drange)

#         date  value
# 1 2025-06-22     20
# 2 2025-06-23     30

# Filter using between()
btwn = df[df["date"].between("2025-06-22", "2025-06-23")]
# print(btwn)
#       date  value
# 1 2025-06-22     20
# 2 2025-06-23     30

# Filter by year / month / day

year = df[df['date'].dt.year == 2025]
# print(year)

#         date  value
# 0 2025-06-21     10
# 1 2025-06-22     20
# 2 2025-06-23     30
# 3 2025-06-24     40

month = df[df['date'].dt.month == 6]
# print(month)

#         date  value
# 0 2025-06-21     10
# 1 2025-06-22     20
# 2 2025-06-23     30
# 3 2025-06-24     40

day = df[df['date'].dt.day == 22]
# print(day)
#        date  value
# 1 2025-06-22     20

# Filter by time (hour/minute)

df = pd.DataFrame({
    "date": pd.date_range("2025-06-21 10:00", periods=4, freq="h"),
    "value": [10, 20, 30, 40]
})

time = df[df['date'].dt.hour >= 11]
# print(time)
#                  date  value
# 1 2025-06-21 11:00:00     20
# 2 2025-06-21 12:00:00     30
# 3 2025-06-21 13:00:00     40

# By Index
# -------------------------------
df.set_index("date", inplace=True)

loc = df.loc["2025-06-21":"2025-06-23"]
# print(loc)
#                      value
# date
# 2025-06-21 10:00:00     10
# 2025-06-21 11:00:00     20
# 2025-06-21 12:00:00     30
# 2025-06-21 13:00:00     40





# Benifit of dateTimeIndex

data = {
    "date": pd.date_range("2025-06-21", periods=4, freq="D"),
    "value": [10, 20, 30, 40]
}

df = pd.DataFrame(data)

df_index = df.drop("value", axis=1)
# print(df_index)
#         date
# 0 2025-06-21
# 1 2025-06-22
# 2 2025-06-23
# 3 2025-06-24

df_index.index = df_index['date']
print(df_index)
#                  date
# date
# 2025-06-21 2025-06-21
# 2025-06-22 2025-06-22
# 2025-06-23 2025-06-23
# 2025-06-24 2025-06-24
