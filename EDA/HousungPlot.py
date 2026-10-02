import numpy as np
import pandas as pd

import matplotlib.pyplot as plt
import seaborn as sns


df = pd.read_csv('Housing.csv')

df.head(5).style.background_gradient(cmap='Blues')

# print(df)

# print(df.shape)

# Checking null values across columns
# print(df.isnull().sum())

# Description of the dataset
# only describes about the numerical columns, not the categorical ones
# print(df.describe())
print(df.describe().T)