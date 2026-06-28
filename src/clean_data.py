# module 2
import pandas as pd

df=pd.read_csv("data/student_dataset_v2.csv")


# old code is not important
print("missing values:")
print(df.isnull().sum())

print("duplicate records:")
print(df.duplicated().sum())

print("descriptive statistics:")
print(df.describe())

print("memory usage:")
print(df.memory_usage())

print("summary:")
print(df.info())

# module 3

print(df.drop_duplicates())

print(df.dropna())

print(df.isnull().sum().sum())

print(df[(df["Attendance"]>=0) & (df["Attendance"]<=100)])

print(df[(df["StudyHours"]<=0) & (df["StudyHours"]<=24)])

print(df[(df["Marks"]<=0) & (df["Marks"]<=100)])

print("Clean dataset:",df.shape)

df.to_csv("cleaned_dataset.csv",index=False)
