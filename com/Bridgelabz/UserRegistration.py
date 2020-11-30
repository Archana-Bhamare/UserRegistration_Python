import re


class UserRegistration:
    NAME_REGEX = '^[A-Z]{1}[a-z]{3,}$'

    # User First Name
    def user_name(self):
        """
        Taking the First Name from user and match it with respective regex pattern
        """
        while True:
            user_name = input("Enter the User Name : ")
            if re.fullmatch(UserRegistration.NAME_REGEX, user_name):
                print("Valid Name")
                break
            else:
                print("Invalid Name, Please enter name in proper format")


if __name__ == "__main__":
    user = UserRegistration()
    user.user_name()
