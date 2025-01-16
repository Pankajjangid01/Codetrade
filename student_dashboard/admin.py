from student_details import LoginUser, SignupUser  
from question_answer import QuestionPaper, SetAnswer  


class AdminRegistration:
    """
        Description: Admin Registration class used to check if the user is registered or not,
                    and if registered, whether the user is an admin or not.
                    It calls the login class default constructor to check the user input
                    with the data stored in a CSV file, and returns the username and password.
    """
    def register_admin(self):
        """
            Description: Constructor to check if the user is registered or not.
        """
        try:
            is_user_exist = input("User Already Exist? (press 'y' if exists, 'n' if not): ").lower().strip()
            
            # Ensure valid input (either 'y' or 'n')
            while is_user_exist not in ['y', 'n']:
                print("Invalid input. Please enter 'y' for yes or 'n' for no.")
                is_user_exist = input("User Already Exist? (press 'y' if exists, 'n' if not): ").lower().strip()

            if is_user_exist == 'y':  # Check if the user exists
                user_login = LoginUser()  # Calling the login class to authenticate the user
                is_logged_in, admin_status, username, password = user_login.check_user_info()  # Verifying user credentials

                if is_logged_in:
                    admin_status = admin_status.strip()  # Clean up any newline or extra spaces
                    if admin_status == "True":
                        return 1, username, password  # User is admin, return admin access details
                    else:
                        return 2, username, password  # User is not admin, return regular user access details
                else:
                    if password == "Invalid":
                        return 3, None, None  # Invalid credentials
            else:  # User is not registered
                print("User is not registered.")
                return None, None, None
        except Exception as exe:
            print(f"Error during admin registration: {str(exe)}")
            return None, None, None



class AdminAccess:
    """
        Description: If the user is an admin, this class allows them to add new users,
                    create question papers, and manage answers.
    """
    def provide_admin_access(self):
        """
        Description: Provides admin functionalities such as adding new users or creating question papers.
        """
        try:
            admin_role = int(input("Enter 1 for adding new user\nEnter 2 for setting question paper: "))
            if admin_role == 1:  # Add a new user
                SignupUser()  # Call the SignUp class to register a new user
            elif admin_role == 2:  # Create question paper and set answers
                question_paper = QuestionPaper()  # Create the question paper
                total_questions = question_paper.total_question  # Get the total number of questions entered
                answer_manager = SetAnswer(total_questions)  # Manages the answer sets
                answer_manager.add_answers_to_file()  # Sets the answers for the questions
            else:
                print("Invalid choice. Please try again.")
        except Exception as e:
            print(f"Error during admin access: {str(e)}")


class MainApplication:
    """
        Description: Main class that controls the flow of the program, whether to provide admin access or student functionalities.
    """
    def __init__(self):
        self.admin_registration = AdminRegistration()  # Initialize the AdminRegistration class
        self.admin_access = AdminAccess()  # Initialize the AdminAccess class

    def main_function(self):
        """
            Description: The main function checks the registration status of the user and provides
                         access to either the admin panel or student functionalities.
        """
        try:
            admin_number, username, password = self.admin_registration.register_admin()  # Check user registration and determine admin/student access

            if admin_number == 1:  # Admin access
                self.admin_access.provide_admin_access()  # Admin access functionalities
            elif admin_number == 2:  # Student access
                print("Student functionalities coming soon.")
            elif admin_number == 3:  # Invalid credentials
                print("Invalid credentials. Please try again.")
            else:  # User not registered
                print("Please ask the administrator for registration.")
        except Exception as e:
            print(f"Error during main execution: {str(e)}")


# Entry point for the program
if __name__ == "__main__":
    app = MainApplication()  # Instantiate the MainApplication class
    app.main_function()  # Execute the main function to start the program


# is_user_exists = input("User Already Exist? (press 'y' if exists): ").lower().strip() == 'y'  in this if user enter n then show user not registered and if the input is other than y or n then tell the user to give valid input (y/n)