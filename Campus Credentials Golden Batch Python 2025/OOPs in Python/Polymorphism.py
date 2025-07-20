"""DIfferent number of arguments then python will always consider only method"""

"Python doesn't support method overloading aka commpile time polymorphism"

# class Arithmetic:
#     def add(self, a):
#         print(a)
#     def add(self, a, b):
#         print(a+b)
#     def add(self, a, b, c):
#         print(a+b+c)

    
# obj = Arithmetic()
# obj.add(10)
# obj.add(10, 20)
# obj.add(1, 2, 3)

"""But wait! There's always a way around: (**************)"""

# Photo se likh
# class Arithmetic:
#     def add(self, a = None, b = None, c = None):
        
#         if a != None:
#             print(a)

#         if a != None and b != None and c != None:
#             print(a+b)

#         if a != None and b != None and c != None:
#             print(a+b+c)
        
            
# obj = Arithmetic()
# obj.add(10)
# obj.add(10,20)
# obj.add(1, 2, 3)


"""Constructor Overloading.... not supported"""

# class Arithmetic:
#     def __init__(self):
#         print("No Args")

#     def __init__(self, a):
#         print("One Args")

#     def __init__(self, a, b):
#         print("Two Args")

# obj = Arithmetic()
# obj = Arithmetic(10)
# obj = Arithmetic(2, 2)

"""Method Overriding (Python Supports): Dynamic or Run time polymorphism"""

# class Rbi:
#     def homeLoan_Rbi(self):
#         print("Home Loan Rate of Interest = 7.5%")
    
#     def carLoan(self):
#         print("Car Loan Rate of Interest = 8%")

# class Sbi(Rbi):
#     def homeLoan_Rbi(self):
#         print("Home Loan Rate of Interest = 6.5")
    
#         super().homeLoan_Rbi()

# obj = Sbi()
# obj.homeLoan_Rbi()
# obj.carLoan()

"""Constructor overridinng"""

# class Rbi:
#     def homeLoan_Rbi(self):
#         print("Home Loan Rate of Interest = 7.5%")
    
#     def carLoan(self):
#         print("Car Loan Rate of Interest = 8%")

# class Sbi(Rbi):
#     def homeLoan_Rbi(self):
#         print("Home Loan Rate of Interest = 6.5")
    
#         super().homeLoan_Rbi()

# obj = Sbi()

