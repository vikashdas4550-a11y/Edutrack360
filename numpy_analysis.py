# ============================================
# EDUTRACK360
# NUMPY STUDENT ANALYSIS
# ============================================

import numpy as np


def numpy_analysis(students, study_data):

    print("\n" + "=" * 60)
    print("          NUMPY STUDENT PERFORMANCE ANALYSIS")
    print("=" * 60)

    # Check study data
    if not study_data:
        print("\n❌ No study data available!")
        print("Please add study data first.")
        return

    # --------------------------------------------
    # SEARCH STUDENT BY ID
    # --------------------------------------------

    student_id = input("\nEnter Student ID: ").strip()

    student = None

    for s in students:
        if s["id"].strip() == student_id:
            student = s
            break

    if student is None:
        print("\n❌ Student not found!")
        return

    # --------------------------------------------
    # FILTER STUDY DATA
    # --------------------------------------------

    student_records = []

    for record in study_data:
        if record["student_id"].strip() == student_id:
            student_records.append(record)

    if not student_records:
        print("\n❌ No study records found for this student!")
        return

    # --------------------------------------------
    # CONVERT DATA INTO NUMPY ARRAYS
    # --------------------------------------------

    try:

        study_hours = np.array([
            float(record["study_hours"])
            for record in student_records
        ])

        sleep_hours = np.array([
            float(record["sleep_hours"])
            for record in student_records
        ])

        phone_hours = np.array([
            float(record["phone_hours"])
            for record in student_records
        ])

        break_hours = np.array([
            float(record["break_hours"])
            for record in student_records
        ])

        marks = np.array([
            float(record["marks"])
            for record in student_records
        ])

    except ValueError:
        print("\n❌ Invalid numerical data found!")
        return

    # --------------------------------------------
    # NUMPY CALCULATIONS
    # --------------------------------------------

    average_study = np.mean(study_hours)
    average_sleep = np.mean(sleep_hours)
    average_phone = np.mean(phone_hours)
    average_break = np.mean(break_hours)
    average_marks = np.mean(marks)

    minimum_marks = np.min(marks)
    maximum_marks = np.max(marks)

    study_std = np.std(study_hours)
    marks_std = np.std(marks)

    # --------------------------------------------
    # STUDENT INFORMATION
    # --------------------------------------------

    print("\n" + "-" * 60)
    print("                 STUDENT INFORMATION")
    print("-" * 60)

    print("Student ID :", student["id"])
    print("Name       :", student["name"])
    print("Course     :", student["course"])
    print("Semester   :", student["semester"])

    # --------------------------------------------
    # NUMPY ANALYSIS
    # --------------------------------------------

    print("\n" + "-" * 60)
    print("                 NUMPY ANALYSIS")
    print("-" * 60)

    print("Records Analyzed    :", len(student_records))

    print("Average Study Hours :", round(average_study, 2))
    print("Average Sleep Hours :", round(average_sleep, 2))
    print("Average Phone Usage :", round(average_phone, 2))
    print("Average Break Hours :", round(average_break, 2))

    print("Average Marks       :", round(average_marks, 2))
    print("Minimum Marks       :", round(minimum_marks, 2))
    print("Maximum Marks       :", round(maximum_marks, 2))

    print("Study Hours Std Dev :", round(study_std, 2))
    print("Marks Std Dev       :", round(marks_std, 2))

    # --------------------------------------------
    # PRODUCTIVITY SCORE
    # --------------------------------------------

    study_score = min((average_study / 8) * 40, 40)

    if 7 <= average_sleep <= 9:
        sleep_score = 20
    elif 6 <= average_sleep < 7 or 9 < average_sleep <= 10:
        sleep_score = 15
    else:
        sleep_score = 10

    marks_score = (average_marks / 100) * 30

    if average_phone <= 2:
        phone_score = 10
    elif average_phone <= 4:
        phone_score = 7
    elif average_phone <= 6:
        phone_score = 4
    else:
        phone_score = 2

    productivity_score = (
        study_score
        + sleep_score
        + marks_score
        + phone_score
    )

    # --------------------------------------------
    # PERFORMANCE LEVEL
    # --------------------------------------------

    if productivity_score >= 80:
        performance = "Excellent"
    elif productivity_score >= 65:
        performance = "Good"
    elif productivity_score >= 50:
        performance = "Average"
    else:
        performance = "Needs Improvement"

    print("\n" + "-" * 60)
    print("              PRODUCTIVITY ANALYSIS")
    print("-" * 60)

    print("Study Score        :", round(study_score, 2), "/ 40")
    print("Sleep Score        :", round(sleep_score, 2), "/ 20")
    print("Marks Score        :", round(marks_score, 2), "/ 30")
    print("Phone Usage Score  :", round(phone_score, 2), "/ 10")

    print(
        "Productivity Score :",
        round(productivity_score, 2),
        "/ 100"
    )

    print("Performance Level  :", performance)

    # --------------------------------------------
    # SUBJECT-WISE ANALYSIS
    # --------------------------------------------

    print("\n" + "-" * 60)
    print("              SUBJECT-WISE ANALYSIS")
    print("-" * 60)

    subjects = {}

    for record in student_records:

        subject = record["subject"]

        if subject not in subjects:
            subjects[subject] = []

        subjects[subject].append(
            float(record["marks"])
        )

    for subject, subject_marks in subjects.items():

        subject_array = np.array(subject_marks)

        subject_average = np.mean(subject_array)

        print(
            f"{subject:<20} Average Marks : "
            f"{subject_average:.2f}"
        )

    # --------------------------------------------
    # RECOMMENDATIONS
    # --------------------------------------------

    print("\n" + "-" * 60)
    print("                 RECOMMENDATIONS")
    print("-" * 60)

    recommendation_found = False

    if average_study < 4:
        print("📚 Increase your daily study hours.")
        recommendation_found = True

    if average_sleep < 7:
        print("😴 Try to maintain at least 7 hours of sleep.")
        recommendation_found = True

    if average_phone > 4:
        print("📱 Reduce unnecessary phone usage.")
        recommendation_found = True

    if average_break > 3:
        print("☕ Try to reduce excessive break time.")
        recommendation_found = True

    if average_marks < 50:
        print("📝 Focus more on revision and practice.")
        recommendation_found = True

    elif average_marks < 75:
        print("📝 Increase revision to improve your marks.")
        recommendation_found = True

    if not recommendation_found:
        print("🎉 Good study habits! Keep maintaining your routine.")

    print("=" * 60)