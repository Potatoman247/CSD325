# Aidan Jacoby 9.2 5/4/25 - Aidan Jacoby 2.2 Debugging 6/7/25


# Sets the Student class
class Student:
  def __init__ (self, first_name, last_name):
    self.first_name = first_name
    self.last_name = last_name
    self.grade_points = 0
    self.credits = 0
    self.gpa = 0

# Calculates the GPA depending on letter grade
  def calculated_gpa(self, grade, credits):
    import pdb
    pdb.set_trace()
    self.credits = self.credits + int(credits)
    if grade == 'A':
      self.grade_points = self.grade_points + (int(credits)*4)
    if grade == 'B':
      self.grade_points = self.grade_points + (int(credits)*3)
    if grade == 'C':
      self.grade_points = self.grade_points + (int(credits)*2)
    if grade == 'D':
      self.grade_points = self.grade_points + (int(credits)*1)
    else:
      self.grade_points = self.grade_points + (int(credits)*0)
    self.gpa = self.grade_points/self.credits

# Print method for GPA
  
  def getGPA(self):
    print(f'the GPA for {self.first_name} is {round(self.gpa, 1)} ')

# Sets the variables for student1
student_first_n = input('Please enter the student first name: ')
student_last_n = input('Please enter the student last name: ')
student_1 = Student(student_first_n, student_last_n)

# While loop for adding grades

quit = '1'
while quit == '1':
  grade = input('Please enter student grade: ')
  credits = input('Please enter credits: ')
  try:
    student_1.calculated_gpa(grade, credits)
  except: print("Invalid Input, Please try Again.")
  quit = input('Enter 1 to continue or 2 to quit: ')

student_1.getGPA()