class AccessMethod:
    """constructor to initialize the username  and password """
    def __init__(self):
        self.username = input("Enter the usename: ")
        self.password = input("Enter the password: ")


    def print_details(self):
        """ printing username and password """
        print(f"username:{self.username},password:{self.password}")

AccessMethod().print_details()  # calling the print_details() method of class without self

        