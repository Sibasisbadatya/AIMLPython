import pandas as pd

dic = {
    "name":["Sibasis","Ansuman","Bhaskar"],
    "mark":[12,17,11],
    "rank":[2,1,3]
}

carr = pd.DataFrame(dic)
print(carr)
# carr.to_csv("nmr.csv") # creates csv file with name with index
# carr.to_csv("nmr.csv",index=False)# without index

# carr.to_csv("nmr.csv",header=False) without header
# carr.to_csv("nmr.csv",header=['a','b','c']) with customised header



# Reading Pandas
# ---------------------
readcsv = pd.read_csv("Pandas/people.csv")
print(readcsv)

# getting limited rows
readcsv = pd.read_csv("Pandas/people.csv",nrows=5)
print(readcsv)

# use of head(from front) and tail(from end) both takes by default 5 rows ro show
print(readcsv.head(10))
print(readcsv.tail(15))
# But in nrows all datas are not stored in memory only given rows are stored but in head and tail all file are stored but it shows only mentioned rows


# Use nrows when:
# CSV is very large
# you want to load only a small part

# Use .head() when:
# DataFrame already loaded
# you want to inspect first rows

# limited columns 

readcsv = pd.read_csv("Pandas/people.csv",usecols=["Email"],nrows=50) #using collumn name
print(readcsv)

readcsv = pd.read_csv("Pandas/people.csv",usecols=[1,2,3],nrows=50) #using column index
print(readcsv)

# skipping rows
readcsv = pd.read_csv("Pandas/people.csv",usecols=["Email"],skiprows=[1,2,3,4,5]) #using collumn name
print(readcsv)

# To make custom index 

readcsv = pd.read_csv("Pandas/people.csv",index_col="Email") 
print(readcsv)

# To make some row a sheader
readcsv = pd.read_csv("Pandas/people.csv",header=2) #by giving the index
print(readcsv)

# to give name
readcsv = pd.read_csv("Pandas/people.csv",names=['col']) #The number of names must match the number of columns in the CSV. If names are fewer or more
# Pandas will combine them into one column: and should be unique
print(readcsv)

# if some csv have no heading then here by default 1st row becomes heading
# to overcome we can do haeder = None 
readcsv = pd.read_csv("Pandas/people.csv",header=None) 
print(readcsv)

# to change the data type
readcsv = pd.read_csv("Pandas/people.csv",dtype={"Index":"float"}) # here we should give column name and the updated data type
print(readcsv)