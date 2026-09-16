# ============================================
# EDUTRACK360
# MATPLOTLIB STUDENT VISUALIZATION
# ============================================

import os
import pandas as pd
import matplotlib.pyplot as plt


STUDY_FILE = os.path.join("data", "study_data.csv")
STUDENT_FILE = os.path.join("data", "students.csv")


# ============================================
# MATPLOTLIB ANALYSIS
# ============================================

def matplotlib_analysis():

    print("\n" + "=" * 60)
    print("          STUDENT DATA VISUALIZATION")
    print("=" * 60)

    # ----------------------------------------
    # CHECK FILE
    # ----------------------------------------

    if not os.path.exists(STUDY_FILE):

        print("\n❌ study_data.csv not found!")
        print("Please add study data first.")
        return

    try:

        # ------------------------------------
        # LOAD FILES
        # ------------------------------------

        study_df = pd.read_csv(STUDY_FILE)

        if os.path.exists(STUDENT_FILE):
            student_df = pd.read_csv(STUDENT_FILE)
        else:
            student_df = pd.DataFrame()

        if study_df.empty:

            print("\n❌ No study data available.")
            return

        # ------------------------------------
        # ENTER STUDENT ID
        # ------------------------------------

        student_id = input(
            "\nEnter Student ID for visualization: "
        ).strip()

        # ------------------------------------
        # FILTER STUDENT DATA
        # ------------------------------------

        student_data = study_df[
            study_df["student_id"].astype(str) == student_id
        ].copy()

        if student_data.empty:

            print("\n❌ No study data found for this Student ID.")
            return

        # ------------------------------------
        # GET STUDENT INFORMATION
        # ------------------------------------

        student_name = "Unknown"
        course = "Unknown"
        semester = "Unknown"

        if not student_df.empty:

            student_df["id"] = student_df["id"].astype(str)

            student_info = student_df[
                student_df["id"] == student_id
            ]

            if not student_info.empty:

                student_name = student_info.iloc[0]["name"]
                course = student_info.iloc[0]["course"]
                semester = student_info.iloc[0]["semester"]

        # ------------------------------------
        # CONVERT NUMERICAL DATA
        # ------------------------------------

        columns = [
            "study_hours",
            "sleep_hours",
            "phone_hours",
            "break_hours",
            "marks"
        ]

        for column in columns:

            student_data[column] = pd.to_numeric(
                student_data[column],
                errors="coerce"
            )

        student_data = student_data.dropna(
            subset=columns
        )

        if student_data.empty:

            print("\n❌ No valid numerical data found.")
            return

        # ------------------------------------
        # STUDENT INFORMATION
        # ------------------------------------

        print("\n" + "-" * 60)
        print("              STUDENT INFORMATION")
        print("-" * 60)

        print("Student ID :", student_id)
        print("Name       :", student_name)
        print("Course     :", course)
        print("Semester   :", semester)
        print("Records    :", len(student_data))

        print("-" * 60)

        # ====================================
        # VISUALIZATION MENU
        # ====================================

        while True:

            print("\n" + "=" * 60)
            print(
                f"       VISUALIZATION - {student_name}"
            )
            print("=" * 60)

            print("1. Study Hours Chart")
            print("2. Marks Chart")
            print("3. Sleep vs Marks")
            print("4. Phone Usage vs Marks")
            print("5. Study Hours vs Marks")
            print("6. Overall Performance")
            print("7. Show All Charts")
            print("8. Change Student")
            print("9. Exit")

            print("=" * 60)

            choice = input(
                "Enter your choice: "
            ).strip()

            # =================================
            # 1. STUDY HOURS
            # =================================

            if choice == "1":

                plt.figure(figsize=(10, 5))

                plt.bar(
                    range(1, len(student_data) + 1),
                    student_data["study_hours"]
                )

                plt.xlabel("Study Record")
                plt.ylabel("Study Hours")

                plt.title(
                    f"Study Hours Analysis\n"
                    f"{student_name} (ID: {student_id})"
                )

                plt.grid(
                    axis="y",
                    alpha=0.3
                )

                plt.tight_layout()
                plt.show()

            # =================================
            # 2. MARKS
            # =================================

            elif choice == "2":

                plt.figure(figsize=(10, 5))

                plt.plot(
                    range(1, len(student_data) + 1),
                    student_data["marks"],
                    marker="o"
                )

                plt.xlabel("Study Record")
                plt.ylabel("Marks")

                plt.title(
                    f"Marks Analysis\n"
                    f"{student_name} (ID: {student_id})"
                )

                plt.ylim(0, 100)

                plt.grid(
                    True,
                    alpha=0.3
                )

                plt.tight_layout()
                plt.show()

            # =================================
            # 3. SLEEP VS MARKS
            # =================================

            elif choice == "3":

                plt.figure(figsize=(10, 6))

                plt.scatter(
                    student_data["sleep_hours"],
                    student_data["marks"],
                    s=80,
                    alpha=0.7
                )

                plt.xlabel("Sleep Hours")
                plt.ylabel("Marks")

                plt.title(
                    f"Sleep Hours vs Marks\n"
                    f"{student_name} (ID: {student_id})"
                )

                plt.ylim(0, 100)

                plt.grid(
                    True,
                    alpha=0.3
                )

                plt.tight_layout()
                plt.show()

            # =================================
            # 4. PHONE VS MARKS
            # =================================

            elif choice == "4":

                plt.figure(figsize=(10, 6))

                plt.scatter(
                    student_data["phone_hours"],
                    student_data["marks"],
                    s=80,
                    alpha=0.7
                )

                plt.xlabel("Phone Usage Hours")
                plt.ylabel("Marks")

                plt.title(
                    f"Phone Usage vs Marks\n"
                    f"{student_name} (ID: {student_id})"
                )

                plt.ylim(0, 100)

                plt.grid(
                    True,
                    alpha=0.3
                )

                plt.tight_layout()
                plt.show()

            # =================================
            # 5. STUDY VS MARKS
            # =================================

            elif choice == "5":

                plt.figure(figsize=(10, 6))

                plt.scatter(
                    student_data["study_hours"],
                    student_data["marks"],
                    s=80,
                    alpha=0.7
                )

                plt.xlabel("Study Hours")
                plt.ylabel("Marks")

                plt.title(
                    f"Study Hours vs Marks\n"
                    f"{student_name} (ID: {student_id})"
                )

                plt.ylim(0, 100)

                plt.grid(
                    True,
                    alpha=0.3
                )

                # Correlation

                if len(student_data) >= 2:

                    correlation = student_data[
                        "study_hours"
                    ].corr(
                        student_data["marks"]
                    )

                    print(
                        "\nStudy Hours vs Marks "
                        "Correlation:",
                        round(correlation, 2)
                    )

                plt.tight_layout()
                plt.show()

            # =================================
            # 6. OVERALL PERFORMANCE
            # =================================

            elif choice == "6":

                average_study = student_data[
                    "study_hours"
                ].mean()

                average_sleep = student_data[
                    "sleep_hours"
                ].mean()

                average_phone = student_data[
                    "phone_hours"
                ].mean()

                average_marks = student_data[
                    "marks"
                ].mean()

                categories = [
                    "Study Hours",
                    "Sleep Hours",
                    "Phone Usage",
                    "Marks"
                ]

                values = [
                    average_study,
                    average_sleep,
                    average_phone,
                    average_marks
                ]

                plt.figure(figsize=(10, 6))

                plt.bar(
                    categories,
                    values
                )

                plt.ylabel("Average Value")

                plt.title(
                    f"Overall Performance\n"
                    f"{student_name} (ID: {student_id})"
                )

                plt.grid(
                    axis="y",
                    alpha=0.3
                )

                plt.tight_layout()
                plt.show()

            # =================================
            # 7. ALL CHARTS
            # =================================

            elif choice == "7":

                # Study Hours

                plt.figure(figsize=(10, 5))

                plt.bar(
                    range(1, len(student_data) + 1),
                    student_data["study_hours"]
                )

                plt.xlabel("Study Record")
                plt.ylabel("Study Hours")

                plt.title(
                    f"Study Hours - {student_name} "
                    f"(ID: {student_id})"
                )

                plt.grid(
                    axis="y",
                    alpha=0.3
                )

                plt.tight_layout()
                plt.show()

                # Marks

                plt.figure(figsize=(10, 5))

                plt.plot(
                    range(1, len(student_data) + 1),
                    student_data["marks"],
                    marker="o"
                )

                plt.xlabel("Study Record")
                plt.ylabel("Marks")

                plt.title(
                    f"Marks - {student_name} "
                    f"(ID: {student_id})"
                )

                plt.ylim(0, 100)

                plt.grid(
                    True,
                    alpha=0.3
                )

                plt.tight_layout()
                plt.show()

                # Sleep vs Marks

                plt.figure(figsize=(10, 6))

                plt.scatter(
                    student_data["sleep_hours"],
                    student_data["marks"],
                    s=80,
                    alpha=0.7
                )

                plt.xlabel("Sleep Hours")
                plt.ylabel("Marks")

                plt.title(
                    f"Sleep vs Marks - {student_name}"
                )

                plt.grid(
                    True,
                    alpha=0.3
                )

                plt.tight_layout()
                plt.show()

                # Phone vs Marks

                plt.figure(figsize=(10, 6))

                plt.scatter(
                    student_data["phone_hours"],
                    student_data["marks"],
                    s=80,
                    alpha=0.7
                )

                plt.xlabel("Phone Usage Hours")
                plt.ylabel("Marks")

                plt.title(
                    f"Phone Usage vs Marks - "
                    f"{student_name}"
                )

                plt.grid(
                    True,
                    alpha=0.3
                )

                plt.tight_layout()
                plt.show()

                # Study vs Marks

                plt.figure(figsize=(10, 6))

                plt.scatter(
                    student_data["study_hours"],
                    student_data["marks"],
                    s=80,
                    alpha=0.7
                )

                plt.xlabel("Study Hours")
                plt.ylabel("Marks")

                plt.title(
                    f"Study Hours vs Marks - "
                    f"{student_name}"
                )

                plt.grid(
                    True,
                    alpha=0.3
                )

                plt.tight_layout()
                plt.show()

            # =================================
            # 8. CHANGE STUDENT
            # =================================

            elif choice == "8":

                print(
                    "\nReturning to Student Selection..."
                )

                return matplotlib_analysis()

            # =================================
            # 9. EXIT
            # =================================

            elif choice == "9":

                print(
                    "\nReturning to main menu..."
                )

                break

            else:

                print(
                    "\n❌ Invalid choice!"
                )

    except FileNotFoundError:

        print(
            "\n❌ Required file not found!"
        )

    except KeyError as e:

        print(
            "\n❌ Required column missing:",
            e
        )

    except ValueError as e:

        print(
            "\n❌ Invalid numerical data:",
            e
        )

    except Exception as e:

        print(
            "\n❌ Unexpected error:",
            e
        )