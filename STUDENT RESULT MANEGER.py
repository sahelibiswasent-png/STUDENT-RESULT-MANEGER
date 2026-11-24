student ={}
while True:
    print("\n------------STUDENT MANEGER APP------------")
    print("1. Add Student")
    print("2. View Students")
    print("3. Update Student")
    print("4. Delete Student")
    print("5. Check Results")
    print("6. Exit")

    choice = input("Enter your choice (1-6): ")

    # add student
    if choice=="1":
        name=input("Enter the student name: ")
        marks=int(input("Enter the student marks: "))
        #dic update 
        student[name]=marks
        print(f"Student {name} added successfully!.")
        

 
    #view student
    elif choice=="2":
        if not student:
            print("No students found.")
        else:
            print("\nStudent List:")
            for name, marks in student.items():
                print(name,":",marks)
    elif choice=="3":
        name=input("Enter the update student name:")
        if name in student:
            marks=int(input("Enter the new marks:"))
            student[name]=marks
            print("student updated sucessfully!.")
        else:
            print("student not found.")
    elif choice=="4":
        name=input("Enter the student name to delete:")
        if name in student:
            marks=int(input("Enter the deleted student marks:"))
            student[name]=marks
            print("student deleted sucessfully!.")
        else:
            print("student not found.")
    elif choice==5:
        name=input("Enter the student name to check results:")
        if name in student:
            marks=student[name]
            if marks>=90:
                print("student has scored marks and got grade A.")
            elif marks>=80:
                print("student has scored marks and got grade B.")
            elif marks>=70:
                print("student has scored marks and got grade C.")
            elif marks>=60:
                print("student has scored marks and got grade D.")
            else:
                print("student has scored marks and got grade F.")
        else:
            print("student not found.")    

    elif choice==6: 
        print("Exiting the program.")
        break
    else:
        print("In-valid input. please choose the valid number between 1-6.")
                             

     



                                 
                   
                   
                   
                   
                   
                   
                   
                   
                   
                   
                   
                   
                   
                   
                   
                   
                   
                   
                   
                   
                   
                   
                   
                   
                

