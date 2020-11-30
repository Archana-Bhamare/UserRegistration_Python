import re


class UserRegistration:
    NAME_REGEX = '^[A-Z]{1}[a-z]{3,}$'
    EMAIL_REGEX = '^[a-zA-Z0-9]+([.+-_][a-z-A-Z0-9]+)*@[a-zA-Z0-9]+.[a-z]{2,3}([.][a-z]{2})*$'
    MOBILE_REGEX = '^[91]{2}[ ]?[0-9]{10}$'
    PASSWD_REGEX = '^(?=.*[A-Z])(?=.*[0-9])[a-zA-Z0-9]{8,}'

    # User First Name
    def user_firstname(self):
        """
        Taking the First Name from user and match it with respective regex pattern
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
        Taking the Last Name from user and match it with respective regex pattern
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
        Taking the Email Id from user and match it with respective regex pattern
        """
        while True:
            user_email = input("Enter the Email Id : ")
            if re.fullmatch(UserRegistration.EMAIL_REGEX, user_email):
                print("Valid Email Id")
                break
            else:
                print("Invalid Email Id")

    # User Email
    def user_mobnumber(self):
        """
        Taking the Mobile Number from user and match it with respective regex pattern
        """
        while True:
            user_mobnumber = input("Enter the Mobile Number : ")
            if re.fullmatch(UserRegistration.MOBILE_REGEX, user_mobnumber):
                print("Valid Mobile Number")
                break
            else:
                print("Invalid Mobile Number")

    # User Password
    def user_password(self):
        """
        Taking the Password from user and match it with respective regex pattern
        """
        while True:
            user_password = input("Enter the Password : ")
            if re.fullmatch(UserRegistration.PASSWD_REGEX, user_password):
                print("Valid Password")
                break
            else:
                print("Invalid Password, Please enter valid password")


if __name__ == "__main__":
    user = UserRegistration()
    user.user_firstname()
    user.user_lastname()
    user.user_email()
    user.user_mobnumber()
    user.user_password()