def calculate_total(marks):
    total = 0

    for mark in marks:
        total = total + mark

    return total


def calculate_average(marks):
    if len(marks) == 0:
        return 0

    total = calculate_total(marks)
    average = total / len(marks)

    return average


def find_highest(marks):
    if len(marks) == 0:
        return 0

    highest = marks[0]

    for mark in marks:
        if mark > highest:
            highest = mark

    return highest


def find_lowest(marks):
    if len(marks) == 0:
        return 0

    lowest = marks[0]

    for mark in marks:
        if mark < lowest:
            lowest = mark

    return lowest


def find_highest_subject(subjects, marks):
    if len(subjects) == 0:
        return "None"

    highest_index = 0

    for i in range(len(marks)):
        if marks[i] > marks[highest_index]:
            highest_index = i

    return subjects[highest_index]


def find_lowest_subject(subjects, marks):
    if len(subjects) == 0:
        return "None"

    lowest_index = 0

    for i in range(len(marks)):
        if marks[i] < marks[lowest_index]:
            lowest_index = i

    return subjects[lowest_index]


def display_marks_analysis(subjects, marks):

    if len(marks) == 0:
        print("\nNo marks available.")
        return

    total = calculate_total(marks)
    average = calculate_average(marks)
    highest = find_highest(marks)
    lowest = find_lowest(marks)

    highest_subject = find_highest_subject(subjects, marks)
    lowest_subject = find_lowest_subject(subjects, marks)

    print("\n========== MARKS ANALYSIS ==========")
    print("Total Marks     :", total)
    print("Average Marks   :", round(average, 2))
    print("Highest Marks   :", highest)
    print("Highest Subject :", highest_subject)
    print("Lowest Marks    :", lowest)
    print("Lowest Subject  :", lowest_subject)
    print("====================================")
