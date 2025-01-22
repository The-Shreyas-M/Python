# Value error:
# a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# a[::2]=10,20,30,40,50,60
# print(a)

# python by default takes pass by reference:
# def func(value, values):
#     var = 1
#     values[0] = 44

# t = 3
# v = [1, 2, 3]
# func(t, v)
# print(t, v[0])

# data = [[[1, 2], [3, 4]], [[5, 6], [7, 8]]]

# def fun(m):
#     v = m[0][0]
#     for row in m:
#         for element in row:
#             if v < element : v = element
#     return v
# print(fun(data[0]))

# arr = [[1, 2, 3, 4], [4, 5, 6, 7], [8, 9, 10, 11], [12, 13, 14, 15]]
# for i in range(0, 4):
#     print(arr[i].pop(), end=" ")

# def f(i, values=[]):
#     values.append(i)
#     print(values, end=" ")

# f(1)
# f(2)
# f(3)

# arr = [1, 2, 3, 4, 5, 6]

# for i in range(1, 6):
#     arr[i-1] = arr[i]

# for i in range(0, 6):
#     print(arr[i], end = " ")

# List aliasing:
# fruit_list1 = ['Apple', 'Berry', 'Cherry', 'Papaya']
# fruit_list2 = fruit_list1
# fruit_list3 = fruit_list1[:] # Making copy of list
# fruit_list2[0] = 'Guava'
# fruit_list3[1] = 'kiwi'

# sum = 0
# for ls in (fruit_list1, fruit_list2, fruit_list3):
#     if ls[0] == 'Guava':
#         sum += 1
#     if ls[1] == "kiwi":
#         sum += 20

# print(sum)

"""Print this
1 5
2 4
4 2
5 1
"""
# My Own:

# r = range(1, 6)
# ptr_left = 0
# ptr_right = -1
# for i in range(1, 6):
#         if(not (r[ptr_right] == 3 and r[ptr_left] == 3)):
#             print(r[ptr_left], r[ptr_right])
#         ptr_left += 1
#         ptr_right -= 1
    
# Sir Logic:

# for i, j in zip(range(1, 6), range(5, 0, -1)):
#     if i == 3 and j == 3:
#         continue
#     print(i, j)

# Remove duplicate from string:

# string = 'Programming'
# final_string = ''

# for letter in string:
#     if letter not in final_string:
#         final_string += letter

# print(final_string)

# print tables:

# 
# for i in range(1, 11):
#     print(i*2,"|", i*3,"|", i*4,'|', i*4,"|", i*5, i*6)

# n^2 complexity
# count = 1
# for i in range(1, 11):
#     for j in range(1, 11):
#         print(i*j,end=" ")
#     print()

# Print:
# Enter no of rows:5
# A 
# A B 
# A B C 
# A B C D 
# A B C D E 

# n = int(input("Enter no of rows:"))

# for i in range(1, n+1):
#     for j in range(1, 1+i):
#         print(chr(64+j), end=" ")
#     print()


# 1 1 1 
# 2 2 2 
# 3 3 3

# for i in range(1, 4):
#     for j in range(1, 4):
#         print(i, end=" ")
#     print()

# palindrome:

# string = input("Type something: ")
# if(string[0::]== string[::-1]): print("palindrome")
# else: print('Not palindrome')

# couunt consonant and vowel:

# consonent_count = 0
# vowel_count = 0

# string = input("Type something: ")

# vowels = "aeiou"

# for letter in string:
#     if letter.lower() in vowels:
#         vowel_count += 1
#     else:
#         consonent_count += 1

# print(f"Vowels: {vowel_count}\nConsonents: {consonent_count}")

# anagram:

# str1 = list(input("Type something: "))
# str2 = list(input("Type something: "))
# str1.sort()
# str2.sort()
# if str1 == str2:
#     print("Anagram")


# Panagram: all alphabets in phrase

# str1 = list(input("Type a panagram: ").lower())
# str1.sort()
# alphabet = []
# for i in range(65, 91):
#     alphabet.append(chr(i).lower())

# if(str1 == alphabet): print("Panagram")
# else: print("Not")


# Substring:

# s1 = input("What is substring?")
# s2 = input("Ok now enter whole text")

# for i in s2:
#     if 
    
# print()




# Wipro problem: count repeating numbers

# data = int(input("Type the data string"))
# num_str=str(data)
# count = 0
# for i in set(num_str):
#     if num_str.count(i)>1:
#         count  += 1

# print(count)


# distance btw array elemts

# arr_size = int(input("Size of array?"))
# arr = []
# count = 0
# for i in range(1, arr_size):
#     a = int(input("::"))
#     arr.append(a)

# dist = 0

# for j in range(len(arr)):
#     if j+1 in range(len(arr)):
#         count += abs(arr[j]-arr[j+1])

# print(count)

# Count words in string:

# str1 = input("Enter a sentence: ")
# print(str1.count(" ")+1)
# lis = list(str1.split(" "))
# print(len(lis))

# Compression:

