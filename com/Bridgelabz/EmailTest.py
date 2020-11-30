import re


class EmailTest:
    REGEX = '^[a-zA-Z0-9]+([.+-_][a-z-A-Z0-9]+)*@[a-zA-Z]+.[a-z]{2,3}([.][a-z]{2})*$'
    # Valid EMail Ids
    valid_email = {
        "abc@yahoo.com",
        "abc-100@yahoo.com",
        "abc.100@yahoo.com",
        "abc111@abc.com",
        "abc-100@abc.net",
        "abc.100@abc.com.au",
        "abc@1.com",
        "abc@gmail.com.com",
        "abc+100@gmail.com",
    }
    # Invalid Email Ids
    invalid_email = {
        "abc@.com.my",
        "abc123@gmail.a",
        "abc123@.com",
        "abc123@.com.com",
        ".abc@abc.com",
        "abc()*@gmail.com",
        "abc..2002@gmail.com",
        "abc.@gmail.com",
        "abc@gmail.com.1a",
    }

    # Validate EMails
    def email_validator(self, request):
        return re.match(EmailTest.REGEX, request)


if __name__ == "__main__":
    email = EmailTest()
    print("For valid Email Ids")
    for i in EmailTest.valid_email:
        valid = bool(email.email_validator(i))
        print("Email id : " + i + " is valid? : \t" + str(valid))
    print("For Invalid Email Ids")
    for i in EmailTest.invalid_email:
        valid = bool(email.email_validator(i))
        print("Email id : " + i + " is valid? : \t" + str(valid))
