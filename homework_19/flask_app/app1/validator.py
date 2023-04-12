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
        self.pattern_email = r'^[\w.-]+@[\w.-]+\.(\S{2}$)'

    def validate_login(self) -> bool:
        if not match(self.pattern_login, self.login):
            raise InvalidLogin('Длина логина менее 6 знаков!')

    def validate_password(self) -> bool:
        if not match(self.pattern_password, self.password):
            raise InvalidPassword('Ошибка. Пароль не соответствует следующим требованиям: не менее 8 символов, буквы в верхнем и нижнем регистре, не менее одного специального символа')

    def validate_email(self) -> bool:
        if not match(self.pattern_email, self.email):
            raise InvalidEmail('Ошибка. Email не соответствует следующим требованиям:  присутствует символ @, оканчивается . и 2 символами (.by)')


    def validate(self) -> bool:
        try:
            self.validate_login()
            self.validate_password()
            self.validate_email()
        except (InvalidLogin, InvalidPassword, InvalidEmail) as valid_error:
             
            return valid_error
        else:
            return True


# print(Validator('xxxxxx','xX0xd1*sfdfhfdhs','xsf@m.by').validate())
