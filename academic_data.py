def add_academic_record(subjects, marks, attendance):
    print("\nAdd Academic Record")

    while True:
        subject = input("Enter subject name: ")

        if subject != "":
            break

        print("Subject name cannot be empty.")

    while True:
        try:
            mark = int(input("Enter marks: "))

            if mark >= 0 and mark <= 100:
                break

            print("Marks should be between 0 and 100.")

        except ValueError:
            print("Please enter a number.")

    while True:
        try:
            att = int(input("Enter attendance percentage: "))

            if att >= 0 and att <= 100:
                break

            print("Attendance should be between 0 and 100.")

        except ValueError:
            print("Please enter a number.")

    subjects.append(subject)
    marks.append(mark)
    attendance.append(att)

    print("Academic record added successfully.")


def display_academic_records(subjects, marks, attendance):
    print("\nAcademic Records")

    if len(subjects) == 0:
        print("No academic records available.")
        return

    for i in range(len(subjects)):
        print("\nSubject:", subjects[i])
        print("Marks:", marks[i])
        print("Attendance:", attendance[i], "%")


def get_subject_count(subjects):
    return len(subjects)

subjects = []
marks = []
attendance = []

add_academic_record(subjects, marks, attendance)

display_academic_records(subjects, marks, attendance)

print("\nNumber of subjects:", get_subject_count(subjects))