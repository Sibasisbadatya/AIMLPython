import pandas as pd

readcsv = pd.read_csv("Pandas/people.csv")
# print(readcsv)
# get indexes
print(readcsv.index)
print(readcsv.index.array) #as an array

# get columns
print(readcsv.columns)

# to get priority results (values)
print(readcsv.describe()) # it works only for numerical values Her eonly index is in numerical so it will give results for Index column data


# use indexing

print(readcsv[:10])

# make dataframe to numoy
ncsv = readcsv.to_numpy()
print(ncsv)

# sorting according to index
dscndingcsv = readcsv.sort_index(axis=0,ascending=False) #along the axis
print(dscndingcsv)

# sorting according to values
dscndingcsv = readcsv.sort_values(by="First Name", ascending=False)
print(dscndingcsv)

dscndingcsv = readcsv.sort_values(by=["First Name","Email"], ascending=False)
print(dscndingcsv)

# Here by may be array and priority order will be the order in the list


# Changing the data

readcsv.loc[0,"First Name"]="Sibasis" # here the 1st parameter also can be a list to update in multiple row
print(readcsv)


readValue = readcsv.loc[0,"First Name"]
print(readValue)

readValue = readcsv.loc[[1,2,3],["First Name","Email"]]
print(readValue)
readValue = readcsv.loc[:,["First Name","Email"]] # for all rows
print(readValue)

readValue = readcsv.loc[[1,2],:] # for all columns
print(readValue)


# Dropping a row
readcsv.drop(1) # by default axis is 0
print(readcsv)
readcsv.drop([0,2])

# Dropping a column
readcsv.drop("First Name", axis=1)
print(readcsv)

deleted = readcsv.drop(["First Name","Email"], axis=1)
print(deleted)

