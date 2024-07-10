#%%


#%%
marksheet={
    'student_name':'manoj',
    'Mark in english':89,
    'marks in math': 45,
    'total marks': 134
    }
marksheet_1={
    'student_name':'saroj',
    'Mark in english':78,
    'marks in math': 89,
    'total marks': 167
    }
list_1=[marksheet, marksheet_1]
print(f"the mark sheet of the student is {list_1}")



# %%


def calculate_total_marks(stud):
    return stud["english_mark"] + stud["math_mark"]

student_list = []


for i in range(5):
    stud_name = input("Enter student name: ")
    
    english_mark = int(input("Enter English mark: "))
    
    # Get Math mark
    math_mark = int(input("Enter Math mark: "))
    
    # Create a dictionary for the student
    student = {
        "name": stud_name,
        "english_mark": english_mark,
        "math_mark": math_mark
    }
    
    # Calculate total marks and add it to the dictionary
    student["total"] = calculate_total_marks(student)
    
    # Add the student dictionary to the list
    student_list.append(student)

# Print the list of students
print(student_list)
# %%
def find_odd_even(n):
    # Use bitwise AND operator to check if the number is even
    if n & 1:
        return "Odd"
    else:
        return "Even"

# Test the function
num = int(input("Enter a number: "))
print(find_odd_even(num))


# %%
#wap to print the higest of a given number




# %%
