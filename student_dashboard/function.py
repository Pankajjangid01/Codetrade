# class AccessMethod:
#     """constructor to initialize the username  and password """
#     def __init__(self):
#         self.username = input("Enter the usename: ")
#         self.password = input("Enter the password: ")


#     def print_details(self):
#         """ printing username and password """
#         print(f"username:{self.username},password:{self.password}")

# AccessMethod().print_details()  # calling the print_details() method of class without self
class StudentTest:
    """
        Desciption: Student class that handle the take-test student functionality    
    """
    def __init__(self, username, password):
        """
            Description: Constructor to set the username and password and initialize score and total questions
        """
        self.username = username
        self.password = password
        self.score = 0
        self.total_questions=0
    
    def start_test(self):
        """
            Description: Method to start the test
        """
        print("Test Started\n")
        try:
            with open('questions.csv','r') as question_file, open('answers.csv','r') as answers_file:
                question_lines = question_file.readlines()[1:]
                answers_lines = answers_file.readlines()[1:]

                self.total_questions = len(question_lines)  # set the totol number of questions 

                if len(question_lines) != len(answers_lines):
                    print("Number of questions and Number of Answers are not equal")
                    return
                for question_index in range(len(question_lines)):
                    question = question_lines[question_index].split(":")[1].strip()  # Extract the question text         
                    answer = answers_lines[question_index].split(',')[1:]  # extract the answers and split them on the basis of ','
                    answer_list=[]  # created a new list 

                    # import pdb+
                    # pdb.set_trace()
                    right_answer = None  # mark the right answer None initially when we havent taken input from user
                    for element in range(len(answer)):
                        if '[' in answer[element]:
                            right_answer = chr(element + 97)  # find the correct answer and store it in the righ answer
                        answer_list.extend(answer[element].replace('['," ").replace(']'," ").split())  # replace the '[' and ']' with empty " "

                    print(f"Ques {question_index+1}: {question}")
                    for index in range(len(answer_list)):
                        print(f"{chr(97+index)}){answer_list[index]}")
                    
                    user_answer = None  # set the user answer None and get the answer from the user then 
                    while user_answer not in ['a','b','c','d']:
                        user_answer = input("Enter your answer (a/b/c/d): ").lower()

                    if user_answer == right_answer:
                        self.score += 1
                      
                self.display_result()

        except IOError:
            print(f"Something went wrong while opening Questions or Answers file {str(IOError)}")

    def display_result(self):
        """
        Description: Display the result to the student.
        """
        percentage = (self.score / self.total_questions) * 100 if self.total_questions else 0
        print(f"\nYour result: {percentage:.2f}%")
        self.store_result(percentage)
    
    def store_result(self, percentage):
        """
        Description: Store the student's result in a CSV file.
        """
        try:
            with open("Results.csv", 'a', newline='') as result_file:
                result_writer = result_file.write(result_file)

                if result_file.tell() == 0:
                    result_writer.writerow(["Username", "Score", "Percentage"])

                result_writer.writerow([self.username, self.score, f"{percentage:.2f}%"])

            print("Result saved successfully!")

        except Exception as e:
            print(f"Error while storing the result: {str(e)}")
        
    def store_result(self, percentage):
        """
        Description: Store the student's result in a CSV file.
        """
        try:
            with open("results.csv", 'a', newline='') as result_file:
                if result_file.tell() == 0:
                    result_file.write("Username,Password,Score,Percetage\n")
                result_file.write(f"{self.username},{self.password}, {self.score}, {percentage:.2f}%\n")

            print("Result saved successfully!")

        except Exception as e:
            print(f"Error while storing the result: {str(e)}")  
studnt=StudentTest("Pankaj","Pankaj@345")
studnt.start_test()