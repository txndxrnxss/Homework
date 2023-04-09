import string

class InvalidLogin(Exception):
    ...
class InvalidEmail(Exception):
    ...
class InvalidPassword(Exception):
    ...
class ValidationError(Exception):
    ...

class Validator:

    @staticmethod
    def validate(user_data: tuple) -> bool:
        try:
            Validator.validate_email(user_data[2])
            Validator.validate_password(user_data[1])
            Validator.validate_login(user_data[0])
        except (InvalidPassword, InvalidEmail, InvalidLogin):
            raise ValidationError
        else:
            raise True

    @staticmethod
    def validate_login(login: str) -> bool:
        if len(login) >= 6:
            return True
        else: 
            raise InvalidLogin

    @staticmethod
    def validate_email(email: str) -> bool:
        if '@' in email and email[-3] == '.' and email[-3:].isalpha():
            return True
        else:
            raise InvalidEmail

    @staticmethod
    def validate_password(password: str) -> bool:
        if (len(password) >= 8 and 
            len([x for x in password if x in string.ascii_uppercase]) > 0 and
            len([x for x in password if x in string.ascii_lowercase]) > 0 and
            len([x for x in password if x in string.punctuation])) > 0:
            return True
        else:
            raise InvalidPassword