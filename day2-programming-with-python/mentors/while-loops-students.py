blank = False

while not blank:
    student = input("Please enter the name of a student: ")
    if student == '':
        blank = True
    print(student)