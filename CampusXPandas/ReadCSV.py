import pandas as pd

csv = pd.read_csv('healthexp.csv')
# print(csv.head())
# Reading .tsv files(same as csv but instead of comma we have tab)
tsv = pd.read_csv('mtcars.tsv', sep='\t')
# print(tsv.head())

# Reading .xlsx files
xlsx = pd.read_excel('file_example_XLSX_10.xlsx') #need to install openpyxl library to read excel files
# print(xlsx.head())

# Reading json files
df = pd.read_json("https://jsonplaceholder.typicode.com/users")

# print(df.head())

# Read HTML
url = "https://www.worldometers.info/world-population/population-by-country/"

# pd.read_html(url)
# but it most of the time doesnot works

# Pandas internally uses urllib to ectract the data from the webpage, and it does not include a user-agent header by default.
# 👉 But many websites block:

# bots 🤖
# scripts without headers

tables = pd.read_html(url, storage_options={
    "User-Agent": "Mozilla/5.0"
}) #extract all the tables from the webpage (by finding table tag) and return a list of DataFrames
print(tables[0].head()) #need to be installed lxml library to read html tables