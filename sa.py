import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

print("AI Student Performance Analyzer")
print("\n")
print("---------------------------------------")
n=int(input("Enter total no: of student details to enter:"))
print("\n")
print("---------------------------------------")
name=[]
attendance=[]
marks=[]
study_hours=[]
for i in range(n):
    na=input("Enter student name:")
    m=int(input("Enter total marks:"))
    at=float(input("Enter total attendance out of 100 (in %):"))
    sh=int(input("Enter total study hours:"))
    print("\n")
    print("---------------------------------------")
    name.append(na)
    attendance.append(at)
    marks.append(m)
    study_hours.append(sh)
    
data={
    "name":name,
    "marks":marks,
    "attendance":attendance,
    "study_hours":study_hours
}

df=pd.DataFrame(data)
df.to_csv("students.csv",index=False)
df1=pd.read_csv("students.csv")
#average mark
avg_mark=np.mean(df1["marks"])
print(f'Average mark:{avg_mark}')
print("\n")
print(f'Highest mark:{df1["marks"].max()}')
print("\n")
print(f'Lowest mark:{df1["marks"].min()}')
highest_mark=df1["marks"].max()
topper=df1[df1["marks"]==highest_mark]
print(topper)
for i in range(len(df1)):
    if df1["marks"][i]>=50:
        print(df1["name"][i],"is pass")
    else:
        print(df1["name"][i],"is fail")
for i in range(len(df1)):
    if df1["attendance"][i]>=75:
        print(df1["name"][i],"is eligible to write exam")
    else:
        print(df1["name"][i],"is not eligible to write exam")
    
print("Variance:",np.var(df1["marks"]))
print("Standard deviation:",np.std(df1["marks"]))

#bar graph
x=df1["name"]
y=df1["marks"]

plt.bar(x,y)
plt.title("Student names vs marks.")
plt.xlabel("Student name")
plt.ylabel("Marks")
plt.show()

# piechart
pass_count = 0
fail_count = 0
for mark in df1["marks"]:
    
    if mark >= 50:
        pass_count += 1
    else:
        fail_count += 1
sizes = [pass_count, fail_count]

labels = ["Pass","Fail"]

plt.pie(sizes, labels=labels, autopct="%1.1f%%")

plt.title("Pass vs Fail")

plt.show()

#scatter plot
x1=df1["study_hours"]
y1=df1["marks"]

plt.scatter(x1,y1,label="Students")
plt.title("Study hours vs marks.")
plt.xlabel("study hours")
plt.ylabel("Marks")
plt.legend()
plt.show()


#histogram
a=df1["marks"]
plt.hist(a)
plt.title("Marks Distribution")
plt.xlabel("Marks")
plt.ylabel("Frequency")
plt.show()
#box plot
plt.boxplot(a)
plt.title("Marks Spread")
plt.show()
print(df1.sort_values("marks",ascending=False))
