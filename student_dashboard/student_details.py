import re 
class Signup_User:
    """Class to create the function to signup and store their information in the user_info csv file """
    def __init__(self):
        try:
            self.admin = input('Is Admin (y/n): ').lower().strip() == 'y'
            self.username = input("Enter the username: ")
            while True:
                try:
                    password = input("Enter Password: ")
                    # import pdb
                    # pdb.set_trace()
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
        # try:
        if re.match(pattern, password):
            return True
        raise Exception("Password must be at least 8 characters long, contain at least one lowercase letter, one uppercase letter, one special character, one digit, and must not have spaces.")


    def open_file(self,password):
        """
            Description:opening the file in the read and write mode using a+ mode at the same time to append data in the file and read the file 
            check if the content exists in the file or not, if not then append header first after that append data to the file and read the content of file
        """
        try:
            with open("User.csv", "a+") as file:
                # Write and read from the text file
                file.seek(0)  # Move to the start of the file
                content = file.read()  # read the cotent of file whether it is empty or not 
        
                # Check if the file is empty
                if not content:
                    file.write("User-Name,Password,isAdmin\n")  # Write header if file is empty

                # Append the user data
                file.write(f"{self.username},{password},{self.admin}\n")
        
                # Move back to the start and display the file content
                file.seek(0)
                print("\nFile Content:",file.read())

        except Exception as exe:  # handle error when error occurs during file opening 
            print("Error in opening file:",str(exe))

# signupobj=Signup_User()  # creating the Signup class object

class Login_User:
    """
        Description:Login Class which take the username and password and match if both username and password correct
    """

    def __init__(self):
        """
            Description:Constructor that takes the username and password and pass username and password to the check_user_info method
        """
        self.username = input("Enter your User Name: ")
        self.password = input("Enter your Password: ")
        self.check_user_info()

    def check_user_info(self):
        try:
            user_info = open("User.csv",'r')  # opens the user Information file containg username and password
            user_data = user_info.readlines()[1:]  # read the data of user from the file 
            user_data=[user_data[serial_number].split(',') for serial_number in range(len(user_data))]  # Store the userdata in the list  to iterate and check uesnrame and password


            for info in range(len(user_data)):
                # import pdb
                # pdb.set_trace()
                if user_data[info][0]==self.username and user_data[info][1]==self.password:  # matching the user input details with the details stored in file if it match then login.
                    print("Login Successfull")
                    return True,user_data[info][3],self.username,self.password  # return the csv file content i.e true for user login, isAdmin, username, password 
            return False,'False','False','False'  # return false if user is entering invalid credentials 
        except Exception as exe:
            print("User Failed to login")
            
loginobj=Login_User()  # creating the Login class object
        