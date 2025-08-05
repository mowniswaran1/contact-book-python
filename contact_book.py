Student = []
marks = []

def add_students():
    students = input("enter student name:").lower
    mark = int(input("enter marks : "))
    Student.append(students)
    marks.append(mark)
    
    
def show():
    a = len(Student)
    for i in range(a):
        mark = marks[i]
        print(Student[i],marks[i],grade(mark),sep=" - ")
        print()
        
def avg():
    b = len(marks)
    total = sum(marks)
    print(total/b)      
    
def update_marks():
    stu = input("the the name of the sudent=").lower
    mar = int(input("enter the updated mark="))
    for i in range(len(Student)):
        if Student[i]==stu:
            marks[i]= mar
            break

def delete():
    studen = input("enter the student to delete =")
    for i in range(len(Student)):
        if Student[i]==studen:
            marks.remove(marks[i])
            Student.remove(Student[i])
            break
def grade(mark):
    if mark >= 90:
        return "A+"
    elif mark >= 80:
        return "A"
    elif mark >= 70:
        return "B"
    elif mark >= 60:
        return "C"
    elif mark >= 50:
        return "D"
    else:
        return "F"

    
    
while True:
    
    print("1. Add student\n2. View all students\n3. Show average marks\n4. update marks\n5.delete student\n6.exit")
    choice = int(input("enter your choics in number = "))
   
    if choice == 1:
        add_students()
    elif choice == 2:
        show()
    elif choice == 3:
        avg()
    elif choice==4:
        update_marks()
    elif choice == 5:
        delete()
    elif choice == 6:
        break
    
    

    
        
    
    