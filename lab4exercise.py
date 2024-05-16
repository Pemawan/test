'''name=input("Enter student's name: ")
age=input("Enter student's age: ")
grade=input("Enter student's grade: ")
print("Student inforation added successfully!")
dict_name={}
studen_list=[]

dict_name[name]={'age ':age,'grade':grade}
search=input("Enter the name of the student to remove or simple enter to skip:")
if search in dict_name:
    print'''

# Initialize empty lists and dictionary
students_list = []
students_dict = {}

def add_student():
    name = input("Enter student's name: ")
    age = input("Enter student's age: ")
    grade = input("Enter student's grade: ")
    
    # Add student information to list
    students_list.append(name)
    
    # Add student information to dictionary
    students_dict[name] = {'age': age, 'grade': grade}
    print("Student information added successfully!")

def search_student(name):
    if name in students_dict:
        print(f"Name: {name}, Age: {students_dict[name]['age']}, Grade: {students_dict[name]['grade']}")
    else:
        print("Student not found!")

# Prompt user to input student details and add to list and dictionary
add_student()

# Ask user to input student name to search
search_name = input("Enter the name of the student to search: ")

# Search for the student and print their details if found
search_student(search_name)