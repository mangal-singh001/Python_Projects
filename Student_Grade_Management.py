student_grade = { }

def add_Student(name,grade):
    student_grade[name] = grade
    print(f"Added {name} with a {grade}")
    
    
def update_student(name,grade):
    if name in student_grade:
        student_grade[name] = grade
        print(f"{name} with marks are updated {grade}")
    else:
        print(f"{name} is not found")
        
def delete_student(name):
    if name in student_grade:
        del student_grade[name]
        print(f"{name} has been successfully deleted")
        
    else:
        print(f"{name} is not found")
        
def display_all_items():
    if student_grade:
        for name,grade in student_grade.items():
            print(f"{name} : {grade}")
            
    else:
        print("No Student found/added")
        
def main():
    while True:
        print("Student Grades Management System")
        choose = int(input("1. Add Student\n2. Update Student\n3. Delete Student\n4. View Student\n5. Exit\nEnter your choice = "))
            
        if choose == 1:
            student = input("Enter the name of the student : ")
            marks = int(input(f"Enter marks of the {student} :  "))
            add_Student(student,marks)
             
        elif choose == 2:
            student_name = input("Enter the student name whom you want to update the marks : ")
            student_marks = int(input(f"Enter the updated marks of the {student_name} : "))
            update_student(student_name,student_marks)
            
        elif choose == 3:
            stu = input("Enter the name of the student you want to delete : ")
            delete_student(stu)
            
        elif choose == 4:
            display_all_items()

        elif choose == 5:
            print("Closing the Program")
            break
        
        else:
            print("Invalid Choice")
        
        
if __name__ == "__main__":
    main()