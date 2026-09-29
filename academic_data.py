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

            if mark>=0 and mark<=100:
                break

            print("Marks should be between 0 and 100.")

        except ValueError:
            print("Please enter a number.")

    while True:
        try:
            att = int(input("Enter attendance percentage: "))

            if att>=0 and att<=100:
                break

            print("Attendance should be between 0 and 100.")

        except ValueError:
            print("Please enter a number.")

    subjects.append(subject)