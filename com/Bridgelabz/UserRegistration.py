import re


class UserRegistration:
    pattern = '^[A-Z]{1}[a-z]{3,}$'

    # User First Name
    def user_name(self):
        while True:
            user_name = input("Enter the User Name : ")
            result = re.match(UserRegistration.pattern, user_name)
            if result:
                print("Valid Name")
                break
            else:
                print("Invalid Name, Please enter name in proper format")


if __name__ == "__main__":
    user = UserRegistration()
    user.user_name()
