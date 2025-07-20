class Questions:
   
    def __init__(self):
        
        self.question_list = []
        self.option1 = []
        self.option2 = []
        self.option3 = []
        self.option4 = []
        self.correct_choice = []
        self.marks = []

    def create_exam(self):
        
        self.no_questions = 0
        self.no_questions = int(input("How many questions? "))

        for i in range(self.no_questions):
            self.question_string = input("Question: ")
            self.question_list.append(self.question_string)
            print("Enter the options:")
            self.option1.append(input("1."))
            self.option2.append(input("2."))
            self.option3.append(input("3."))
            self.option4.append(input("4."))
            self.correct_option = int(input("Correct Option: "))
            self.correct_choice.append(self.correct_option)    

    def take_exam(self):

        if self.question_list != []:
            for i in range(len(self.question_list)):
                print(self.question_list[i])
                print("1. ", self.option1[i])
                print("2. ", self.option2[i])
                print("3. ", self.option3[i])
                print("4. ", self.option4[i])

                self.choice = int(input("Choice: "))

                if self.choice == self.correct_choice[i]:
                    self.marks.append(5)
                else:
                    self.marks.append(0)
        
        else:
            print("No test available create one")
    

    def display_marks(self):
        print("Your Score: ", sum(self.marks), "Out of:", self.no_questions*5)
    
    
if __name__ == "__main__":

    questions = Questions()

    while(True):
    
        Dashboard_choice = int(input("\n 1. Admin Create Exam \n 2. Take Exam \n 3. Exit \n:"))

        if Dashboard_choice == 1:
            questions.create_exam()


        elif Dashboard_choice == 2:
            questions.take_exam()
            questions.display_marks()

        elif Dashboard_choice == 3:
            break