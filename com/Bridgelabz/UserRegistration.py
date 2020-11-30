import re


class UserRegistration:
    NAME_REGEX = '^[A-Z]{1}[a-z]{3,}$'
    EMAIL_REGEX = '^[a-zA-Z0-9]+([.+-_][a-z-A-Z0-9]+)*@[a-zA-Z0-9]+.[a-z]{2,3}([.][a-z]{2})*$'

    # User First Name
    def user_firstname(self):
        """
        Taking the First Name from user and match with respective regex pattern
        """
        while True:
            user_name = input("Enter the User First Name : ")
            if re.fullmatch(UserRegistration.NAME_REGEX, user_name):
                print("Valid Name")
                break
            else:
                print("Invalid Name, Please enter name in proper format")

    # User Last Name
    def user_lastname(self):
        """
        Taking the Last Name from user and match with respective regex pattern
        """
        while True:
            user_name = input("Enter the User Last Name : ")
            if re.fullmatch(UserRegistration.NAME_REGEX, user_name):
                print("Valid Name")
                break
            else:
                print("Invalid Name, Please enter Name in proper format")

    # User Email
    def user_email(self):
        """
        Taking the Email Id from user and match with respective regex pattern
        """
        while True:
            user_email = input("Enter the Email Id : ")
            if re.fullmatch(UserRegistration.EMAIL_REGEX, user_email):
                print("Valid Email Id")
                break
            else:
                print("Invalid Emaild Id")


if __name__ == "__main__":
    user = UserRegistration()
    user.user_firstname()
    user.user_lastname()
    user.user_email()
