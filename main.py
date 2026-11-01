from pathlib import Path
import subprocess
import sys


def run_script(script_name):
    script_path = Path(__file__).resolve().parent / script_name

    if not script_path.exists():
        print(f"\nError: {script_name} file not found!")
        return

    subprocess.run([sys.executable, str(script_path)], check=False)


print("\n======================================")
print("     STUDENT STUDY HABIT ANALYZER")
print("======================================")

while True:

    print("\n========== MAIN MENU ==========")
    print("1. Train Machine Learning Model")
    print("2. Predict Student Performance")
    print("3. View Analytics Dashboard")
    print("4. View All Students")
    print("5. Add New Student")
    print("6. Exit")

    choice = input("\nEnter your choice (1-6): ")

    if choice == "1":
        run_script("ml_model.py")

    elif choice == "2":
        run_script("predict_student.py")

    elif choice == "3":
        run_script("analytics.py")

    elif choice == "4":
        run_script("all_students.py")

    elif choice == "5":
        run_script("add_student.py")

    elif choice == "6":
        print("\nThank you for using Student Study Habit Analyzer!")
        print("Project closed successfully.")
        break

    else:
        print("\nInvalid choice! Please enter 1 to 6.")
