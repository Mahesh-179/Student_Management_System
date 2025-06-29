marksheets={}
add_students={}
# declaring function to add students
def add_students_name(name,grade,age,address,phone_no,sub1,sub2,sub3,sub4,sub5,sub6):
# Using Nested Dictionary to store value for different students
    add_students[name] = {
        "grade": grade,
        "age": age,
        "address": address,
        "phone_no": phone_no,
        "Physics": sub1,
        "Chemistry": sub2,
        "Mathematics": sub3,
        "Computer-Science": sub4,
        "Nepali": sub5,
        "English": sub6
    }

    print(f"You Have Successfully Added {name} with a details")

def marksheet_generator():
    name_student=input("Enter the Name of Student: ")
    if name_student in add_students:
        student=add_students[name_student]
        total=0
        filename=f" Marksheet of {name_student} is generated Successfully"
        with open(filename,"w") as file:
            with open(filename, "w") as file:
                file.write("==============================================================\n")
                file.write("             DIVYA ENGLISH BOARDING SCHOOL                    \n")
                file.write("         Keurani-03, Aambaschowk, Nawalparasi                 \n")
                file.write("         Contact Number: +977-9828890064                      \n")
                file.write("==============================================================\n")
                file.write("                        STUDENT MARKSHEET                \n")
                file.write("==============================================================\n")
                file.write(f"  Student Name    : {name_student}\n")
                file.write(f"  Student Age     : {student['age']}\n")
                file.write(f"  Student Address : {student['address']}\n")
                file.write(f"  Phone Number    : {student['phone_no']}\n")
                file.write("--------------------------------------------------------------\n")
                file.write("  Subjects                | Marks\n")
                file.write("--------------------------------------------------------------\n")

                total = 0
                for subject in ["Physics", "Chemistry", "Mathematics", "Computer-Science", "Nepali", "English"]:
                    marks = student[subject]
                    total += marks
                    file.write(f"  {subject:<23} : {marks}\n")

                percentage = total / 6
                file.write("--------------------------------------------------------------\n")
                file.write(f"  Total Marks           : {total}\n")
                file.write(f"  Percentage            : {round(percentage, 2)}%\n")

                # Grade Calculation
                if percentage >= 90:
                    grade = "A+"
                elif percentage >= 80:
                    grade = "A"
                elif percentage >= 70:
                    grade = "B+"
                elif percentage >= 60:
                    grade = "B"
                elif percentage >= 50:
                    grade = "C"
                else:
                    grade = "Fail"

                file.write(f"  Grade                 : {grade}\n")
                file.write("==============================================================\n")
                file.write("  Teacher's Signature   : ___________________________\n")
                file.write("  Principal's Signature : ___________________________\n")
                file.write("==============================================================\n")


# declaring students to update the existing
def updating_students_name(name,grade,age,address,phone_no,sub1,sub2,sub3,sub4,sub5,sub6):
    if name in add_students:
        add_students[name] = {
            "grade": grade,
            "age": age,
            "address": address,
            "phone_no": phone_no,
            "Physics": sub1,
            "Chemistry": sub2,
            "Mathematics": sub3,
            "Computer-Science": sub4,
            "Nepali": sub5,
            "English": sub6,
        }
        print(f"You Have Successfully Updated {name} with a new details")
    else:
        print(f"Sorry, {name} doesn't exist")

# Viewing the stored records in dictionary
def view_students_name():
    if add_students:
        print("======== STUDENT DETAILS =======")
        for key, details in add_students.items():
            print(f"Student Name: {key}")
            print(f"Grade: {details['grade']}")
            print(f"Age: {details['age']}")
            print(f"Address: {details['address']}")
            print(f"Phone No: {details['phone_no']}")

# Delete the existing students
def delete_students_name(name):
    if name in add_students:
        del add_students[name]
        print(f"You Have Successfully Deleted {name}")
    else:
        print(f"Sorry, {name} doesn't exist")
def main():
    while True:
        print("==================== STUDENT MANAGEMENT SYSTEM - BY MAHESH RAJ LAMSAL=======================")
        print(" 1.Add Student Details\n 2.Update Student Details\n 3.View Student Details\n 4.Delete Student Details\n 5.Generate Marksheet\n 6.Exit")
        user_han = int(input("Enter your choice: "))
        if user_han == 1:
            name = input("Enter your name: ")
            grade = int(input("Enter your grade: "))
            age = int(input("Enter your age: "))
            address = input("Enter your address: ")
            phone_no = int(input("Enter your phone number: "))
            sub1=int(input("Enter your Marks for Physics: "))
            sub2=int(input("Enter your Marks for Chemistry: "))
            sub3=int(input("Enter your Marks for Mathematics: "))
            sub4=int(input("Enter your Marks for Computer-Science: "))
            sub5=int(input("Enter your Marks for Nepali: "))
            sub6=int(input("Enter your Marks for English: "))
            add_students_name(name, grade,age,address,phone_no,sub1,sub2,sub3,sub4,sub5,sub6)
        elif user_han == 2:
            name = input("Enter your name: ")
            grade = int(input("Enter your grade: "))
            age = int(input("Enter your age: "))
            address = input("Enter your address: ")
            phone_no = int(input("Enter your phone number: "))
            sub1 = int(input("Enter your Marks for Physics: "))
            sub2 = int(input("Enter your Marks for Chemistry: "))
            sub3 = int(input("Enter your Marks for Mathematics: "))
            sub4 = int(input("Enter your Marks for Computer-Science: "))
            sub5 = int(input("Enter your Marks for Nepali: "))
            sub6 = int(input("Enter your Marks for English: "))
            updating_students_name(name,grade,age,address,phone_no,sub1,sub2,sub3,sub4,sub5,sub6)
        elif user_han == 3:
            view_students_name()
        elif user_han == 4:
            name=input("Enter your name: ")
            delete_students_name(name)
        elif user_han == 5:
           marksheet_generator()
        elif user_han == 6:
            print("Program is Ending...........")
            break
        else:
            print("Sorry, something went wrong")
main()