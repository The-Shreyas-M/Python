"""File Handling"""

# f = open("Myfile.txt", "w")
# print("Name: ", f.name)
# print("file mode", f.mode)
# print("Readable?", f.readable())
# print("Writable", f.writable())
# print("File closed: ", f.closed)
# f.close()
# print("File closed: ", f.closed)

"""Write mode: Overwrites data"""
# f = open("Myfile.txt", "w")
# f.write("\n Hi lol is smart city")
# f.close()
# print("File operation done")

"""Append mode: Adds in the end"""
# f = open("Myfile.txt", "a")
# f.write("\n Hi lol is smart city")
# f.close()
# print("File operation done")

"""Read and write mode"""

"""Inserting list"""
# f = open("Myfile.txt", "w")
# myList = ["prashant", "mahesh", "suresh"]
# f.writelines(myList) # this can be used for all collection data types
# f.close()
# print("Written work has been done success!!")

"""Reading data from file"""
# f = open("covid.txt", "r")
# print(f.read())
# f.close

"""With statement no need to worry about closing"""
# with open("with.txt", "w") as f:
#     f.write("SHreyas\n")
#     f.write("Mhatre\n")
#     f.write("Rajesh\n")
#     print("File Closed? ", f.closed)
# print("File closed: ", f.closed)

"""Reading with with:"""
# with open("with.txt", "r") as f:
#     a = f.readlines()
#     print("File Closed? ", f.closed)
# print(a)
# print("File closed: ", f.closed)

"""HW : tell() and seek() function"""