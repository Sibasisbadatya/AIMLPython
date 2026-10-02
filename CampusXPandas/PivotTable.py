import pandas as pd
data = {
    "Region": ["North", "North", "South", "South"],
    "Year": [2024, 2025, 2024, 2025],
    "Product": ["Product_A", "Product_B", "Product_A", "Product_B"],
    "Sales": [232, 192, 412, 156]
}

df = pd.DataFrame(data)
# print(df)
#   Region  Year    Product  Sales
# 0  North  2024  Product_A    232
# 1  North  2025  Product_B    192
# 2  South  2024  Product_A    412
# 3  South  2025  Product_B    156

# Pivot Table
# -----------------------------------------------------------------------------
# total sales per region per product

pivot = pd.pivot_table(
    df,
    values='Sales', # on which column we want to perform the aggregation
    index='Region', # represents the rows of the pivot table
    columns='Product', # represents the columns of the pivot table
    aggfunc='sum',
    fill_value=0 # to fill the missing values with 0 instead of NaN
)

# print(pivot)

# Product  Product_A  Product_B
# Region
# North          232        192
# South          412        156

