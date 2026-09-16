# ============================================
# ANALYZE PERFORMANCE
# ============================================

def analyze_performance(students, study_data):

    print("\n" + "=" * 60)
    print("                 PERFORMANCE ANALYZER")
    print("=" * 60)

    # Check study data
    if len(study_data) == 0:
        print("\n❌ No study data available.")
        print("Please add study data first using Option 6.")
        return

    # Get Student ID
    student_id = input("Enter Student ID: ").strip()

    # Check student
    student = None

    for s in students:
        if s["id"] == student_id:
            student = s
            break

    if student is None:
        print("\n❌ Student not found!")
        return

    # Get student's study records
    student_records = []

    for record in study_data:
        if record["student_id"] == student_id:
            student_records.append(record)

    # Check records
    if len(student_records) == 0:
        print("\n❌ No study records found for this student.")
        print("Please add study data using Option 6.")
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

    sleep_score = 0

    if 7 <= avg_sleep <= 9:
        sleep_score = 20
    elif 6 <= avg_sleep < 7 or 9 < avg_sleep <= 10:
        sleep_score = 15
    else:
        sleep_score = 10

    marks_score = (avg_marks / 100) * 30

    phone_score = 10

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
    # DISPLAY RESULT
    # ============================================

    print("\n" + "=" * 60)
    print("              PERFORMANCE REPORT")
    print("=" * 60)

    print("Student ID   :", student["id"])
    print("Student Name :", student["name"])
    print("Course       :", student["course"])
    print("Semester     :", student["semester"])

    print("-" * 60)

    print("Records Analyzed      :", total_records)
    print("Average Study Hours   :", round(avg_study, 2))
    print("Average Sleep Hours   :", round(avg_sleep, 2))
    print("Average Phone Usage   :", round(avg_phone, 2))
    print("Average Break Hours   :", round(avg_break, 2))
    print("Average Marks         :", round(avg_marks, 2))

    print("-" * 60)

    print("Productivity Score    :", round(productivity_score, 2), "/ 100")
    print("Performance Level     :", performance)

    print("-" * 60)

    # ============================================
    # RECOMMENDATIONS
    # ============================================

    print("                 RECOMMENDATIONS")
    print("-" * 60)

    recommendation_found = False

    if avg_study < 4:
        print("📚 Increase daily study time.")
        recommendation_found = True

    if avg_sleep < 7:
        print("😴 Try to maintain at least 7 hours of sleep.")
        recommendation_found = True

    if avg_phone > 4:
        print("📱 Reduce unnecessary phone usage during study.")
        recommendation_found = True

    if avg_break > 3:
        print("☕ Try to reduce excessive break time.")
        recommendation_found = True

    if avg_marks < 50:
        print("📝 Focus more on revision and practice tests.")
        recommendation_found = True
    elif avg_marks < 75:
        print("📝 Increase revision and practice to improve marks.")
        recommendation_found = True

    if avg_study >= 4 and 7 <= avg_sleep <= 9 and avg_phone <= 4 and avg_marks >= 75:
        print("🎉 Excellent study habits! Keep maintaining your routine.")
        recommendation_found = True

    if not recommendation_found:
        print("✅ Keep following your current routine.")

    print("=" * 60)