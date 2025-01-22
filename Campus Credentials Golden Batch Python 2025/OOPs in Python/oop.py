# class NewClass:
#     def __init__(self):
#         self.a=10
#         print("Hi I'm Constructor",self.a)

#     def show(self):
#         print("Class level hi", self.a)

# obj = NewClass()
# print(obj)
# obj.show()
# obj2 = NewClass()

"""Parameterized constructor"""

# class Hod:
#     def __init__(self, name, age, rollno):
#         self.a=10
#         self.name = name
#         self.age = age
#         self.rollno = rollno
        
#     def show(self):
#         print("Name", self.name)
#         print("Name", self.age)
#         print("Name", self.rollno)

# obj = Hod("Arjun", 69, 72)
# obj.show()

"""Normal Constructor"""

# class Hod:
#     def __init__(self):
#         self.name = "Shreyas"
#         self.age = 89
#         self.rollno = 79
        
#     def show(self):
#         print("Name", self.name)
#         print("Name", self.age)
#         print("Name", self.rollno)

# obj = Hod()
# obj.show()


"""CRUD operation"""
class CRUD:
    def __init__(self):
        print("Student MGMT")
        self.studentID = []
        self.studentName = []
        self.studentRollNo = []
        self.studenCity = []
    
    def addStudent(self):
        self.studentID.append(input("ID: "))
        self.studentName.append(input("Name: "))
        self.studentRollNo.append(input("Roll no: "))
        self.studenCity.append(input("City: "))
            
    def deleteStudent(self, i):
        self.studentID.remove(i)
        self.studentName.remove(i)
        self.studentRollNo.remove(i)
        self.studenCity.remove(i)
    
    def display(self):
        for i in range(len(self.studentID)):
            print(self.studentID)
            print(self.studentName)
            print(self.studentRollNo)
            print(self.studenCity)

    def update(self, i):
        self.studentID.insert(i, input("ID: "))
        self.studentName.insert(input("Name: "))
        self.studentRollNo.insert(input("Roll no: "))
        self.studenCity.insert((input("City: ")))


exit = False
obj = CRUD()

while(not exit):
    

    sts = int(input("""Enter your choice:
        
            1. Add Student
            2. Delete Student
            3. Display
            4. Exit\n"""))

    if(sts == 1):
        obj.addStudent()
    elif(sts == 2):
        choice = int(input("Which student ID?"))
        obj.deleteStudent(choice)
    elif(sts == 3):
        obj.display()
    elif(sts == 4):
        exit = True
        break
    else:
        print("Enter 1 or 2 or 3 or 4")