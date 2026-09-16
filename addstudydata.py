# ============================================
# ADD STUDY DATA
# ============================================




from main import save_study_data, student_exists, validate_date, validate_hours
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


