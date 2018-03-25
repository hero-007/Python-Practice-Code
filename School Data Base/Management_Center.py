
import Student_operation as so


ch = 'yes'
while ch=='yes':
    print("\n\n************ OPERATION TO PERFORM ON STUDENT DATABASE **************")
    print("1: ADD A STUDENT TO THE DATA BASE\n2: DELETE A STUDENT FROM THE DATA BASE\n3: DISPLAY THE ENTIRE DATA BASE\n4: MODIFY THE DATA OF A STUDENT IN THE DATA BASE\n5: PRINT TOTAL NUMBER OF STUDENT IN THE DATABASE\n\n")
    choice = int(input("ENTER YOUR CHOICE : "))
    print("\n")
    if choice == 1:
        so.add_Student()
        

    elif choice == 2:
        so.del_Student()
        

    elif choice == 3:
        so.display_Students()
        

    elif choice == 4:
        so.modify_Student()

    elif choice == 5:
        so.total_Students()
        

    else : print("YOU CHOOSE WRONG OPTION FROM THE MENU ABOVE")

    ch = input("\n\nEnter 'yes' to continue operations with the database else enter 'no' : ")
print("\n\n************* THANK YOU **************")
input("\n************* PRESS ANY KEY TO EXIT *************")
