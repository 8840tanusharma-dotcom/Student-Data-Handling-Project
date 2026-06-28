# module 10

import pandas as pd
df=pd.read_csv("output/Transformed_dataset.csv")

total_stu= len(df)
pass_stu=len(df[df["result"] == "Pass"])
fail_stu= len(df[df["result"] == "Fail"])
high_marks= df["Marks"].max()
Low_marks= df["Marks"].min()
average_marks= df["Marks"].mean()
average_attendance= df["Attendance"].mean()
grade= df["grade"].value_counts()

report={
    "Matric":[
        "Total students",
        "No.of Passed students",
        "No.of Failed students",
        "Highest marks",
        "Lowest marks",
        "Average marks",
        "Average attendance",
        "Grade-wise distribution"
    ],
    "Values":[
        total_stu,
        pass_stu,
        fail_stu,
        high_marks,
        Low_marks,
        average_marks,
        average_attendance,
        grade
        
    ]
}
report_df=pd.DataFrame(report)
print(report_df)

report_df.to_csv("Report.csv",index=False)

