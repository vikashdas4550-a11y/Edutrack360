# ============================================
# Edutrack360
# Student Behavior & Study Pattern Analyzer

# ============================================

import csv
import os
import re
import pandas as pd
import numpy as np
from datetime import datetime
from analyze import analyze_performance
from matplotlib_analysis import matplotlib_analysis
from numpy_analysis import numpy_analysis
from pandas_analysis import pandas_analysis
from studentsearch import search_student
from deletestudent import delete_student





# ============================================
# INPUT VALIDATION FUNCTIONS
# ============================================

def validate_student_id(student_id):

    if student_id == "":
        return False

    if not student_id.isdigit():
        return False

    return True


def validate_name(name):

    if name == "":
        return False

    if not name.replace(" ", "").isalpha():
        return False

    return True


def validate_semester(semester):

    if not semester.isdigit():
        return False

    semester = int(semester)

    if semester < 1 or semester > 8:
        return False

    return True

# ============================================
# FILE PATH
# ============================================

DATA_FOLDER = "data"
STUDENT_FILE = os.path.join(DATA_FOLDER, "students.csv")
STUDY_FILE = os.path.join(DATA_FOLDER, "study_data.csv")
REPORT_FOLDER = "reports"


# ============================================
# CREATE DATA FOLDER
# ============================================

def create_data_folder():

    if not os.path.exists(DATA_FOLDER):

        os.makedirs(DATA_FOLDER)
# ============================================
# CREATE REPORT FOLDER
# ============================================

def create_report_folder():

    if not os.path.exists(REPORT_FOLDER):
        os.makedirs(REPORT_FOLDER)

# ============================================
# LOAD STUDENTS FROM CSV
# ============================================

def load_students():

    students = []

    create_data_folder()

    if not os.path.exists(STUDENT_FILE):
        return students

    try:

        with open(
            STUDENT_FILE,
            "r",
            newline="",
            encoding="utf-8"
        ) as file:

            reader = csv.DictReader(file)

            for row in reader:

                students.append(row)

    except Exception as e:

        print("❌ Error while loading student data:", e)

    return students


# ============================================
# SAVE STUDENTS TO CSV
# ============================================

def save_students(students):

    create_data_folder()
    create_report_folder()

    try:

        with open(
            STUDENT_FILE,
            "w",
            newline="",
            encoding="utf-8"
        ) as file:

            fieldnames = [
                "id",
                "name",
                "course",
                "semester"
            ]

            writer = csv.DictWriter(
                file,
                fieldnames=fieldnames
            )

            writer.writeheader()

            writer.writerows(students)

    except Exception as e:

        print("❌ Error while saving student data:", e)

# ============================================
# SAVE STUDY DATA
# ============================================

def save_study_data(study_data):

    create_data_folder()
    create_report_folder()

    try:

        with open(
            STUDY_FILE,
            "w",
            newline="",
            encoding="utf-8"
        ) as file:

            fieldnames = [
                "student_id",
                "date",
                "subject",
                "study_hours",
                "sleep_hours",
                "phone_hours",
                "break_hours",
                "study_time",
                "mood",
                "marks"
            ]

            writer = csv.DictWriter(
                file,
                fieldnames=fieldnames
            )

            writer.writeheader()
            writer.writerows(study_data)

    except PermissionError:

        print("❌ Permission denied!")
        print("Please close study_data.csv if it is open.")

    except OSError as e:

        print("❌ File error:", e)

    except Exception as e:

        print("❌ Unexpected error:", e)

# ============================================
# LOAD STUDY DATA
# ============================================

def load_study_data():

    study_data = []

    create_data_folder()
    create_report_folder()

    if not os.path.exists(STUDY_FILE):
        return study_data

    try:

        with open(
            STUDY_FILE,
            "r",
            newline="",
            encoding="utf-8"
        ) as file:

            reader = csv.DictReader(
                file,
                skipinitialspace=True
            )

            for row in reader:

                study_data.append(row)

    except FileNotFoundError:

        print("❌ Study data file not found.")

    except PermissionError:

        print("❌ Permission denied while reading study data.")

    except Exception as e:

        print("❌ Unexpected error:", e)

    return study_data
        
# ============================================
# VALIDATE DATE
# ============================================

def validate_date(date_text):

    try:

        datetime.strptime(
            date_text,
            "%d-%m-%Y"
        )

        return True

    except ValueError:

        return False

# ============================================
# VALIDATE HOURS
# ============================================

def validate_hours(value, minimum, maximum):

    try:

        value = float(value)

        if minimum <= value <= maximum:

            return True

        return False

    except ValueError:

        return False
        
# ============================================
# SHOW MENU
# ============================================

