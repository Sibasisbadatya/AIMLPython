import pandas as pd

readcsv = pd.read_csv("Pandas/people.csv")
print(readcsv)

# Replacing values
a = readcsv.replace("Lori","Louda") # 1st parameter is old value and 2nd parameter is new value
b = readcsv.replace(["Lori","Yesina"],"Louda") # if we want to replace multiple values with same value
print(b)

c = readcsv.replace({
    "Email": {"elijah57@example.net": "siba"},
    "Name": {"Louda": "Bhaskar"}
})  # for different values in different columns we can use dictionary of dictionary
print(c)

readcsv.replace(r"\s+", "_", regex=True) # for regex replacement here we are replacing all white spaces with underscore

readcsv.replace(1,method="ffill") # for forward fill replacement for 1
readcsv.replace(1,method="bfill") # for backward fill replacement for 1

readcsv.replace(1,method="ffill",limit=2) # with limit  replace only first N(given limit) occurrences
readcsv.replace(1,method="bfill",limit=2,axis=1) 