# str1 = input("Enter key")
# a = {}
# for i in str1:
#    a[i] = str1.count(i)

# for key, value in a.items():
#     print(key,value,sep="", end="")

# sum of all values in dict

# dic = {121:10,122:10,123:10}

# print(sum(dic.values()))

# dict basic:

# mydict = {101:"hihihih", 102:"dfsja", 103:"safdsa", 104:"asfadas"}
# print(type(mydict))
# print(mydict[102])
# mydict[102] = "Peter Parkerr"
# print(mydict[102])
# for x in mydict:
#     print(x)
# for x in mydict.items():
#     print(x)
# for x in mydict.values():
#     print(x)
# for x in mydict.keys():
#     print(x)
# for x,y in mydict.items():
#     print(x, y)

# mydict["Mobile number"] = 32453425423

# print(mydict)

# mydict.pop(101)
# print(mydict)

# sort dictionary:
# dic = {1:"a", 2:"e", 3:"b", 5:"n"}
# by_key = []
# by_values = []
# for key in dic.keys():
#     by_key.append(key)

# for value in dic.values():
#     by_values.append(value)

# by_key.sort()
# by_values.sort()
# print(by_values, dic[by_key])


# Exception Handling:

# a = int(input("Val 1: "))
# b = int(input("Val 2: "))

# try:
#     print(a/b)
# except:
#     print("CAnt divide by zero")



# try:
#     a = int(input("Val 1: "))
#     b = int(input("Val 2: "))
#     print(a/b)
# except ZeroDivisionError as message:
#     print("MMessaeg: ", message)

# except ValueError as message:
#     print("Value lol: ", message)

# Handling multiple exception with single block

# try:
#     a=int(input("Enter a: "))
#     b=int(input("Enter b: "))
#     print(a/b)
# except (ValueError, ZeroDivisionError) as message:
#     print(message)

# default except block: (put at last lol)

# try:
#     a=int(input("Enter a: "))
#     b=int(input("Enter b: "))
#     print(a/b)

# except:
#     print("U have entered default except block")

# except (ValueError, ZeroDivisionError) as message:
#     print(message)


# try:
#     a=int(input("Enter a: "))
#     b=int(input("Enter b: "))
#     print(a/b)

# except (ValueError, ZeroDivisionError) as message:
#     print(message)

# except:
#     print("U have entered default except block")

# we can also use else with try except

# try:
#     a=int(input("Enter a: "))
#     b=int(input("Enter b: "))
#     print(a/b)

# except (ValueError, ZeroDivisionError) as message:
#     print(message)

# else:
#     print("U have entered else")

# Finally block: always execute whether try block

# try:
#     a=int(input("Enter a: "))
#     b=int(input("Enter b: "))
#     print(a/b)

# except (ValueError, ZeroDivisionError) as message:
#     print(message)

# finally:
#     print("I will always execute")

"""Nested try except"""

# try:
#     a = int(input("A: "))
#     b = int(input("B: "))
#     try:
#         print(a/b)
#     except ZeroDivisionError as msg:
#         print(msg)
# except ValueError as msg:
#     print(msg)

"""Example statement"""
# try:
#     a = int(input("A: "))
#     b = int(input("B: "))
#     print(a/b)
# except (ZeroDivisionError, ValueError) as message:
#     print(message)
# else:
#     print("No error in try block")
# finally:
#     print("AAg lage basti mai apan apni masti mai")

"""Move zeros to end don't change order tho"""

# a = [0, 1, 5, 0, 0, 0, 0, 3, 12]
# print(a)
# for i in a:
#     if i == 0:
#         a.remove(i)
#         a.append(i)
# print(a)

"""Dutch National Flag sort array of 0, 1 and 2 in single pass"""

# a = [1, 2, 0, 1, 2, 1, 0]
# a0 = []
# a1 = []
# a2 = []

# for i in a:
#     if i == 0:
#         a0.append(i)
#     elif i == 1:
#         a1.append(i)
#     elif i == 2:
#         a2.append(i)
    
# print(a0 + a1 + a2)



"""Intersection"""
# A = [1, 2, 3]
# B = [2, 3, 4]
# C = [2, 4, 3]

# for i in A:
#     if i in B and i in C:
#         print(i)

"""Maximum consecutive ones in binary array"""

# a = [0,1,1,1,0,0,1,1,0,0,1,1,1,1,1,1]
# count = 1
# for i in a:
#     if i == 1 and a[i +1] == 1:
#         count += 1
#     else:
#         count = 0

# print(count)


"""Product of arrray except self"""

# a = [1, 2, 3, 4]
# b = []

# for i in range(len(a)):
#     b[i] = 

"""Find first non repeating element"""

# a = [1, 2, 3, 2, 1, 4, 5]
# for i in a:
#     if a.count(i) == 1:
#         print(i)
#         break

"""Split a list into chunks of given size"""

a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
b = []
chunk_size = int(input("Chunk size: "))


for i in range(0, len(a), chunk_size):
    b.append(a[i:i+chunk_size])


print(b)