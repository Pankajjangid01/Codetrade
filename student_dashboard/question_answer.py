class Question_Paper:

    """Description: Class to take the Questions from the user and store them in questions.csv file"""

    def __init__(self):
        """Constructor to ask the user for the number of question and store them in csv file"""
        self.total_question = int(input("Enter the number of questions you want to enter: "))  # ask the user to enter the number of question 
        self.add_questions_to_file()  # calling the add_questions_to_file() to add the questions to the file
        
    def add_questions_to_file(self):
        """Description:This function open the question.csv file if it does not exits then it create that file and then ask the user to enter the questions"""
        try:
            with open('Questions.csv','w') as question_file:
                question_file.write("Question Number:Question\n")  # writing header in the file

                for question_number in range(self.total_question):  
                    write_question = input(f"Enter the question {question_number+1}: ")  # taking the question from the user, question_number+1 because loop start from 0 
                    question_file.write(f"{question_number+1}:{write_question}\n")  # write each question to the file 

            # print("Questions added successfully")
            
        except Exception as exe:
            print("Something went wrong,please try again later...",str(exe))  #handle the exception if any error occur in writing the question to file



class Set_Answer:
    """
    Description: Class manages the creation and store the answer set in the answer.csv file for each question
    It takes four option for each question and identifies the correct option and then store them in csv file
    """
    def __init__(self,total_question):
        """Description: Constructor to assign the value to total_questions"""
        self.total_question=total_question

    def add_answers_to_file(self):
        """Description: This function open the questions file in read mode and for each question it takes the 4 option and and identifies the correct option"""
        try:
            with open("Questions.csv",'r') as read_question:
                # import pdb
                # pdb.set_trace()
                questionlines=read_question.readlines()[1:]  # read the complete question file except the header
            
            with open("Answers.csv",'w') as answer_file:  # open the answer or creates it if it does not exist in write mode
                answer_file.write("S.no.: Option 1, Option 2, Option 3, Option 4\n")  # write the header in the answer file
                for answer in range(total_question):
                    print(f"\nEnter answers for Question {answer + 1}:")
                    options = [input("Option A: "), input("Option B: "), input("Option C: "), input("Option D: ")]  # store the options in list
                    correct_option = input("Which option is correct (a/b/c/d)? ").lower()  # ask the user which option is correct 
                    options[ord(correct_option)-97] = f"[{options[ord(correct_option)-97]}]"  # used to mark the correct option in []
                    answer_file.write(f"{answer + 1}: A: {options[0]}, B: {options[1]}, C: {options[2]}, D: {options[3]}\n")  # store the options in the answer file 
            # print("Answers Added Successfully")
        except Exception as exe:
            print("Something went wrong, try again later...",str(exe))  # handle exception if any error occur in reading questions or writing answer to the file 

questionobj=Question_Paper()
total_question=questionobj.total_question
answerobj=Set_Answer(total_question)
answerobj.add_answers_to_file()