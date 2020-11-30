import re


class UserRegistration:
    pattern = '^[A-Z]{1}[a-z]{3,}$'

    # User First Name
    def user_firstname(self):
        while True:
            user_name = input("Enter the User First Name : ")
            result = re.match(UserRegistration.pattern, user_name)
            if result:
                print("Valid Name")
                break
            else:
                print("Invalid Name, Please enter name in proper format")

    # User Last Name
    def user_lastname(self):
        while True:
            user_name = input("Enter the User Last Name : ")
            result = re.match(UserRegistration.pattern, user_name)
            if result:
                print("Valid Name")
                break
            else:
                print("Invalid Name, Please enter Name in proper format")


if __name__ == "__main__":
    user = UserRegistration()
    user.user_firstname()
    user.user_lastname()
