
# ============================================
# SEARCH STUDENT
# ============================================

def search_student(students):

    print("\n" + "-" * 55)
    print("                SEARCH STUDENT")
    print("-" * 55)

    print("\nSearch By:")
    print("1. Student ID")
    print("2. Student Name")
    print("3. Course")
    print("4. Semester")

    choice = input("\nEnter your choice: ").strip()

    # ============================================
    # SEARCH BY STUDENT ID
    # ============================================

    if choice == "1":

        search_value = input("Enter Student ID: ").strip()

        found = False

        for student in students:

            if student["id"].lower() == search_value.lower():

                print("\n✅ Student Found!")
                print("-" * 55)

                print("Student ID :", student["id"])
                print("Name       :", student["name"])
                print("Course     :", student["course"])
                print("Semester   :", student["semester"])

                print("-" * 55)

                found = True

        if not found:
            print("\n❌ Student not found.")


    # ============================================
    # SEARCH BY NAME
    # ============================================

    elif choice == "2":

        search_value = input("Enter Student Name: ").strip().lower()

        found = False

        for student in students:

            if search_value in student["name"].lower():

                print("\n✅ Student Found!")
                print("-" * 55)

                print("Student ID :", student["id"])
                print("Name       :", student["name"])
                print("Course     :", student["course"])
                print("Semester   :", student["semester"])

                print("-" * 55)

                found = True

        if not found:
            print("\n❌ Student not found.")


    # ============================================
    # SEARCH BY COURSE
    # ============================================

    elif choice == "3":

        search_value = input("Enter Course: ").strip().lower()

        found = False

        for student in students:

            if search_value in student["course"].lower():

                print("\n✅ Student Found!")
                print("-" * 55)

                print("Student ID :", student["id"])
                print("Name       :", student["name"])
                print("Course     :", student["course"])
                print("Semester   :", student["semester"])

                print("-" * 55)

                found = True

        if not found:
            print("\n❌ Student not found.")


    # ============================================
    # SEARCH BY SEMESTER
    # ============================================

    elif choice == "4":

        search_value = input("Enter Semester: ").strip()

        found = False

        for student in students:

            if student["semester"] == search_value:

                print("\n✅ Student Found!")
                print("-" * 55)

                print("Student ID :", student["id"])
                print("Name       :", student["name"])
                print("Course     :", student["course"])
                print("Semester   :", student["semester"])

                print("-" * 55)

                found = True

        if not found:
            print("\n❌ Student not found.")


    # ============================================
    # INVALID CHOICE
    # ============================================

    else:

        print("\n❌ Invalid choice!")
        print("Please select 1, 2, 3 or 4.")

