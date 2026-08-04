"""
Introduction to Python for Data Analytics - issue #22
Loads and prints a dataset using pandas.
"""

import pandas as pd

# Load the dataset into a DataFrame
df = pd.read_csv("sample_dataset.csv")

# Print the full dataset
print("=== Full dataset ===")
print(df)

# Print basic info about it
print("\n=== Dataset info ===")
print(df.info())

# Print a quick summary of the numeric columns
print("\n=== Summary statistics ===")
print(df.describe())