def show_menu():

    print("\n" + "=" * 55)
    print("                  EDUTRACK360")
    print("        Student Behavior & Study Pattern Analyzer")
    print("=" * 55)

    print("1. Add Student")
    print("2. View All Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Add Study Data")
    print("7. Analyze Performance")
    print("8. Generate Report")
    print("9. Pandas Data Analysis")
    print("10. Numpy Data Analysis")
    
    print("11. Matplotlib Data Visualization")
    print("12. Exit")

    print("=" * 55)


# ============================================
# CHECK STUDENT
# ============================================

def student_exists(students, student_id):

    for student in students:

        if student["id"] == student_id:

            return True

    return False


# ============================================
# ADD STUDENT
# ============================================

def add_student(students):

    print("\n" + "-" * 55)
    print("                  ADD STUDENT")
    print("-" * 55)

    # ----------------------------------------
    # STUDENT ID
    # ----------------------------------------

    student_id = input("Enter Student ID: ").strip()

    if not validate_student_id(student_id):

        print("❌ Invalid Student ID!")
        print("Student ID must contain numbers only.")

        return

    # ----------------------------------------
    # DUPLICATE ID CHECK
    # ----------------------------------------

    if student_exists(students, student_id):

        print("❌ Student ID already exists!")
        print("Please enter a different Student ID.")

        return

    # ----------------------------------------
    # STUDENT NAME
    # ----------------------------------------

    name = input("Enter Student Name: ").strip()

    if not validate_name(name):

        print("❌ Invalid student name!")
        print("Name should contain letters only.")

        return

    # ----------------------------------------
    # COURSE
    # ----------------------------------------

    course = input("Enter Course: ").strip()

    if course == "":

        print("❌ Course cannot be empty.")

        return

    # ----------------------------------------
    # SEMESTER
    # ----------------------------------------

    semester = input("Enter Semester: ").strip()

    if not validate_semester(semester):

        print("❌ Invalid semester!")
        print("Semester must be between 1 and 8.")

        return

    # ----------------------------------------
    # CREATE STUDENT
    # ----------------------------------------

    student = {
        "id": student_id,
        "name": name,
        "course": course,
        "semester": semester
    }

    # ----------------------------------------
    # ADD TO LIST
    # ----------------------------------------

    students.append(student)

    # ----------------------------------------
    # SAVE TO CSV
    # ----------------------------------------

    save_students(students)

    # ----------------------------------------
    # SUCCESS MESSAGE
    # ----------------------------------------

    print("\n" + "-" * 55)
    print("✅ STUDENT REGISTERED SUCCESSFULLY!")
    print("-" * 55)

    print("Student ID :", student_id)
    print("Name       :", name)
    print("Course     :", course)
    print("Semester   :", semester)

    print("-" * 55)
    print("💾 Data saved to students.csv")


# ============================================
# VIEW STUDENTS
# ============================================

def view_students(students):

    print("\n" + "-" * 55)
    print("                ALL STUDENTS")
    print("-" * 55)

    if len(students) == 0:

        print("No students registered yet.")
        return

    for student in students:

        print(f"""
Student ID : {student["id"]}
Name       : {student["name"]}
Course     : {student["course"]}
Semester   : {student["semester"]}
{"-" * 40}
""")



# ============================================
# UPDATE STUDENT
# ============================================

def update_student(students):

    print("\n" + "-" * 55)
    print("                UPDATE STUDENT")
    print("-" * 55)

    student_id = input("Enter Student ID: ").strip()

    for student in students:

        if student["id"] == student_id:

            print("\nStudent Found!")

            new_name = input(
                f"Enter new name [{student['name']}]: "
            ).strip()

            new_course = input(
                f"Enter new course [{student['course']}]: "
            ).strip()

            new_semester = input(
                f"Enter new semester [{student['semester']}]: "
            ).strip()

            if new_name != "":
                student["name"] = new_name

            if new_course != "":
                student["course"] = new_course

            if new_semester != "":
                student["semester"] = new_semester

            save_students(students)

            print("\n✅ Student updated successfully!")
            print("Changes saved to students.csv")

            return

    print("\n❌ Student not found.")




# ============================================
# ADD STUDY DATA
# ============================================

