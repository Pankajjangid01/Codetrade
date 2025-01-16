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

        except Exception as exe:  # handle error when error occurs during file opening 
            print(f"Error in opening file:{str(exe)}")


class LoginUser:
    """
        Description:Login Class which take the username and password and match if both username and password correct
    """

    def __init__(self):
        """
            Description:Constructor that takes the username and password and pass username and password to the check_user_info method
        """
        self.username = input("Enter your User Name: ")
        self.password = input("Enter your Password: ")


    def check_user_info(self):
        """
            Description: Function that opens the user CSV file, splits the data on the basis of commas,
            and stores them in a list. It then checks the username and password entered by the user against
            the stored data in the file.
        """
        try:
            with open("user.csv", 'r') as user_info:  # Open the user information file containing username and password
                user_data = user_info.readlines()[1:]  # Read the data of users from the file, skipping the header
                
                # Split the user data into a list of lists, where each list contains [username, password, isAdmin]
                user_data = [line.split(',') for line in user_data]
                
                # Iterate through each line of the data to check the username and password
                for info in user_data:
                    if info[0] == self.username and info[1] == self.password:  # Matching the username and password
                        print(f"Login Successful as {self.username}")
                        return True, info[2], self.username, self.password  # Return success if credentials match
                
                # If we reach here, no match was found, print invalid credentials message once
                # print("Invalid credentials")
                return False, 'False', 'False', "Invalid"  # Return failure if no match is found
        except IOError:
            print(f"Something went wrong, failed to open user.csv file... :{IOError}")
            return False, 'False', 'False', "Error"


        