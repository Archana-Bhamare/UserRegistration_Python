import re


class UserRegistration:
<<<<<<< HEAD
<<<<<<< HEAD
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
=======
    NAME_REGEX = '^[A-Z]{1}[a-z]{3,}$'
    EMAIL_REGEX = '^[a-zA-Z0-9]+([.+-_][a-z-A-Z0-9]+)*@[a-zA-Z0-9]+.[a-z]{2,3}([.][a-z]{2})*$'
    MOBILE_REGEX = '^[91]{2}[ ]?[0-9]{10}$'
    PASSWD_REGEX = '^[a-zA-Z]{8,}$'
>>>>>>> UC5-PasswordWith_Min_8_Characters
=======
    NAME_REGEX = '^[A-Z]{1}[a-z]{3,}$'
    EMAIL_REGEX = '^[a-zA-Z0-9]+([.+-_][a-z-A-Z0-9]+)*@[a-zA-Z0-9]+.[a-z]{2,3}([.][a-z]{2})*$'
    MOBILE_REGEX = '^[91]{2}[ ]?[0-9]{10}$'
    PASSWD_REGEX = '^(?=.*[A-Z])[a-zA-Z0-9]{8,}$'
>>>>>>> UC6-PasswordWith_1UpperCaseLetter

    # User First Name
    def user_firstname(self):
        user_name = input("Enter the User First Name : ")
        result = re.match(UserRegistration.NAME_REGEX, user_name)
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> UC3_User_Email
=======
>>>>>>> UC5-PasswordWith_Min_8_Characters
=======
>>>>>>> UC6-PasswordWith_1UpperCaseLetter
        if result:
            print("Valid Name")
        else:
            print("Invalid Name, Please enter name in proper format")

<<<<<<< HEAD
<<<<<<< HEAD
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
=======
>>>>>>> UC5-PasswordWith_Min_8_Characters
=======
>>>>>>> UC6-PasswordWith_1UpperCaseLetter
    # User Last Name
    def user_lastname(self):
        user_name = input("Enter the User Last Name : ")
        result = re.match(UserRegistration.NAME_REGEX, user_name)
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> UC3_User_Email
=======
>>>>>>> UC5-PasswordWith_Min_8_Characters
=======
>>>>>>> UC6-PasswordWith_1UpperCaseLetter
        if result:
            print("Valid Name")
        else:
            print("Invalid Name, Please enter Name in proper format")

<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
=======
>>>>>>> UC5-PasswordWith_Min_8_Characters
=======
>>>>>>> UC6-PasswordWith_1UpperCaseLetter
    # User Email
    def user_email(self):
        user_email = input("Enter the Email Id : ")
        result = re.match(UserRegistration.EMAIL_REGEX, user_email)
        if result:
            print("Valid Email Id")
        else:
<<<<<<< HEAD
<<<<<<< HEAD
            print("Invalid Emaild Id")

>>>>>>> UC3_User_Email
=======
=======
>>>>>>> UC6-PasswordWith_1UpperCaseLetter
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

<<<<<<< HEAD
>>>>>>> UC5-PasswordWith_Min_8_Characters
=======
>>>>>>> UC6-PasswordWith_1UpperCaseLetter

if __name__ == "__main__":
    user = UserRegistration()
    user.user_firstname()
    user.user_lastname()
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> UC2-Last_Name
=======
    user.user_email()
>>>>>>> UC3_User_Email
=======
    user.user_email()
    user.user_mobnumber()
    user.user_password()
>>>>>>> UC5-PasswordWith_Min_8_Characters
=======
    user.user_email()
    user.user_mobnumber()
    user.user_password()
>>>>>>> UC6-PasswordWith_1UpperCaseLetter
