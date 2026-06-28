# module 1

import pandas as pd

df=pd.read_csv("data/student_dataset_v2.csv")

print("first 5 records:")
print(df.head(5))

print("last 5 records:")
print(df.tail(5))

print("shape of the dataset:")
print(df.shape)

print("columns name:")
print(df.columns)

print("datatypes:")
print(df.dtypes)