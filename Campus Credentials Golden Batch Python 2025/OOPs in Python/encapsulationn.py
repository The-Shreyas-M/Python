# Encapsulation

"""Creating a base class"""

"""Private Variable: strongly private in python, only accessible in Class"""

# class Base:
#     def __init__(self):
#         print("Parent class constructor called")
#         self.a = "prashant" # Public Variable
#         self.__c = "Ashish" # Private Variable
    
# class Derived(Base):
#     def __init__(self):

#         # Call constructor of Base Class
#         Base.__init__(self)
#         print("Calling provate member of base class")
#         print(self.a)
#         # print(self.__c)

# obj1 = Derived()
# print(obj1.a)
# print(obj1.__c)
# obj2 = Base()
# print(obj2.__c)

"""Protected Variable: Child has access"""

# class Base:
#     def __init__(self):
#         print("Parent class constructor called")
#         self.a = "prashant" # Public Variable
#         self._c = "Ashish" # Private Variable
    
# class Derived(Base):
#     def __init__(self):

#         # Call constructor of Base Class
#         Base.__init__(self)
#         print("Calling provate member of base class")
#         print(self.a)
#         print(self._c)

# obj1 = Derived()
# print(obj1.a)
# print(obj1._c)
# obj2 = Base()
# print(obj2._c)

"""Private Method"""

# class Rbi:
#     def publicPolicy(self):
#         print("Check the publilc policy")

#     def __privatePolicy(self):
#         print("This is not access to public")

# class Sbi(Rbi):
#     def __init__(self):
#         Rbi.__init__(self)

#     def callingPublicMethod(self):
#         print("\n Inside child class")
#         self.publicPolicy()

#     def callingPrivateMethod(self):
#         self.__privatePolicy()

# obj1 = Sbi()
# obj1.callingPublicMethod()
# obj1.callingPrivateMethod()
# obj1.publicPolicy()
# obj1.__privatePolicy()
# obj2 = Rbi()
# obj2.publicPolicy()
# obj2.__privatePolicy()





"""Why calling constructors... use case?"""
# Cuz if we don't then it will override

"""How to use Private Variable then?"""
# Getter Setters

"""Protected Method"""

# class Rbi:
#     def publicPolicy(self):
#         print("Check the publilc policy")

#     def _privatePolicy(self):
#         print("This is not access to public")

# class Sbi(Rbi):
#     def __init__(self):
#         Rbi.__init__(self)

#     def callingPublicMethod(self):
#         print("\n Inside child class")
#         self.publicPolicy()

#     def callingPrivateMethod(self):
#         self._privatePolicy()

# obj1 = Sbi()
# obj1.callingPublicMethod()
# obj1.callingPrivateMethod()
# obj1.publicPolicy()
# obj1._privatePolicy()
# obj2 = Rbi()
# obj2.publicPolicy()
# obj2._privatePolicy()