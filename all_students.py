import pandas as pd
from pathlib import Path
from tabulate import tabulate

file_path = Path(__file__).resolve().parent / "student_data.csv"

print("\n")
print("=" * 75)
print("                 STUDENT STUDY HABIT ANALYZER")
print("                    ALL STUDENTS RECORDS")
print("=" * 75)

try:
    df = pd.read_csv(file_path)

    print("\n TOTAL STUDENTS:", len(df))

    print("\n STUDENT DETAILS")
    print("-" * 75)

    print(tabulate(
        df,
        headers="keys",
        tablefmt="grid",
        showindex=False
    ))

    df["Performance"] = df["Marks"].apply(
        lambda x: "Good" if x >= 75
        else "Average" if x >= 50
        else "Needs Improvement"
    )

    print("\n PERFORMANCE SUMMARY")
    print("-" * 40)

    summary = df["Performance"].value_counts().reset_index()
    summary.columns = ["Performance", "Total Students"]

    print(tabulate(
        summary,
        headers="keys",
        tablefmt="fancy_grid",
        showindex=False
    ))

    print("\n" + "=" * 75)
    print("                 REPORT GENERATED SUCCESSFULLY")
    print("=" * 75)

except FileNotFoundError:
    print("\nError: student_data.csv file not found!")

except Exception as e:
    print("\nError:", e)

input("\nPress Enter to return to Main Menu...")
