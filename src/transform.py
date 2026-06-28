# module 4

import pandas as pd
df=pd.read_csv("output/cleaned_dataset.csv")

def calculate_grade(marks):
    if marks >= 90:
        return "A"
    elif marks >= 75:
        return "B"
    elif marks >= 60:
        return "C"
    elif marks >= 40:
        return "D"
    else:
        return "F"
    
df["grade"] = df["Marks"].apply(calculate_grade)   
print(df["grade"])

df["result"]= df["Marks"].apply(lambda x:"Pass" if x>=40 else "Fail")
print(df["result"])

df["performance"] = (df["Marks"]*0.6 + df["Attendance"]*0.2 + df["StudyHours"]*2)
print(df["performance"])

print(df.head(5))

df.to_csv("Transformed_dataset.csv",index=False)

