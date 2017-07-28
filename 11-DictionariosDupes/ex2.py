def main():

    students = []
    new_student = " "
    new_student = input("Student's name (or press ENTER to finish)")
    # Use a space to allow for the while check below
    grades=int(input("enter the grades"))

    # Get student names
    if new_student != "":
       students.append(new_student)

    # Get student grades
    grades = [0]*len(students)
    for idx, student in enumerate(students):
        new_grade = float(input("Grade for " + student + ": "))
        grades[idx] = new_grade

    # Print class roster
    print("\nClass roster:")
    for idx, student in enumerate(students):
        print(student + " (" + str(grades[idx]) + ")")

    avg = sum(grades) / len(grades)
    print("\nAverage grade: " + str(avg))

if __name__ == '__main__':
    main()
# /////////////////////////////////////////////
students={}

namestudent=input("enter the name ")
# for x in namestudent:
#     =input("enter the grade for ",x)
for i in students:
  