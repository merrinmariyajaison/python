def get_student_details():
    students = {}
    n = int(input("Enter the number of students: "))

    for i in range(n):
        print(f"\nEnter details for student {i+1}:")
        name = input("Name: ")
        roll_no = input("Roll number: ")
        total_mark = int(input("Total marks: "))
        students[roll_no] = {"name": name, "total_mark": total_mark}

    return students

def find_top_student(students):
    highest_marks = -1
    top_student = None

    for roll_no, details in students.items():
        if details["total_mark"] > highest_marks:
            highest_marks = details["total_mark"]
            top_student = {"roll_no": roll_no, "name": details["name"], "total_mark": details["total_mark"]}

    return top_student

students = get_student_details()
top_student = find_top_student(students)

if top_student:
    print("\nDetails of the student with the highest total marks:")
    print(f"Name: {top_student['name']}")
    print(f"Roll Number: {top_student['roll_no']}")
    print(f"Total Marks: {top_student['total_mark']}")
else:
    print("No students found.")
