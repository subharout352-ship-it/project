students = {}

while True:
    print("\n1. Add Student")
    print("2. View Students")
    print("3. Exit")

    choice = input("Enter Choice: ")

    if choice == "1":
        roll = input("Enter Roll Number: ")
        name = input("Enter Name: ")
        students[roll] = name
        print("Student Added Successfully")

    elif choice == "2":
        print("\nStudent Records")
        for roll, name in students.items():
            print("Roll:", roll, "Name:", name)

    elif choice == "3":
        print("Program Closed")
        break

    else:
        print("Invalid Choice")