import re 
class SignupUser:
    """Class to create the function to signup and store their information in the user_info csv file """
    def __init__(self):
        try:
            self.admin = input('Is Admin (y/n): ').lower().strip() == 'y'
            self.username = input("Enter the username: ")
            while True:
                try:
                    password = input("Enter Password: ")
                    self.validate_password(password)
                    self.open_file(password)
                    break
                except Exception as exe:
                    print("Error:", str(exe))
        except Exception as exe:
            print(str(exe))

    # Function to validate the password
    def validate_password(self,password):
        """
            Desctiption:Checks is the password matches the regex pattern, if it not matches then show the error message
        """
        pattern = r"^(?=.*[A-Z])(?=.*[a-z])(?=.*[0-9])(?=.*[#?!@$%^&*-]).{8,}$"
        if re.match(pattern, password):
            return True
        raise Exception("Password must be at least 8 characters long, contain at least one lowercase letter, one uppercase letter, one special character, one digit, and must not have spaces.")

    def open_file(self,password):
        """
            Description:opening the file in the read and write mode using a+ mode at the same time to append data in the file and read the file 
            check if the content exists in the file or not, if not then append header first after that append data to the file and read the content of file
        """
        try:
            with open("user.csv", "a+") as file:
                # Write and read from the text file
                file.seek(0)  # Move to the start of the file
                content = file.read()  # read the cotent of file whether it is empty or not 
        
                # Check if the file is empty
                if not content:
                    file.write("User-Name,Password,isAdmin\n")  # Write header if file is empty

                # Append the user data
                file.write(f"{self.username},{password},{self.admin}\n")
                print("User added successfully")

        except IOError:  # handle error when error occurs during file opening 
            print(f"Error in opening file:{str(IOError)}")

class LoginUser:
    """
    Description: Login Class that takes the username and checks if the username exists in the file,
    then asks for the password to validate the login.
    """

    def check_user_info(self):
        """
        Description: Function that checks if the entered username exists,
        then validates the password against the username.
        """
        max_attempts = 3  # Maximum number of login attempts
        attempts = 0

        while attempts < max_attempts:
            self.username = input("Enter username: ").strip()
            
            try:
                with open("user.csv", 'r') as user_info:  # Open the user information file containing username and password
                    user_data = user_info.readlines()[1:]  # Read user data, skipping the header

                    # Split the user data into a list of lists, where each list contains [username, password, isAdmin]
                    user_data = [line.strip().split(',') for line in user_data]

                    # Check if the username exists
                    user_record = next((info for info in user_data if info[0] == self.username), None)  # checks the current user info if not match then move to the next user in the list 
                    
                    if not user_record:
                        print("Username not found. Try again.")
                        attempts += 1
                        print(f"Attempts left: {max_attempts - attempts}")
                        continue

                    # If username exists, ask for the password
                    for _ in range(max_attempts):
                        self.password = input("Enter password: ").strip()
                        if self.password == user_record[1]:  # Validate password
                            print(f"Login Successful as {self.username}")
                            return True, user_record[2], self.username, self.password  # Return success with role information
                        else:
                            print("Invalid password. Try again.")
                    
                    print("Maximum password attempts exceeded for this username.")
                    return False, 'False', 'False', 'False'

            except IOError:
                print(f"Something went wrong, failed to open user.csv file... :{str(IOError)}")
                return False, 'Error', 'Error', 'Error'

        # After maximum attempts for username validation are exhausted
        print("Maximum attempts exceeded. Please try again later.")
        return False, 'False', 'False', 'False'    
    
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

                    right_answer = None  # mark the right answer None initially when we havent taken input from user
                    for element in range(len(answer)):
                        if '[' in answer[element]:
                            right_answer = chr(element + 97)  # find the correct answer and store it in the righ answer
                        answer_list.extend(answer[element].replace('['," ").replace(']'," ").split(','))  # replace the '[' and ']' with empty " "

                    print(f"Ques {question_index+1}: {question}")
                    for index in range(len(answer_list)):
                        print(f"{chr(97+index)}:{answer_list[index]}")
                    
                    user_answer = None  # set the user answer None and get the answer from the user then 
                    while user_answer not in ['a','b','c','d']:
                        user_answer = input("Enter your answer (a/b/c/d): ").lower()
                        print("Invalid option, please choose from(a/b/c/d)")

                    if user_answer == right_answer:
                        self.score += 1
                      
                self.display_result()

        except IOError:
            print(f"Something went wrong while opening Questions or Answers file {str(IOError)}")

    def display_result(self):
        """
        Description: Display the result to the student.
        """
        try:
            percentage = (self.score / self.total_questions) * 100 if self.total_questions else 0
            print(f"\nYour result: {percentage:.2f}%")
            self.store_result(percentage)

        except ValueError:
            print(f"Error in displaying Result: {str(ValueError)}")
        
    def store_result(self, percentage):
        """
        Description: Store the student's result in a CSV file.
        """
        try:
            with open("results.csv", 'a', newline='') as result_file:
                if result_file.tell() == 0:  # checks if it is header or not if it is at 0 then write the header 
                    result_file.write("Username,Password,Score,Percetage\n")
                result_file.write(f"{self.username},{self.password}, {self.score}, {percentage:.2f}%\n")  # store the username,password,score,percentage in result csv file

            print("Result saved successfully!")

        except IOError:
            print(f"Error while storing the result: {str(IOError)}")


        