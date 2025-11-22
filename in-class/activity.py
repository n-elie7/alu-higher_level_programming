student_grades = {
    "Elie": 98,
    # "Denzel": 99,
    # "Suwafa": 97,
    # "Collins": 100
}

# print(f"Denzel marks: {student_grades["Denzel"]}")

student_grades["Irakoze"] = 100

while True:
    search_name = input("Enter name of student: ")
    # first make copy of dictionary to avoid runtime error caused by
    # dictionary that has changed size during iteration which led
    # for an iterator to be invalid
    for name, grade in list(student_grades.items()):
        if name == search_name:
            print(f"{name}: {grade}")
            break
    else:
        print("Name is not available")
        answer = input("Do you want to add this new student? (y/n): ")
        if answer == "y":
            search_name = input("Enter name of student: ")
            grade = input("Enter his/her grade: ")
            student_grades[search_name] = grade
            print(f"{name}: {grade}")
        else:
            break
    want_to_exit = input("Do you want to exit?(y/n): ")

    if want_to_exit == "y":
        break
    else:
        continue



student_grades = {
    "Elie": 98,
    # "Denzel": 99,
    # "Suwafa": 97,
    # "Collins": 100
}

while True:
    search_name = input("Enter name of student: ")
    for name, grade in list(student_grades.items()):
        if name.lower() == search_name.lower():
            print(f"{name}: {grade}")
            break
    else:
        response = input("Name not found. Add this new student? (y/n): ")
        if response.lower() != 'n':
            new_student_name = input("Enter his/her name: ")
            while True:
                try:
                    new_grade = int(input("Enter their grade: "))
                    break
                except ValueError:
                    print("Invalid input. Please enter a number.")
            student_grades[new_student_name] = new_grade
            print(f"{new_student_name}: {new_grade}")
        else:
            continue

    want_to_exit = input("Do you want to exit? (y/n): ")
    if want_to_exit.lower() == 'y':
        break
