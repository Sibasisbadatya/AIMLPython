import pandas as pd

readcsv = pd.read_csv("Pandas/people.csv")
print(readcsv)

# Dropping the missed value

dropped = readcsv.dropna()  # drop the row where value is missed becoz by default axis is 0
print(dropped)  

dropped = readcsv.dropna(axis=1)  # drop the column where value is missed.
print(dropped)  

dropped = readcsv.dropna(axis=0,how="any") #does the same as .dropna()
print(dropped)

dropped = readcsv.dropna(axis=0,how="all") #does deleet the row if all are absent or NaN

readcsv.dropna(subset=["Email"]) # means delete the row for the NaN present in only Email (or the columns present in subset array)

readcsv.dropna(inplace=True) #Modifies original DataFrame AND FOR   inplace = false it returns modifies dataFrame

threshDt = readcsv.dropna(thresh=2) #Keep rows with at least 2 non-NaN(not blank) values

cd = readcsv.fillna("@123@") #replace emoty or NaN to given value 
# if inplace = True  readcsv.fillna("@123@",inplace=True) it doesn't return anyhting to a variable and modify the original data
# It only changes the DataFrame in memory  ,Your original file on disk remains unchanged
readcsv.fillna("@123@",inplace=True)


customFIll = readcsv.fillna({
    'Email': "Sibasis",
    'Phone': "12345"
})  #Different values for different columns

# Forward fill (propagate previous row value)
d = readcsv.ffill()

# Backward fill
d=readcsv.bfill()

# Forward fill (propagate previous column value) with axis 1
d=readcsv.ffill(axis=1)

# Backward fill wirh axis 1
d=readcsv.bfill(axis=1)
d = readcsv.ffill(limit=2) #with limit  Fill only first N(given limit) NaNs
d = readcsv.ffill("12sibasis12",limit=2)
# so here axis by default is 0 so which row has minimum 2 NaN then first 2 NaN will filled y 12sibasis12
