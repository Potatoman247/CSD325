import json

with open('student.json', 'r') as file:
    students = json.load(file)
    
def printClassList():    
    for student in students:
        print(student["F_Name"], ',', student["L_Name"], ' : ID = ', student['Student_ID'], ', Email =', student['Email'])

def main():
    print("This Is The Original Class List\n")
    
    printClassList()
    newStudent = {"F_Name": "Aidan", "L_Name": "Jacoby","Student_ID": 24714,"Email": "aidanjacoby247@gmail.com"}
    students.append(newStudent)
    print("This is The Updated Class List")
    printClassList()
    
    with open('student.json', 'w') as file:
        json.dump(students, file, indent = 4)
main()