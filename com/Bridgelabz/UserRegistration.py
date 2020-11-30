import re


class UserRegistration:
<<<<<<< HEAD
    pattern = '^[A-Z]{1}[a-z]{3,}$'

    # User First Name
<<<<<<< HEAD
    def user_name(self):
        user_name = input("Enter the User Name : ")
=======
    def user_firstname(self):
        user_name = input("Enter the User First Name : ")
>>>>>>> UC2-Last_Name
        result = re.match(UserRegistration.pattern, user_name)
=======
    NAME_REGEX = '^[A-Z]{1}[a-z]{3,}$'
    EMAIL_REGEX = '^[a-zA-Z0-9]+([.+-_][a-z-A-Z0-9]+)*@[a-zA-Z0-9]+.[a-z]{2,3}([.][a-z]{2})*$'

    # User First Name
    def user_firstname(self):
        user_name = input("Enter the User First Name : ")
        result = re.match(UserRegistration.NAME_REGEX, user_name)
>>>>>>> UC3_User_Email
        if result:
            print("Valid Name")
        else:
            print("Invalid Name, Please enter name in proper format")

<<<<<<< HEAD
<<<<<<< HEAD

if __name__ == "__main__":
    user = UserRegistration()
    user.user_name()
=======
    # User Last Name
    def user_lastname(self):
        user_name = input("Enter the User Last Name : ")
        result = re.match(UserRegistration.pattern, user_name)
=======
    # User Last Name
    def user_lastname(self):
        user_name = input("Enter the User Last Name : ")
        result = re.match(UserRegistration.NAME_REGEX, user_name)
>>>>>>> UC3_User_Email
        if result:
            print("Valid Name")
        else:
            print("Invalid Name, Please enter Name in proper format")

<<<<<<< HEAD
=======
    # User Email
    def user_email(self):
        user_email = input("Enter the Email Id : ")
        result = re.match(UserRegistration.EMAIL_REGEX, user_email)
        if result:
            print("Valid Email Id")
        else:
            print("Invalid Emaild Id")

>>>>>>> UC3_User_Email

if __name__ == "__main__":
    user = UserRegistration()
    user.user_firstname()
    user.user_lastname()
<<<<<<< HEAD
>>>>>>> UC2-Last_Name
=======
    user.user_email()
>>>>>>> UC3_User_Email
