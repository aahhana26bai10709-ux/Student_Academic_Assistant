def create_profile():
    name = input("Enter name: ")

    while name == "":
        print("Name cannot be blank.") # user messed up
        name = input("Enter name: ")

    reg_no = input("Enter registration number: ")

    while reg_no == "":
        print("Registration number cannot be blank.")
        reg_no = input("Enter registration number: ")

    while True:
        try:
            semester = int(input("Enter semester: "))

            if semester >= 1:
                break
            else:
                print("Enter a semester number greater than 0.")

        except ValueError:
            print("Please enter a number.")


    return name, reg_no, semester

def display_profile(name, reg_no, semester):
    print("\nSTUDENT PROFILE")
    print("---------------------")
    print("Name:", name)
    print("Registration No:", reg_no)
    print("Semester:", semester)
    print("---------------------")

name, reg_no, semester = create_profile()
display_profile(name, reg_no, semester)
