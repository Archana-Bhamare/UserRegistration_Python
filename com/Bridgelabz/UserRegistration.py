import re


class UserRegistration:
    NAME_REGEX = '^[A-Z]{1}[a-z]{3,}$'
    EMAIL_REGEX = '^[a-zA-Z0-9]+([.+-_][a-z-A-Z0-9]+)*@[a-zA-Z0-9]+.[a-z]{2,3}([.][a-z]{2})*$'

    # User First Name
    def user_firstname(self):
        while True:
            user_name = input("Enter the User First Name : ")
            result = re.match(UserRegistration.NAME_REGEX, user_name)
            if result:
                print("Valid Name")
                break
            else:
                print("Invalid Name, Please enter name in proper format")

    # User Last Name
    def user_lastname(self):
        while True:
            user_name = input("Enter the User Last Name : ")
            result = re.match(UserRegistration.NAME_REGEX, user_name)
            if result:
                print("Valid Name")
                break
            else:
                print("Invalid Name, Please enter Name in proper format")

    # User Email
    def user_email(self):
        while True:
            user_email = input("Enter the Email Id : ")
            result = re.match(UserRegistration.EMAIL_REGEX, user_email)
            if result:
                print("Valid Email Id")
                break
            else:
                print("Invalid Emaild Id")


if __name__ == "__main__":
    user = UserRegistration()
    user.user_firstname()
    user.user_lastname()
    user.user_email()
