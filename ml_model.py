
import pandas as pd
from pathlib import Path
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import (
    accuracy_score,
    classification_report,
    precision_score,
    recall_score,
    f1_score
)
from tabulate import tabulate

file_path = Path(__file__).resolve().parent / "student_data.csv"

print("\n" + "=" * 65)
print("              MACHINE LEARNING MODEL")
print("                  TRAINING REPORT")
print("=" * 65)

try:
    df = pd.read_csv(file_path)

    # Performance categories
    df["Performance"] = df["Marks"].apply(
        lambda x: "Good" if x >= 75
        else "Average" if x >= 50
        else "Needs Improvement"
    )

    X = df[["Study_Hours", "Sleep_Hours", "Attendance"]]
    y = df["Performance"]

    # Split dataset
    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.3,
        random_state=42,
        stratify=y
    )

    # Train model
    model = RandomForestClassifier(
        n_estimators=100,
        random_state=42
    )

    model.fit(X_train, y_train)

    # Prediction
    y_pred = model.predict(X_test)

    # Calculate metrics
    accuracy = accuracy_score(y_test, y_pred)
    precision = precision_score(
        y_test, y_pred, average="weighted", zero_division=0
    )
    recall = recall_score(
        y_test, y_pred, average="weighted", zero_division=0
    )
    f1 = f1_score(
        y_test, y_pred, average="weighted", zero_division=0
    )

    # Main result table
    results = [
        ["Accuracy", f"{accuracy * 100:.2f}%"],
        ["Precision", f"{precision * 100:.2f}%"],
        ["Recall", f"{recall * 100:.2f}%"],
        ["F1-Score", f"{f1 * 100:.2f}%"]
    ]

    print("\n MODEL PERFORMANCE")
    print(tabulate(
        results,
        headers=["Evaluation Metric", "Score"],
        tablefmt="fancy_grid"
    ))

    # Classification report
    report = classification_report(
        y_test,
        y_pred,
        output_dict=True,
        zero_division=0
    )

    report_data = []

    for category in ["Average", "Good", "Needs Improvement"]:
        if category in report:
            values = report[category]
            report_data.append([
                category,
                f"{values['precision']:.2f}",
                f"{values['recall']:.2f}",
                f"{values['f1-score']:.2f}",
                int(values["support"])
            ])

    print("\n CLASSIFICATION REPORT")
    print(tabulate(
        report_data,
        headers=["Category", "Precision", "Recall", "F1-Score", "Support"],
        tablefmt="grid"
    ))

    print("\n" + "=" * 65)
    print("           MODEL TRAINED SUCCESSFULLY")
    print("=" * 65)

except FileNotFoundError:
    print("\nError: student_data.csv file not found!")

except Exception as e:
    print("\nError:", e)

input("\nPress Enter to return to Main Menu...")
