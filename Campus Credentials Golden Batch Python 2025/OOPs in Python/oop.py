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
# class CRUD:
#     def __init__(self):
#         print("Student MGMT")
#         self.studentID = []
#         self.studentName = []
#         self.studentRollNo = []
#         self.studenCity = []
    
#     def addStudent(self):
#         self.studentID.append(input("ID: "))
#         self.studentName.append(input("Name: "))
#         self.studentRollNo.append(input("Roll no: "))
#         self.studenCity.append(input("City: "))
            
#     def deleteStudent(self, i):
#         self.studentID.remove(i)
#         self.studentName.remove(i)
#         self.studentRollNo.remove(i)
#         self.studenCity.remove(i)
    
#     def display(self):
#         for i in range(len(self.studentID)):
#             print(self.studentID)
#             print(self.studentName)
#             print(self.studentRollNo)
#             print(self.studenCity)

#     def update(self, i):
#         self.studentID.insert(i, input("ID: "))
#         self.studentName.insert(input("Name: "))
#         self.studentRollNo.insert(input("Roll no: "))
#         self.studenCity.insert((input("City: ")))


# exit = False
# obj = CRUD()

# while(not exit):
    

#     sts = int(input("""Enter your choice:
        
#             1. Add Student
#             2. Delete Student
#             3. Display
#             4. Exit\n"""))

#     if(sts == 1):
#         obj.addStudent()
#     elif(sts == 2):
#         choice = int(input("Which student ID?"))
#         obj.deleteStudent(choice)
#     elif(sts == 3):
#         obj.display()
#     elif(sts == 4):
#         exit = True
#         break
#     else:
#         print("Enter 1 or 2 or 3 or 4")

"""Instance, Static and Local Variable"""

# Instance Var: New, seperate memory for every new object/instance. Syntax is inside class self.varname, outside class obj.varname

# class Student:
#     def __init__(self):
#         self.s_name = "Shreyas"
#         self.s_rollno = 101

#     def getdata(self):
#         self.s_mb = 282282828

# obj = Student()
# obj.getdata()
# obj.s_branch = "CS"
# print(obj.__dict__)
# print(obj.s_mb)

# hardcoded memory mgmt
# del obj.s_rollno
# print(obj.__dict__)


"""Static Variable: 
1.Can be declared
- inside class but outside method
- in a constructor by using class name
- in a instance method by using class name
- in a classmethod using class name or cls variable
- staticmethod by using classname

2.How do we access static variable?
- inside instance method using self or class name
- in a constructor using self or class name
- in a class method using cls variable or class name
- in a static method using class name
- outside of the class using object or class name

3.How to we delete the static variable?
- del classname.Staticvariablename
- inside classmethod we can use cls variable: del cls:Staticvariablename"""

# class College:
#     collegename = "Modern College"
#     def __init__(self):
#         self.studentname = "Prashant"
    
# principal = College()
# teacher = College()
# accountant = College()

# print("principal=", principal.collegename, "...", principal.studentname)
# print("principal=", teacher.collegename, "...", teacher.studentname)
# print("principal=", accountant.collegename, "...", accountant.studentname)
# College.collegename = "Halla Bulla"
# principal.studentname = "Shreyas"
# print("principal=", principal.collegename, "...", principal.studentname)
# print("principal=", teacher.collegename, "...", teacher.studentname)
# print("principal=", accountant.collegename, "...", accountant.studentname)


"""Static Method ================="""

# class Student:
#     # by using class name we can access this
#     @staticmethod #decorator
#     def get_personal_detail(Fname, Lname):
#         print("Your details: ", Fname, Lname)
    
#     @staticmethod
#     def contact_details(mobil_no, rollno):
#         print("Your contact details: ", mobil_no, rollno)

# Student.get_personal_detail("Shreyas", "Mhatre")
# Student.contact_details(535252642652, 1001)

"""Single Level Inheritance"""

# class College:
#     def college_name(self):
#         print("Modern COllege")

# class Student(College):
#     def student_info(self):
#         print("Name: Shreyas")
#         print("Branch: AIML")
    
# obj = Student()
# obj.college_name()
# obj.student_info()

"""Multi-Level Inheritance"""

# class College:
#     def college_name(self):
#         print("Modern College")

# class Student(College):
#     def student_info(self):
#         print("Name: Shreyas")
#         print("Branch: AIML")

# class Exam(Student):
#     def subject(self):
#         print("Subject1: Designe Engg")
#         print("Subject2: Math")
#         print("Subject3: C-lang")

# obj = Exam()
# obj.college_name()
# obj.student_info()
# obj.subject()

"Multiple Inheritance"

# class SubMarks:
#     math = int(input("Math Marks: "))
#     DE = int(input("DE: "))
#     C = int(input("C: "))
#     Eng = int(input("Eng: "))

#     def test(self):
#         print("Grand Father")

# class PracMarks:
#     cpract = int(input("C prac marks: "))

#     def test(self):
#         print("Father")

# class Result(SubMarks, PracMarks):
#     print("If pass in both, only then pass!")
#     def total(self):
#         if self.math>=40 and self.DE>=40 and self.C>=40 and self.Eng>=40 and self.cpract>=40:
#             print("Pass")
#         else:
#             print("Fail")

#     def test(self):
#         print("Child")

# obj = Result()
# obj.total()
# obj.test()