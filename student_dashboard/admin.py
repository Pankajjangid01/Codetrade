
class Admin_Registration:
    """
        Description:Admin Registration class used to check that the user is registered or not registered
                    and if it is already registered then it is admin or not
                    Calling the login class default constructor to check the user input with the data stored in csv file return the username,password
    """
    def __init__(self):
        """
            Description: constructor to take input user registered or not 
        """
        self.user=input("User Already Exist?").lower().strip=='y'  # asks if user alreadey exist or not

  

   