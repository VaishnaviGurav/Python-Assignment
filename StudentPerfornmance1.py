import pandas as pd

import matplotlib.pyplot as plt

import seaborn as sns

from sklearn.model_selection import train_test_split

from sklearn.tree import DecisionTreeClassifier, plot_tree

Border = "-"*40
##########################################################################
# Step 1 : Load the dataset
##########################################################################
print(Border)
print("Step 1 : Load the dataset")
print(Border)

DatasetPath = "student_performance_ml.csv"

df = pd.read_csv(DatasetPath)

print("Dataset gets loaded successfully...")
print("Initial entries from dataset : ")
print(df.head())

print(df.tail())

print(df.shape)

print(df.columns)      

print(df.dtypes)

print("Total Students:", len(df))

#counts the how many students passed(FinalResult =1)

passed_students = df[df["FinalResult"] == 1]

print("Total Passed Students:", len(passed_students))

#counts the how many students failed(FinalResult =0)
failed_students = df[df["FinalResult"] == 0]
print("Total Failed Students:", len(failed_students))

#Average study hours of students
average_hours = df["StudyHours"].mean()

print("Average Study Hours:", average_hours)

#Average Attendence
average_attendance = df["Attendance"].mean()

print("Average Attendance:", average_attendance)

#Maximum Previous Score

max_score = df["PreviousScore"].max()

print("Maximum Previous Score:", max_score)
#Minimum Sleep Hours
min_sleep = df["SleepHours"].min()

print("Minimum Sleep Hours:", min_sleep)
#Value counts of FinalResult
print(df["FinalResult"].value_counts())

#Calculate percentage

print(df["FinalResult"].value_counts(normalize=True) * 100)
 #
counts = df["FinalResult"].value_counts()
percentage = df["FinalResult"].value_counts(normalize=True) * 100

print("Counts:\n", counts)
print("\nPercentage:\n", percentage)

#PLot histogram of StudyHours

plt.hist(df["StudyHours"], bins=10)
plt.xlabel("Study Hours")
plt.ylabel("Number of Students")
plt.title("Histogram of Study Hours")

plt.show()


# Separate Pass and Fail students
pass_students = df[df["FinalResult"] == 1]
fail_students = df[df["FinalResult"] == 0]

# Create scatter plot
plt.scatter(pass_students["StudyHours"], pass_students["PreviousScore"], label="Pass")
plt.scatter(fail_students["StudyHours"], fail_students["PreviousScore"], label="Fail")

plt.xlabel("Study Hours")
plt.ylabel("Previous Score")
plt.title("Study Hours vs Previous Score")
plt.legend()

plt.show()

# Boxplot for Attendance
plt.boxplot(df["Attendance"])

plt.title("Boxplot of Attendance")
plt.ylabel("Attendance")

plt.show()

pass_students = df[df["FinalResult"] == 1]
fail_students = df[df["FinalResult"] == 0]

plt.scatter(pass_students["AssignmentsCompleted"], pass_students["FinalResult"], label="Pass")
plt.scatter(fail_students["AssignmentsCompleted"], fail_students["FinalResult"], label="Fail")

plt.xlabel("Assignments Completed")
plt.ylabel("Final Result")
plt.title("Assignments Completed vs Final Result")

plt.legend()
plt.show()
#Plot SleepHours against FinalResult

pass_students = df[df["FinalResult"] == 1]
fail_students = df[df["FinalResult"] == 0]

plt.scatter(pass_students["SleepHours"], pass_students["FinalResult"], label="Pass")
plt.scatter(fail_students["SleepHours"], fail_students["FinalResult"], label="Fail")

plt.xlabel("Sleep Hours")
plt.ylabel("Final Result")
plt.title("Sleep Hours vs Final Result")

plt.legend()
plt.show()