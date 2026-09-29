import os

from academic_data import add_academic_record
from academic_data import display_academic_records
from academic_data import get_subject_count
from marks_analyser import display_marks_analysis


def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")


def show_header():
    print("\n" + "=" * 55)
    print("             STUDENT ACADEMIC ASSISTANT")
    print("             Academic Management System")
    print("=" * 55)


def show_menu():
    print("\nMain Menu")
    print("-" * 55)
    print("1. Add Academic Records")
    print("2. View Academic Records")
    print("3. View Marks Analysis")
    print("4. Number of Subjects")
    print("5. Exit")
    print("-" * 55)


def press_enter():
    input("\nPress Enter to continue...")


def add_records(subjects, marks, attendance):
    clear_screen()
    show_header()

    print("\nAdd Academic Record")
    print("-" * 55)
    print("Enter the details of your subjects.")
    print("You can add more than one subject.\n")

    while True:
        add_academic_record(subjects, marks, attendance)

        choice = input(
            "\nDo you want to add another subject? (Y/N): "
        ).strip().lower()

        if choice == "y":
            print("\nLet's add another subject.\n")

        elif choice == "n":
            print("\nAll academic records have been saved.")
            break

        else:
            print("Please enter Y or N.")


def view_records(subjects, marks, attendance):
    clear_screen()
    show_header()

    display_academic_records(subjects, marks, attendance)
    press_enter()


def view_analysis(subjects, marks):
    clear_screen()
    show_header()

    display_marks_analysis(subjects, marks)
    press_enter()


def show_subject_count(subjects):
    clear_screen()
    show_header()

    count = get_subject_count(subjects)

    print("\nSubject Summary")
    print("-" * 55)
    print("Number of subjects:", count)

    if count == 0:
        print("No subjects have been added yet.")
    elif count == 1:
        print("You currently have 1 subject.")
    else:
        print("You currently have", count, "subjects.")

    press_enter()


def main():
    subjects = []
    marks = []
    attendance = []

    while True:
        clear_screen()
        show_header()
        show_menu()

        choice = input("\nEnter your choice (1-5): ").strip()

        if choice == "1":
            add_records(subjects, marks, attendance)

        elif choice == "2":
            view_records(subjects, marks, attendance)

        elif choice == "3":
            view_analysis(subjects, marks)

        elif choice == "4":
            show_subject_count(subjects)

        elif choice == "5":
            clear_screen()
            print("\nThank you for using Student Academic Assistant!")
            print("Goodbye!")
            break

        else:
            print("\nInvalid choice.")
            print("Please select a number between 1 and 5.")
            press_enter()


if __name__ == "__main__":
    main()