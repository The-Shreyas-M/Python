import csv

# f = open("student.csv", "a", newline="")
# a = csv.writer(f) # here it will return csvwriter object that helps do all operations
# a.writerow(["studentID", "rollno", "name", "mobileno"])

# how_many_records = int(input("How many records?"))

# while(how_many_records):
#     studentid = int(input("Student ID: "))
#     rollno = int(input("Enter your roll no: "))
#     name = input("Enter your name: ")
#     mobileno = int(input("Enter your mobile no: "))
#     how_many_records -= 1
#     a.writerow([studentid, rollno, name, mobileno])
#     print("Updated")
# f.close()

"""Student marks management system"""

# with open("Studmgm.csv", "a") as f:
#     a = csv.writer(f)
#     #a.writerow(['ID', 'StudentName', 'StudentEmail', 'MobileNo', 'p1', "p2", 'p3', "p4", "p5", "totalMarks", "percentage", "result"])
#     id = int(input("Student ID: "))
#     StudentName = input("Name: ")
#     StudentEmail = input("Email: ")
#     MobileNo = int(input("Mobile no: "))

#     p1 = int(input("p1: "))
#     p2 = int(input("p2: "))
#     p3 = int(input("p3: "))
#     p4 = int(input("p4: "))
#     p5 = int(input("p5: "))

#     totalMarks = p1 + p2 + p3 + p4 + p5
#     percentage = totalMarks/5
#     if(p1 < 40 or p2 < 40 or p3 < 40 or p4 < 40 or p5 < 40):
#         result = "Fail"
#     else:
#         result = "Pass"
    
#     a.writerow([id, StudentName, StudentEmail, MobileNo, p1, p2, p3, p4, p5, totalMarks, percentage, result])