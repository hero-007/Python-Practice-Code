import Student as st

student_record = []

def add_Student():
    nm = input("Enter Student's name : ")
    ag = int(input("Enter Student's age : "))
    sec = input("Enter student's section : ")
    marks = float(input("Enter student's percentage : "))
    obj = st.Student(nm,ag,sec,marks)
    student_record.append(obj)
    print("Student record is added succesfully in the database")
    return

def del_Student():
    n = int(input("Enter the Id of student that you want to delete from the record : "))
    print("Student named "+student_record[n].getName()+" has been deleted from the record ")
    del student_record[n]
    return

def display_Students():
    for i in student_record:
        print("Student Id : "+str(i.getId()))
        print("Student Name : "+i.getName())
        print("Student Age : "+str(i.getAge()))
        print("Student Section : "+i.getSec())
        print("Student Percent : "+str(i.getPercent()))
        print("\n\n")
    return

def modify_Student():
    n = int(input("Enter the Id of student whose data you want to modify : "))
    ob = student_record[n]
    print("Choose one field that you want to modify : \n1: Name\n2: Age\n3: Section\n4: Percentage\n\nChoice : ")
    chk = int(input())
    if chk==1:
        nm = input("Enter the new name : ")
        ob.setName(nm)
        print("Name has been changed successfuly")
        

    elif chk==2:
        ag = int(input("Enter the new age : "))
        ob.setAge(ag)
        print("Age of Student has been changed successfuly")
        

    elif chk==3:
        sec = input("Enter the new section : ")
        ob.setSec(sec)
        print("Section of the Student has been changed successfuly ")
        

    elif chk==4:
        mark = float(input("Enter the new percentage of the student : "))
        ob.setPercent(mark)
        print("Percentage of the Student has been upadated successfuly ")
        

    else : print("You entered the wrong choice")
    return

def total_Students():
    print("Total number of students in your data base :",st.Student.number_of_students)
    return
