
import pandas as pd
import os

file_name = "student_data.csv"

# Check dataset
if not os.path.exists(file_name):
    print("Student dataset not found!")
    exit()

# Read existing data
df = pd.read_csv(file_name)

print("\n===== ADD NEW STUDENT =====")

# Take student details
student_id = int(input("Enter Student ID: "))
study = float(input("Enter Daily Study Hours: "))
sleep = float(input("Enter Daily Sleep Hours: "))
attendance = float(input("Enter Attendance Percentage: "))
marks = float(input("Enter Student Marks: "))

# Validate input
if not (0 <= study <= 24 and
        0 <= sleep <= 24 and
        0 <= attendance <= 100 and
        0 <= marks <= 100):
    print("Invalid input! Please enter valid values.")

elif student_id in df["Student_ID"].values:
    print("Student ID already exists!")

else:
    new_student = pd.DataFrame([{
        "Student_ID": student_id,
        "Study_Hours": study,
        "Sleep_Hours": sleep,
        "Attendance": attendance,
        "Marks": marks
    }])

    # Add new student to CSV
    df = pd.concat([df, new_student], ignore_index=True)
    df.to_csv(file_name, index=False)

    print("\nStudent added successfully!")
    print(new_student.to_string(index=False))
