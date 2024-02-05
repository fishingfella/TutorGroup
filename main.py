import time

Usernames = [["Daveyboi12","DaveIsCool12"],["MarkInit","Mark1990"]]

def stringValidation(value, text):
  while not value.split() or "," in value:
    print("Invalid.")
    value = str(input(f"\n{text}"))
  return value

def selectStudent():
  studentIds = []
  studentDetails = []
  try:
    f = open('students.csv', 'r')
  except:
    f = open('students.csv', 'x')
    f.close()
    f = open('students.csv', 'r')

  for line in f:
    words = line.split(",")
    print(f"{words[0]} {words[1]} | {words[4]}")
    studentIds.append(words[4])
    studentDetails.append(words)

  f.close()

  selectedStudent = str(input("Select a student (Enter ID): "))
  while selectedStudent not in studentIds:
    print("Student not found")
    selectedStudent = str(input("Select a student: "))

  return studentDetails[studentIds.index(selectedStudent)], studentIds.index(selectedStudent)

def storeText(lineNum): #Stores students who weren't selected to not lose data when adding to the text file
  above = []
  below = []
  f = open('students.csv', 'r')
  for currentLine, line in enumerate(f):
    if currentLine < lineNum: #only accepts text above the line number
      above.append(line)
    elif currentLine > lineNum: #only accepts text below the line number
      below.append(line)
  f.close()
  return above, below


auth = False
while auth == False:
  username = str(input("Username: "))
  password = str(input("Password: "))
  for i in range(len(Usernames)):
    if username == Usernames[i][0] and password == Usernames[i][1]:
      auth = True
      break
  else:
    print("Incorrect username or password.")
while auth == True:
  print("\nWelcome to the student database.")
      
      


  print("Select an option:\n1: Select a student\n2: Add a student\n3: Logout")
  option = -1
  while option <= 0 or option >= 4:
    try:
      option = int(input("Enter an option: "))
    except ValueError:
      print("Please enter a number.")
      option = -1

  if option == 1:
    #Allows you to choose a student
    details, line = selectStudent()
    #Menu for the selected student
    print("Select an option:\n1: Edit Details\n2: Print Details\n3: Remove Student")
    option = -1
    while option <= 0 or option >= 4:
      try:
        option = int(input("Enter an option: "))
      except ValueError:
        print("Please enter a number.")
        option = -1

    if option == 1:
      print("To make a change type the change if not then don't input anything and press enter")
      for count, subject in enumerate(details):
        print(subject, count)
        change = str(input())
        if change.split() != "".split():
          print(change)
          details[count] = change
      above, below = storeText(line)
      newLine = ""
      print(details)
      for x in details:
        if x != details[-1]:
          newLine += str(x) + ","
        else:
          newLine += str(x)

      f = open('students.csv', 'w')
      f.write("")#clears the text file
      f.close()
      f = open('students.csv', 'a')
      for x in above:
        f.write(f"{x}")#adds above the selcted student
      f.write(f"{newLine}")
      for x in below:
        f.write(f"{x}")#adds below the selected student
      f.close()

    elif option == 2:
      print(f"Name: {details[0]} {details[1]} \nGender: {details[2]} \nID: {details[4]} \nDate of Birth: {details[3]} \nTutor Group: {details[5]} \nHome Address: {details[6]} \nHome Phone Number: {details[7]}\n")
    elif option == 3:
      above, below = storeText(line)

      f = open('students.csv', 'w')
      f.write("")#clears the text file
      f.close()
      f = open('students.csv', 'a')
      for x in above:
        f.write(f"{x}")#adds above the selcted student
      f.write("")
      for x in below:
        f.write(f"{x}")#adds below the selected student
      f.close()
  elif option == 2:
    #Allows you to add a student
    details = []
    details.append(str(input("Enter first name: ")))
    details[0] = stringValidation(details[0], "Enter first name: ")
    details.append(str(input("Enter last name: ")))
    details[1] = stringValidation(details[1], "Enter last name: ")
    details.append(str(input("Enter gender: ")))
    details[2] = stringValidation(details[2], "Enter gender: ")
    details.append(str(input("Enter date of birth: ")))
    details[3] = stringValidation(details[3], "Enter date of birth: ")
    details.append(str(input("Enter student ID: ")))
    details[4] = stringValidation(details[4], "Enter student ID: ")
    details.append(str(input("Enter tutor group: ")))
    details[5] = stringValidation(details[5], "Enter tutor group: ")
    details.append(str(input("Enter home address: ")))
    details[6] = stringValidation(details[6], "Enter home address: ")
    details.append(str(input("Enter home phone number: ")))
    details[7] = stringValidation(details[7], "Enter home phone number: ")

    option = -1
    while option != 1 and option != 2:
      try:
        option = int(input("Would you like to add this student? (1: Yes | 2: No): "))
      except ValueError:
        print("Please enter a number.")
        option = -1

    if option == 1:
      f = open('students.csv', 'a')
      f.write(f"\n{details[0]}, {details[1]}, {details[2]}, {details[3]}, {details[4]}, {details[5]}, {details[6]}, {details[7]}")
      f.close()
    else:
      print("Student not added")
  elif option == 3:
    loggedIn = False
