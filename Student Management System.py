student_info = []
result_info = []

while True:
    print("-----Welcome to the Student Management System-----")
    print("1. Add Students Name & Results")
    print("2. View Students Lists")
    print("3. View Students Details")
    print("4. Delete Student")
    print("5. Exit")

    choice = input("Enter your choice: ")

    # Add Student
    if choice == "1":
        student = input("Student Name: ")
        result = input("Student Result: ")

        if student in student_info:
            print("Student is Already Added!")
        else:
            student_info.append(student)
            result_info.append(result)
            print("Student Added Successfully!")

    # View Student List
    elif choice == "2":
        if student_info:
            for i in range(len(student_info)):
                print(f"{i+1} | {student_info[i]}")
        else:
            print("No Student Found")

    # View Student Details
    elif choice == "3":
        if student_info:
            for i in range(len(student_info)):
                print(f"{i+1} | Name: {student_info[i]} | Result: {result_info[i]}")
        else:
            print("No Student Found")

    # Delete Student
    elif choice == "4":
        student = input("Enter Student Name to Delete: ")

        if student in student_info:
            index = student_info.index(student)

            student_info.pop(index)
            result_info.pop(index)

            print("Student Deleted Successfully!")
        else:
            print("No Student Found")

    # Exit
    elif choice == "5":
        print("Program Closed")
        break

    else:
        print("Invalid Choice")