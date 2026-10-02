import pandas as pd

# Cross Tabulation
# -----------------------------------------------------------------------------
# Cross tabulation is a method used to analyze the relationship between two or more categorical variables by creating a contingency table.
# It helps to summarize and understand the distribution of data across different categories.


data = {
    "Gender": ["Male", "Male", "Female", "Female", "Male", "Female", "Male", "Female"],
    "Preference": ["Tea", "Coffee", "Coffee", "Tea", "Tea", "Coffee", "Coffee", "Tea"]
}

df = pd.DataFrame(data)
print(df)

#   Gender Preference
# 0   Male        Tea
# 1   Male      Coffee
# 2 Female      Coffee
# 3 Female        Tea
# 4   Male        Tea
# 5 Female      Coffee
# 6   Male      Coffee
# 7 Female        Tea

# Creating Cross tab Using pivot_table
# -----------------------------------------------------------------------------

ctab = pd.pivot_table(
    df,
    index="Gender",
    columns="Preference",
    aggfunc='size',
    fill_value=0 # to fill the missing values with 0 instead of NaN
)

# print(ctab)

# Preference  Coffee  Tea
# Gender
# Female           2    2
# Male             2    2


# By using crosstab function
# -----------------------------------------------------------------------------
ctab = pd.crosstab(df['Gender'], df['Preference'])
# print(ctab)

# Preference  Coffee  Tea
# Gender
# Female           2    2
# Male             2    2