def add_study_data(students, study_data):

    print("\n" + "-" * 55)
    print("                 ADD STUDY DATA")
    print("-" * 55)

    student_id = input("Enter Student ID: ").strip()

    # Check student
    if not student_exists(students, student_id):
        print("❌ Student not found!")
        print("Please register the student first.")
        return

    date = input("Enter Date (DD-MM-YYYY): ").strip()

    if not validate_date(date):
        print("❌ Invalid date!")
        print("Use format: DD-MM-YYYY")
        return

    subject = input("Enter Subject: ").strip()

    if subject == "":
        print("❌ Subject cannot be empty.")
        return

    study_hours = input("Enter Study Hours: ").strip()

    if not validate_hours(study_hours, 0, 24):
        print("❌ Study hours must be between 0 and 24.")
        return

    sleep_hours = input("Enter Sleep Hours: ").strip()

    if not validate_hours(sleep_hours, 0, 24):
        print("❌ Sleep hours must be between 0 and 24.")
        return

    phone_hours = input("Enter Phone Usage Hours: ").strip()

    if not validate_hours(phone_hours, 0, 24):
        print("❌ Phone usage must be between 0 and 24.")
        return

    break_hours = input("Enter Break Hours: ").strip()

    if not validate_hours(break_hours, 0, 24):
        print("❌ Break hours must be between 0 and 24.")
        return

    study_time = input("Enter Study Time (Morning/Afternoon/Evening/Night): ").strip()

    if study_time == "":
        print("❌ Study time cannot be empty.")
        return

    mood = input("Enter Mood (Happy/Normal/Stressed/Tired): ").strip()

    if mood == "":
        print("❌ Mood cannot be empty.")
        return

    marks = input("Enter Test Marks (0-100): ").strip()

    if not validate_hours(marks, 0, 100):
        print("❌ Marks must be between 0 and 100.")
        return

    # Create study record
    record = {
        "student_id": student_id,
        "date": date,
        "subject": subject,
        "study_hours": study_hours,
        "sleep_hours": sleep_hours,
        "phone_hours": phone_hours,
        "break_hours": break_hours,
        "study_time": study_time,
        "mood": mood,
        "marks": marks
    }

    study_data.append(record)

    # Save data
    save_study_data(study_data)

    print("\n" + "-" * 55)
    print("✅ STUDY DATA SAVED SUCCESSFULLY!")
    print("-" * 55)

    print("Student ID  :", student_id)
    print("Date        :", date)
    print("Subject     :", subject)
    print("Study Hours :", study_hours)
    print("Sleep Hours :", sleep_hours)
    print("Phone Usage :", phone_hours)
    print("Break Hours :", break_hours)
    print("Study Time  :", study_time)
    print("Mood        :", mood)
    print("Marks       :", marks)

    print("-" * 55)



# ============================================
# GENERATE REPORT
# ============================================

