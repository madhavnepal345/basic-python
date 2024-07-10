def total_marks(stud):
    return stud["english_mark"] + stud["math_mark"]

student_list = []
for i in range(5):
    stud_name = input("Enter student name: ")
    english_mark = int(input("Enter English mark: "))    
    math_mark = int(input("Enter Math mark: "))
    student = {
        "name": stud_name,
        "english_mark": english_mark,
        "math_mark": math_mark
    }
    student["total"] = total_marks(student)
    student_list.append(student)

print(student_list)