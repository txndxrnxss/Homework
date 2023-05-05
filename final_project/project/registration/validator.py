from re import match

class InvalidLogin(Exception):
    pass
     

class InvalidPassword(Exception):
    pass

class InvalidEmail(Exception):
    pass


class Validator():

    from string import ascii_lowercase, ascii_uppercase, punctuation

    def __init__(self, login: str, password: str, email: str):
        self.login = login
        self.password = password
        self.email = email
        self.pattern_login = r'^[A-Za-z0-9]{6,10}$'
        self.pattern_password = r'^(?=.*[A-Za-z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!%*#?&]{8,}$'
        self.pattern_email = r'^\S+@\S+\.\S+$'

    def validate_login(self) -> bool:
        if not match(self.pattern_login, self.login):
            raise InvalidLogin('Ошибка! Неверно введен Login.')

    def validate_password(self) -> bool:
        if not match(self.pattern_password, self.password):
            raise InvalidPassword('Ошибка! Пароль не соответствует следующим требованиям: не менее 8 символов, буквы в верхнем и нижнем регистре, не менее одного специального символа.')

    def validate_email(self) -> bool:
        if not match(self.pattern_email, self.email):
            raise InvalidEmail('Ошибка! Неверно введен Email.')


    def validate(self) -> bool:
        try:
            self.validate_login()
            self.validate_password()
            self.validate_email()
        except (InvalidLogin, InvalidPassword, InvalidEmail) as valid_error:
             
            return valid_error
        else:
            return True