def generate_report(students, study_data):

    print("\n" + "=" * 60)
    print("                  GENERATE REPORT")
    print("=" * 60)

    # Check study data
    if len(study_data) == 0:
        print("\n❌ No study data available.")
        print("Please add study data using Option 6.")
        return

    # Get Student ID
    student_id = input("Enter Student ID: ").strip()

    # Find student
    student = None

    for s in students:
        if s["id"] == student_id:
            student = s
            break

    if student is None:
        print("\n❌ Student not found!")
        return

    # Find study records
    student_records = []

    for record in study_data:
        if record["student_id"] == student_id:
            student_records.append(record)

    if len(student_records) == 0:
        print("\n❌ No study records found for this student.")
        return

    # ============================================
    # CALCULATE TOTALS
    # ============================================

    total_study = 0
    total_sleep = 0
    total_phone = 0
    total_break = 0
    total_marks = 0

    for record in student_records:

        total_study += float(record["study_hours"])
        total_sleep += float(record["sleep_hours"])
        total_phone += float(record["phone_hours"])
        total_break += float(record["break_hours"])
        total_marks += float(record["marks"])

    total_records = len(student_records)

    # ============================================
    # CALCULATE AVERAGES
    # ============================================

    avg_study = total_study / total_records
    avg_sleep = total_sleep / total_records
    avg_phone = total_phone / total_records
    avg_break = total_break / total_records
    avg_marks = total_marks / total_records

    # ============================================
    # PRODUCTIVITY SCORE
    # ============================================

    study_score = min(avg_study / 8 * 40, 40)

    if 7 <= avg_sleep <= 9:
        sleep_score = 20
    elif 6 <= avg_sleep < 7 or 9 < avg_sleep <= 10:
        sleep_score = 15
    else:
        sleep_score = 10

    marks_score = (avg_marks / 100) * 30

    if avg_phone <= 2:
        phone_score = 10
    elif avg_phone <= 4:
        phone_score = 7
    elif avg_phone <= 6:
        phone_score = 4
    else:
        phone_score = 2

    productivity_score = (
        study_score
        + sleep_score
        + marks_score
        + phone_score
    )

    # ============================================
    # PERFORMANCE LEVEL
    # ============================================

    if productivity_score >= 80:
        performance = "Excellent"
    elif productivity_score >= 65:
        performance = "Good"
    elif productivity_score >= 50:
        performance = "Average"
    else:
        performance = "Needs Improvement"

    # ============================================
    # CREATE REPORT FOLDER
    # ============================================

    create_report_folder()

    report_file = os.path.join(
        REPORT_FOLDER,
        f"student_{student_id}_report.txt"
    )

    # ============================================
    # WRITE REPORT
    # ============================================

    try:

        with open(
            report_file,
            "w",
            encoding="utf-8"
        ) as file:

            file.write("=" * 60 + "\n")
            file.write("              EDUTRACK360\n")
            file.write("       STUDENT PERFORMANCE REPORT\n")
            file.write("=" * 60 + "\n\n")

            # Student information
            file.write("STUDENT INFORMATION\n")
            file.write("-" * 60 + "\n")

            file.write(f"Student ID   : {student['id']}\n")
            file.write(f"Student Name : {student['name']}\n")
            file.write(f"Course       : {student['course']}\n")
            file.write(f"Semester     : {student['semester']}\n")

            file.write("\n")

            # Study summary
            file.write("STUDY SUMMARY\n")
            file.write("-" * 60 + "\n")

            file.write(
                f"Records Analyzed    : {total_records}\n"
            )

            file.write(
                f"Average Study Hours : {avg_study:.2f}\n"
            )

            file.write(
                f"Average Sleep Hours : {avg_sleep:.2f}\n"
            )

            file.write(
                f"Average Phone Usage : {avg_phone:.2f}\n"
            )

            file.write(
                f"Average Break Hours : {avg_break:.2f}\n"
            )

            file.write(
                f"Average Marks       : {avg_marks:.2f}\n"
            )

            file.write("\n")

            # Performance
            file.write("PERFORMANCE ANALYSIS\n")
            file.write("-" * 60 + "\n")

            file.write(
                f"Productivity Score : {productivity_score:.2f}/100\n"
            )

            file.write(
                f"Performance Level  : {performance}\n"
            )

            file.write("\n")

            # Recommendations
            file.write("RECOMMENDATIONS\n")
            file.write("-" * 60 + "\n")

            recommendation_found = False

            if avg_study < 4:
                file.write(
                    "- Increase daily study time.\n"
                )
                recommendation_found = True

            if avg_sleep < 7:
                file.write(
                    "- Try to maintain at least 7 hours of sleep.\n"
                )
                recommendation_found = True

            if avg_phone > 4:
                file.write(
                    "- Reduce unnecessary phone usage during study.\n"
                )
                recommendation_found = True

            if avg_break > 3:
                file.write(
                    "- Try to reduce excessive break time.\n"
                )
                recommendation_found = True

            if avg_marks < 50:
                file.write(
                    "- Focus more on revision and practice tests.\n"
                )
                recommendation_found = True

            elif avg_marks < 75:
                file.write(
                    "- Increase revision and practice to improve marks.\n"
                )
                recommendation_found = True

            if (
                avg_study >= 4
                and 7 <= avg_sleep <= 9
                and avg_phone <= 4
                and avg_marks >= 75
            ):
                file.write(
                    "- Excellent study habits! Keep maintaining your routine.\n"
                )
                recommendation_found = True

            if not recommendation_found:
                file.write(
                    "- Keep following your current routine.\n"
                )

            file.write("\n")
            file.write("=" * 60 + "\n")
            file.write("Report generated by Edutrack360\n")
            file.write("=" * 60 + "\n")

        # ========================================
        # SUCCESS MESSAGE
        # ========================================

        print("\n" + "-" * 60)
        print("✅ REPORT GENERATED SUCCESSFULLY!")
        print("-" * 60)

        print("Student ID :", student_id)
        print("Student    :", student["name"])
        print("Report     :", report_file)

        print("-" * 60)

    except PermissionError:

        print("\n❌ Permission denied!")
        print("Please check the reports folder.")

    except OSError as e:

        print("\n❌ File error:", e)

    except Exception as e:

        print("\n❌ Unexpected error:", e)


       
# ============================================
# MAIN PROGRAM
# ============================================

students = load_students()
study_data = load_study_data()
print("\n✅ Student data loaded successfully.")


while True:

    show_menu()

    choice = input("Enter your choice: ").strip()

    if choice == "1":

        add_student(students)

    elif choice == "2":

        view_students(students)

    elif choice == "3":

        search_student(students)

    elif choice == "4":

        update_student(students)

    elif choice == "5":

        delete_student(students , save_students)

    elif choice == "6":

        add_study_data(students, study_data)

    elif choice == "7":
 
        analyze_performance(students, study_data)

    elif choice == "8":

        generate_report(students, study_data)
    

    elif choice == "9":
      pandas_analysis()

    elif choice == "10":
      numpy_analysis( students, study_data) 

    elif choice == "11":
      matplotlib_analysis()       

    elif choice == "12":

        print("\nThank you for using StudySense! 👋")
        break

    else:

        print("\n❌ Invalid choice!")
        print("Please enter a number between 1 and 12.")
