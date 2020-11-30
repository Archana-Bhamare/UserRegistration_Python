import re


class UserRegistration:
    NAME_REGEX = '^[A-Z]{1}[a-z]{3,}$'
    EMAIL_REGEX = '^[a-zA-Z0-9]+([.+-_][a-z-A-Z0-9]+)*@[a-zA-Z0-9]+.[a-z]{2,3}([.][a-z]{2})*$'
    MOBILE_REGEX = '^[91]{2}[ ]?[0-9]{10}$'
    PASSWD_REGEX = '^(?=.*[A-Z])[a-zA-Z0-9]{8,}$'

    # User First Name
    def user_firstname(self):
        user_name = input("Enter the User First Name : ")
        result = re.match(UserRegistration.NAME_REGEX, user_name)
        if result:
            print("Valid Name")
        else:
            print("Invalid Name, Please enter name in proper format")

    # User Last Name
    def user_lastname(self):
        user_name = input("Enter the User Last Name : ")
        result = re.match(UserRegistration.NAME_REGEX, user_name)
        if result:
            print("Valid Name")
        else:
            print("Invalid Name, Please enter Name in proper format")

    # User Email
    def user_email(self):
        user_email = input("Enter the Email Id : ")
        result = re.match(UserRegistration.EMAIL_REGEX, user_email)
        if result:
            print("Valid Email Id")
        else:
            print("Invalid Email Id")

    # User Email
    def user_mobnumber(self):
        user_mobnumber = input("Enter the Mobile Number : ")
        result = re.match(UserRegistration.MOBILE_REGEX, user_mobnumber)
        if result:
            print("Valid Mobile Number")
        else:
            print("Invalid Mobile Number")

    # User Password
    def user_password(self):
        user_password = input("Enter the Password : ")
        result = re.match(UserRegistration.PASSWD_REGEX, user_password)
        if result:
            print("Valid Password")
        else:
            print("Invalid Password, Please enter valid password")


if __name__ == "__main__":
    user = UserRegistration()
    user.user_firstname()
    user.user_lastname()
    user.user_email()
    user.user_mobnumber()
    user.user_password()