import pandas as pd
from sklearn.ensemble import RandomForestClassifier

# Load dataset
data = pd.read_csv("student_data.csv")

# Create target categories
data["Performance"] = data["Marks"].apply(
    lambda x: "Good" if x >= 75
    else "Average" if x >= 50
    else "Needs Improvement"
)

# Input features
X = data[["Study_Hours", "Sleep_Hours", "Attendance"]]
y = data["Performance"]

# Train model
model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)

model.fit(X, y)

print("==============================")
print(" STUDENT PERFORMANCE PREDICTOR")
print("==============================")

# Take student input
study = float(input("Enter Daily Study Hours: "))
sleep = float(input("Enter Daily Sleep Hours: "))
attendance = float(input("Enter Attendance Percentage: "))

# Validate input
if not (0 <= study <= 24 and
        0 <= sleep <= 24 and
        0 <= attendance <= 100):

    print("Invalid input! Please enter valid values.")

else:
    new_student = pd.DataFrame([{
        "Study_Hours": study,
        "Sleep_Hours": sleep,
        "Attendance": attendance
    }])

    prediction = model.predict(new_student)

    probability = model.predict_proba(new_student)[0]

    print("\n===== PREDICTION RESULT =====")
    print("Student Performance:", prediction[0])

    print("\nPrediction Probabilities:")

    for category, prob in zip(model.classes_, probability):
        print(category, ":", round(prob * 100, 2), "%")
