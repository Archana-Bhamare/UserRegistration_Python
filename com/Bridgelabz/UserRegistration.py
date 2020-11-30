import re


class UserRegistration:
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
        if result:
            print("Valid Name")
        else:
            print("Invalid Name, Please enter name in proper format")

<<<<<<< HEAD

if __name__ == "__main__":
    user = UserRegistration()
    user.user_name()
=======
    # User Last Name
    def user_lastname(self):
        user_name = input("Enter the User Last Name : ")
        result = re.match(UserRegistration.pattern, user_name)
        if result:
            print("Valid Name")
        else:
            print("Invalid Name, Please enter Name in proper format")


if __name__ == "__main__":
    user = UserRegistration()
    user.user_firstname()
    user.user_lastname()
>>>>>>> UC2-Last_Name
