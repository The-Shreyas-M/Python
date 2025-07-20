import csv

"""# printing without list view"""

# with open("exam.csv", "r") as f:
#     r = csv.reader(f)
#     data = list(r)

#     for line in data:
#         for word in line:
#             print(word, "\t", end = "")
#         print()

def addQuestions():

    with open("exam.csv", "a", newline="") as f:
        r = csv.writer(f)
        
        no_questions = 0
        no_questions = int(input("How many questions you want to add? "))

        

        for i in range(no_questions):

            question = input("Question: ")
            print("Enter the options: ")
            option1 = input("1.")
            option2 = input("2.")
            option3 = input("3.")
            option4 = input("4.")
            correct_option = int(input("Correct Option?"))

            r.writerow([question, option1, option2, option3, option4, correct_option])

def readQuestions():
    
    with open("exam.csv", "r") as file:
        
        reader = csv.reader(file)

        for row in reader:
            print(row[0])

        

addQuestions()
readQuestions()

