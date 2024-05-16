num_students=int(input("Enter the number of students: "))
i=1
while i<=num_students:
    total_grade= 0
    num_subjects =int(input("Enter the number of subjects for student (1): "))
    for j in range(1, num_subjects + 1):
        grade=float(input("Enter subject (1) grade for student (1): "))
        total_grade += grade

    average_grade =total_grade / num_subjects
    print("Average grade for student (1): (average_grade:.2f)")
    i+=1
