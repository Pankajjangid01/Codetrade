import re

fields = []
rows = []

# Function to validate the password
def validate_password(password):
    """Checks is the password matches the regex pattern, if it not matches then show the error message """
    # Regex pattern: 
    # ^ = start, (?=.*[a-z]) = at least one lowercase, (?=.*[A-Z]) = at least one uppercase,
    # (?=.*[!@#$%^&*-) = at least one special character,
    # (?=.*[0-9]) = at least one digit, [^\s] = no spaces, .{8,} = minimum 8 characters.
    # import pdb
    # pdb.set_trace()
    pattern = r"^(?=.*[A-Z])(?=.*[a-z])(?=.*[0-9])(?=.*[#?!@$%^&*-]).{8,}$"
    # try:
    if re.match(pattern, password):
        return True
    raise Exception("Password must be at least 8 characters long, contain at least one lowercase letter, one uppercase letter, one special character, one digit, and must not have spaces.")


def open_file(name,branch,roll_number,password):
    """
    opening the file in the read and write mode using a+ mode at the same time to append data in the file and read the file 
    check if the content exists in the file or not, if not then append header first after that append data to the file and read the content of file
    """
    try:
        with open("user.csv", "a+") as file:
            # Write and read from the text file
            file.seek(0)  # Move to the start of the file
            content = file.read()  # read the cotent of file whether it is empty or not 
        
            # Check if the file is empty
            if not content:
                file.write("Name,Branch,Roll No.,Password.\n")  # Write header if file is empty

            # Append the user data
            file.write(f"{name},{branch},{roll_number},{password}\n")
        
            # Move back to the start and display the file content
            file.seek(0)
            print("\nFile Content:",file.read())

    except Exception as exe:  # handle error when error occurs during file opening 
        print("Error in opening file:",str(exe))


def main():
    """main function taking input from the user and calling the validtion password function and openin the file by calling openfile function"""
    # Get user input
    name = input("Enter name: ")
    branch = input("Enter the Branch: ")
    try:
        while True:
            try:
                roll_number = int(input("Enter the Roll Number: "))
                password = input("Enter Password: ")
                # import pdb;pdb.set_trace()
                validate_password(password)
                open_file(name,branch,roll_number,password)
                break
            except Exception as exe:
                print("Error:", str(exe))
    except Exception as exe:
        print(str(exe))

main()  # calling the main function 