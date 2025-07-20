import sys

# class Stack:
#     def __init__(self):
#         self.Liststack = []

#     def push(self, data):
#         self.Liststack.append(data)

#     def pop(self):

#         if not self.isEmpty():
#             # print(self.Liststack[-1])
#             print(self.Liststack.pop())

#         else:
#             print("Stack is empty!")

#     def isEmpty(self):

#         if self.Liststack == []:
#             return True
        
#         else:
#             return False

#     def displayStack(self):
#         print("Stack = ", self.Liststack)

#     def peek(self):
#         if not self.isEmpty():
#             print(self.Liststack[-1])

#         else:
#             print("Stack is Empty!")

#     def deleteStack(self):
#         self.Liststack = []
#         print("Stack is deleted!")



# if __name__ == "__main__":

#     obj = Stack() # object created for stack
#     print("Stack is created")

#     while True:
        
#         print("1. Push")
#         print("2. Pop")
#         print("3. Peek")
#         print("4. Display")
#         print("5. isEmpty()")
#         print("6. Delete Stack")
#         print("7. Exit")

#         ch = int(input("Enter your choice: "))

#         if ch == 1:
#             item = int(input("Enter the element for stack: "))
#             obj.push(item)
#             print("Push operation is done")

#         elif ch == 2:
#             obj.pop()

#         elif ch == 3:
#             obj.peek()

#         elif ch == 4:
#             obj.displayStack()

#         elif ch == 5:
#             print(obj.isEmpty())

#         elif ch == 6:
#             obj.deleteStack()

#         elif ch == 7:
#             sys.exit()

#         else:
#             print("Invalid Choice!")



""""Max Size Stack"""

import sys

class Stack:
    def __init__(self, size):
        self.max_size = size
        self.Liststack = []

    def push(self, data):

        if not self.isFull():
            self.Liststack.append(data)
        else:
            print("Stack is Full")

    def pop(self):

        if not self.isEmpty():
            # print(self.Liststack[-1])
            print(self.Liststack.pop())

        else:
            print("Stack is empty!")

    def isEmpty(self):

        if self.Liststack == []:
            return True
        
        else:
            return False

    def isFull(self):
        if len(self.Liststack) == self.max_size:
            return True
        else:
            return False

    def displayStack(self):
        print("Stack = ", self.Liststack)

    def peek(self):
        if not self.isEmpty():
            print(self.Liststack[-1])

        else:
            print("Stack is Empty!")

    def deleteStack(self):
        self.Liststack = []
        print("Stack is deleted!")



if __name__ == "__main__":

    obj = Stack(2) # object created for stack
    print("Stack is created")

    while True:
        
        print("1. Push")
        print("2. Pop")
        print("3. Peek")
        print("4. Display")
        print("5. isEmpty()")
        print("6. Delete Stack")
        print("7. Exit")

        ch = int(input("Enter your choice: "))

        if ch == 1:
            item = int(input("Enter the element for stack: "))
            obj.push(item)
            print("Push operation is done")

        elif ch == 2:
            obj.pop()

        elif ch == 3:
            obj.peek()

        elif ch == 4:
            obj.displayStack()

        elif ch == 5:
            print(obj.isEmpty())

        elif ch == 6:
            obj.deleteStack()

        elif ch == 7:
            sys.exit()

        else:
            print("Invalid Choice!")