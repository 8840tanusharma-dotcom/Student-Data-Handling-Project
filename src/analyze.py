# module 5

import pandas as pd
df=pd.read_csv("output/Transformed_dataset.csv")

print("Toppers:")
topper= df[df["Marks"]>=90]
print(topper)
topper.to_csv("Topper.csv",index=False)

print("Failure:")
failure= df[df["result"] == "Fail"]
print(failure)
failure.to_csv("Fail.csv",index=False)

print("Attendance below 75:")
low_attendance= df[df["Attendance"] <75]
print(low_attendance)
low_attendance.to_csv("Low_attendance.csv",index=False)

print("Studyhr more than 8:")
low_studyhr = df[df["StudyHours"]>8]
print(low_studyhr)
low_studyhr.to_csv("Low_studyhr.csv",index=False)

# module 6

print("Average marks:")
print(df["Marks"].mean())

print("HIghest marks:")
print(df["Marks"].max())

print("Lowest marks:")
print(df["Marks"].min())

print("Average attendance:")
print(df["Attendance"].mean())

print("Average studyhr:")
print(df["StudyHours"].mean())

total= len(df)
total_pass = len(df[df["result"] == "Pass" ])
pass_percentage = (total_pass/total)*100
print("Pass Percentage:",round(pass_percentage,2), "%")

total= len(df)
total_fail = len(df[df["result"] == "Fail" ])
fail_percentage = (total_fail/total)*100
print("Fail Percentage:",round(fail_percentage,2), "%")

print("Grade distribution:")
print(df["grade"].value_counts())

# module 7
print("sorted by marks:")
marks_sorted= df.sort_values(by="Marks",ascending=False)
print(marks_sorted)

print("sorted by attendance:")
attendance_sorted = df.sort_values(by="Attendance",ascending=False)
print(attendance_sorted)

print("sorted by studyhr:")
studyhr_sorted= df.sort_values(by="StudyHours",ascending=False)
print(studyhr_sorted)

# module 8

print("marks by grade:")
marks=df.groupby("grade")["Marks"].mean()
print(marks)

print("no. of students for each grade:")
student= df.groupby("grade").size()
print(student)

print("attendance by grade:")
attendance= df.groupby("grade")["Attendance"].mean()
print(attendance)

# module 9

print("Mean:")
print(df[["Marks","Attendance","StudyHours"]].mean())

print("Median:")
print(df[["Marks","Attendance","StudyHours"]].median())

print("Mode:")
print(df[["Marks","Attendance","StudyHours"]].mode())

print("Standard Deviation:")
print(df[["Marks","Attendance","StudyHours"]].std())

print("Variance:")
print(df[["Marks","Attendance","StudyHours"]].var())

print("Correlation Matrix:")
print(df[["Marks","Attendance","StudyHours"]].corr())





