"""Way 1: By module name we will access var, func, class etc"""

# import module1

# module1.square(4)
# module1.login("User", "Pass")
# print(module1.pi)

"""Way 2: Alias or short cut name"""

# import module1 as m1

# m1.square(4)
# m1.login("User", "Pass")
# print(m1.pi)

"""Way 3: import a specific func/var/class etc"""

# from module1 import login, pi,square,welcome # Press ctrl+space for suggestions

# print(pi)
# square(4)
# login("User", "User")

"""Way 4: If you are looking"""

# from module1 import*

# square(4)
# login("User", "Pass")
# print(pi)