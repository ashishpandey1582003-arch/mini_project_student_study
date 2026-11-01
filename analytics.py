import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load CSV dataset
df = pd.read_csv("student_data.csv")

print("================================")
print(" STUDENT ANALYTICS DASHBOARD")
print("================================")

# 1. Total Students
print("\nTotal Students:", len(df))

# 2. Average Marks
print("Average Marks:", round(np.mean(df["Marks"]), 2))

# 3. Average Study Hours
print("Average Study Hours:",
      round(np.mean(df["Study_Hours"]), 2))

# 4. Average Attendance
print("Average Attendance:",
      round(np.mean(df["Attendance"]), 2), "%")

# 5. Top Performing Student
top_student = df.loc[df["Marks"].idxmax()]

print("\nTop Performing Student:")
print("Student ID:", top_student["Student_ID"])
print("Marks:", top_student["Marks"])

# 6. Performance Categories
df["Performance"] = np.where(
    df["Marks"] >= 75, "Good",
    np.where(df["Marks"] >= 50, "Average",
             "Needs Improvement")
)

print("\nPerformance Distribution:")
print(df["Performance"].value_counts())

# 7. Marks Comparison Chart
plt.figure(figsize=(9, 5))

plt.bar(df["Student_ID"], df["Marks"])

plt.xlabel("Student ID")
plt.ylabel("Marks")
plt.title("Student Marks Comparison")

plt.xticks(df["Student_ID"])
plt.savefig("marks_chart.png")
plt.show()

# 8. Study Hours Chart
plt.figure(figsize=(9, 5))

plt.plot(
    df["Student_ID"],
    df["Study_Hours"],
    marker="o"
)

plt.xlabel("Student ID")
plt.ylabel("Study Hours")
plt.title("Student Study Hours Analysis")

plt.savefig("study_hours_chart.png")
plt.show()

print("\nAnalytics completed successfully!")
