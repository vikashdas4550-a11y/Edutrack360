# ============================================
# EDUTRACK360
# PANDAS DATA ANALYSIS
# ============================================

import os
import pandas as pd


STUDY_FILE = os.path.join(
    "data",
    "study_data.csv"
)

STUDENT_FILE = os.path.join(
    "data",
    "students.csv"
)


# ============================================
# PANDAS ANALYSIS
# ============================================

def pandas_analysis():

    print("\n" + "=" * 65)
    print("                 PANDAS DATA ANALYSIS")
    print("=" * 65)

    # ----------------------------------------
    # CHECK STUDY FILE
    # ----------------------------------------

    if not os.path.exists(STUDY_FILE):

        print("\n❌ study_data.csv not found!")
        print("Please add study data using Option 6.")
        return

    try:

        # ------------------------------------
        # LOAD DATA
        # ------------------------------------

        study_df = pd.read_csv(STUDY_FILE)

        if study_df.empty:

            print("\n❌ No study data available.")
            return

        # ------------------------------------
        # LOAD STUDENT INFORMATION
        # ------------------------------------

        if os.path.exists(STUDENT_FILE):

            student_df = pd.read_csv(
                STUDENT_FILE
            )

        else:

            student_df = pd.DataFrame()

        # ------------------------------------
        # ENTER STUDENT ID
        # ------------------------------------

        student_id = input(
            "\nEnter Student ID for analysis: "
        ).strip()

        # ------------------------------------
        # FILTER STUDENT DATA
        # ------------------------------------

        student_data = study_df[
            study_df["student_id"].astype(str)
            == student_id
        ].copy()

        if student_data.empty:

            print(
                "\n❌ No study data found "
                "for this Student ID."
            )

            return

        # ------------------------------------
        # GET STUDENT INFORMATION
        # ------------------------------------

        student_name = "Unknown"
        course = "Unknown"
        semester = "Unknown"

        if not student_df.empty:

            student_df["id"] = (
                student_df["id"].astype(str)
            )

            student_info = student_df[
                student_df["id"] == student_id
            ]

            if not student_info.empty:

                student_name = (
                    student_info.iloc[0]["name"]
                )

                course = (
                    student_info.iloc[0]["course"]
                )

                semester = (
                    student_info.iloc[0]["semester"]
                )

        # ------------------------------------
        # CONVERT NUMERICAL COLUMNS
        # ------------------------------------

        numerical_columns = [
            "study_hours",
            "sleep_hours",
            "phone_hours",
            "break_hours",
            "marks"
        ]

        for column in numerical_columns:

            student_data[column] = pd.to_numeric(
                student_data[column],
                errors="coerce"
            )

        # ====================================
        # STUDENT INFORMATION
        # ====================================

        print("\n" + "-" * 65)
        print("                 STUDENT INFORMATION")
        print("-" * 65)

        print("Student ID :", student_id)
        print("Name       :", student_name)
        print("Course     :", course)
        print("Semester   :", semester)
        print(
            "Records    :",
            len(student_data)
        )

        print("-" * 65)

        # ====================================
        # PANDAS ANALYSIS MENU
        # ====================================

        while True:

            print("\n" + "=" * 65)

            print(
                f"             PANDAS ANALYSIS - "
                f"{student_name}"
            )

            print("=" * 65)

            print("1. View Student Data")
            print("2. Statistical Summary")
            print("3. Average Study Hours")
            print("4. Average Sleep Hours")
            print("5. Average Phone Usage")
            print("6. Average Marks")
            print("7. Subject-wise Analysis")
            print("8. Mood Analysis")
            print("9. Performance Analysis")
            print("10. Complete Analysis")
            print("11. Change Student")
            print("12. Exit")

            print("=" * 65)

            choice = input(
                "Enter your choice: "
            ).strip()

            # =================================
            # 1. VIEW DATA
            # =================================

            if choice == "1":

                print("\n" + "-" * 65)
                print(
                    f"       STUDY DATA - "
                    f"{student_name}"
                )
                print("-" * 65)

                print(
                    student_data.to_string(
                        index=False
                    )
                )

            # =================================
            # 2. STATISTICAL SUMMARY
            # =================================

            elif choice == "2":

                print("\n" + "-" * 65)
                print("              STATISTICAL SUMMARY")
                print("-" * 65)

                print(
                    student_data[
                        numerical_columns
                    ].describe().round(2)
                )

            # =================================
            # 3. STUDY HOURS
            # =================================

            elif choice == "3":

                average = student_data[
                    "study_hours"
                ].mean()

                maximum = student_data[
                    "study_hours"
                ].max()

                minimum = student_data[
                    "study_hours"
                ].min()

                print("\n" + "-" * 65)
                print("              STUDY HOURS ANALYSIS")
                print("-" * 65)

                print(
                    "Average Study Hours :",
                    round(average, 2)
                )

                print(
                    "Maximum Study Hours :",
                    round(maximum, 2)
                )

                print(
                    "Minimum Study Hours :",
                    round(minimum, 2)
                )

            # =================================
            # 4. SLEEP HOURS
            # =================================

            elif choice == "4":

                average = student_data[
                    "sleep_hours"
                ].mean()

                maximum = student_data[
                    "sleep_hours"
                ].max()

                minimum = student_data[
                    "sleep_hours"
                ].min()

                print("\n" + "-" * 65)
                print("              SLEEP HOURS ANALYSIS")
                print("-" * 65)

                print(
                    "Average Sleep Hours :",
                    round(average, 2)
                )

                print(
                    "Maximum Sleep Hours :",
                    round(maximum, 2)
                )

                print(
                    "Minimum Sleep Hours :",
                    round(minimum, 2)
                )

            # =================================
            # 5. PHONE USAGE
            # =================================

            elif choice == "5":

                average = student_data[
                    "phone_hours"
                ].mean()

                maximum = student_data[
                    "phone_hours"
                ].max()

                minimum = student_data[
                    "phone_hours"
                ].min()

                print("\n" + "-" * 65)
                print("              PHONE USAGE ANALYSIS")
                print("-" * 65)

                print(
                    "Average Phone Usage :",
                    round(average, 2)
                )

                print(
                    "Maximum Phone Usage :",
                    round(maximum, 2)
                )

                print(
                    "Minimum Phone Usage :",
                    round(minimum, 2)
                )

            # =================================
            # 6. MARKS
            # =================================

            elif choice == "6":

                average = student_data[
                    "marks"
                ].mean()

                maximum = student_data[
                    "marks"
                ].max()

                minimum = student_data[
                    "marks"
                ].min()

                print("\n" + "-" * 65)
                print("                 MARKS ANALYSIS")
                print("-" * 65)

                print(
                    "Average Marks :",
                    round(average, 2)
                )

                print(
                    "Highest Marks :",
                    round(maximum, 2)
                )

                print(
                    "Lowest Marks  :",
                    round(minimum, 2)
                )

            # =================================
            # 7. SUBJECT ANALYSIS
            # =================================

            elif choice == "7":

                print("\n" + "-" * 65)
                print("             SUBJECT-WISE ANALYSIS")
                print("-" * 65)

                subject_analysis = (
                    student_data
                    .groupby("subject")["marks"]
                    .agg(
                        [
                            "count",
                            "mean",
                            "max",
                            "min"
                        ]
                    )
                    .round(2)
                )

                subject_analysis.columns = [
                    "Tests",
                    "Average Marks",
                    "Highest Marks",
                    "Lowest Marks"
                ]

                print(
                    subject_analysis
                )

            # =================================
            # 8. MOOD ANALYSIS
            # =================================

            elif choice == "8":

                print("\n" + "-" * 65)
                print("                  MOOD ANALYSIS")
                print("-" * 65)

                mood_count = (
                    student_data["mood"]
                    .value_counts()
                )

                print(
                    "\nMood Frequency:"
                )

                print(mood_count)

                print(
                    "\nAverage Marks by Mood:"
                )

                mood_marks = (
                    student_data
                    .groupby("mood")["marks"]
                    .mean()
                    .round(2)
                )

                print(mood_marks)

            # =================================
            # 9. PERFORMANCE ANALYSIS
            # =================================

            elif choice == "9":

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

                print("\n" + "-" * 65)
                print("             PERFORMANCE ANALYSIS")
                print("-" * 65)

                print(
                    "Average Study Hours :",
                    round(average_study, 2)
                )

                print(
                    "Average Sleep Hours :",
                    round(average_sleep, 2)
                )

                print(
                    "Average Phone Usage :",
                    round(average_phone, 2)
                )

                print(
                    "Average Marks       :",
                    round(average_marks, 2)
                )

                # Performance level

                if average_marks >= 80:

                    performance = "Excellent"

                elif average_marks >= 65:

                    performance = "Good"

                elif average_marks >= 50:

                    performance = "Average"

                else:

                    performance = "Needs Improvement"

                print(
                    "Performance Level   :",
                    performance
                )

            # =================================
            # 10. COMPLETE ANALYSIS
            # =================================

            elif choice == "10":

                print("\n" + "=" * 65)
                print(
                    f"       COMPLETE ANALYSIS - "
                    f"{student_name}"
                )
                print("=" * 65)

                print(
                    "\nSTUDENT INFORMATION"
                )

                print(
                    "Student ID :",
                    student_id
                )

                print(
                    "Name       :",
                    student_name
                )

                print(
                    "Course     :",
                    course
                )

                print(
                    "Semester   :",
                    semester
                )

                print(
                    "Records    :",
                    len(student_data)
                )

                # --------------------------------
                # AVERAGES
                # --------------------------------

                print(
                    "\nAVERAGES"
                )

                print(
                    "Study Hours :",
                    round(
                        student_data[
                            "study_hours"
                        ].mean(),
                        2
                    )
                )

                print(
                    "Sleep Hours :",
                    round(
                        student_data[
                            "sleep_hours"
                        ].mean(),
                        2
                    )
                )

                print(
                    "Phone Usage :",
                    round(
                        student_data[
                            "phone_hours"
                        ].mean(),
                        2
                    )
                )

                print(
                    "Break Hours :",
                    round(
                        student_data[
                            "break_hours"
                        ].mean(),
                        2
                    )
                )

                print(
                    "Average Marks:",
                    round(
                        student_data[
                            "marks"
                        ].mean(),
                        2
                    )
                )

                # --------------------------------
                # BEST / WORST
                # --------------------------------

                print(
                    "\nPERFORMANCE"
                )

                print(
                    "Highest Marks:",
                    student_data[
                        "marks"
                    ].max()
                )

                print(
                    "Lowest Marks :",
                    student_data[
                        "marks"
                    ].min()
                )

                # --------------------------------
                # SUBJECT ANALYSIS
                # --------------------------------

                print(
                    "\nSUBJECT-WISE AVERAGE"
                )

                subject_average = (
                    student_data
                    .groupby("subject")[
                        "marks"
                    ]
                    .mean()
                    .round(2)
                )

                print(subject_average)

                # --------------------------------
                # MOOD ANALYSIS
                # --------------------------------

                print(
                    "\nMOOD FREQUENCY"
                )

                print(
                    student_data[
                        "mood"
                    ].value_counts()
                )

                print("=" * 65)

            # =================================
            # 11. CHANGE STUDENT
            # =================================

            elif choice == "11":

                print(
                    "\nReturning to "
                    "Student Selection..."
                )

                return pandas_analysis()

            # =================================
            # 12. EXIT
            # =================================

            elif choice == "12":

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