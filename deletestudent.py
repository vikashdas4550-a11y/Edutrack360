# ============================================
# DELETE STUDENT
# ============================================

def delete_student(students, save_students):

    print("\n" + "-" * 55)
    print("                DELETE STUDENT")
    print("-" * 55)

    student_id = input("Enter Student ID: ").strip()

    for student in students:

        if student["id"] == student_id:

            print("\nStudent Found!")
            print("Name:", student["name"])

            confirm = input(
                "Are you sure? (yes/no): "
            ).strip().lower()

            if confirm == "yes":

                students.remove(student)

                save_students(students)

                print("\n✅ Student deleted successfully!")
                print("Changes saved to students.csv")

            else:

                print("\n❌ Delete operation cancelled.")

            return

    print("\n❌ Student not found.")