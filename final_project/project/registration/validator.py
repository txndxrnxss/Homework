"""Создание класса Validator, предназначенного для проверки корректности ввода данных."""

from re import match  # импорт модуля re для регулярных выражений

# создаем класс исключения "InvalidLogin"
class InvalidLogin(Exception):  
    pass

# создаем класс исключения "InvalidPassword"    
class InvalidPassword(Exception):  
    pass

# создаем класс исключения "InvalidEmail"
class InvalidEmail(Exception):  
    pass


class Validator():
    from string import ascii_lowercase, ascii_uppercase, punctuation

    def __init__(self, login: str, password: str, email: str):  
        self.login = login
        self.password = password
        self.email = email

        # регулярные выражения для проверки логина, пароля, email.
        self.pattern_login = r'^[A-Za-z0-9]{6,10}$' 
        self.pattern_password = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[a-zA-Z\d]{8,}$' 
        self.pattern_email = r'^\S+@\S+\.\S+$'  


    """
    Метод, который проверяет логин, если логин не соответствует регулярному выражению, 
    то вызываем исключение "InvalidLogin" и соответствующее сообщение.
    """
    def validate_login(self) -> bool:
        if not match(self.pattern_login, self.login):
            raise InvalidLogin('Ошибка! Неверно введен Login.')


    """
    Метод, который проверяет пароль, если пароль не соответствует регулярному выражению, 
    то вызываем исключение "InvalidPassword" и соответствующее сообщение.
    """
    def validate_password(self) -> bool:  
        if not match(self.pattern_password, self.password):  
            raise InvalidPassword('Ошибка! Пароль не соответствует следующим требованиям: не менее 8 символов, обязательное наличие букв латинского алфавита в верхнем и нижнем регистре, а также цифр.')


    """
    Метод, который проверяет email, если email не соответствует регулярному выражению, 
    то вызываем исключение "InvalidEmail" и соответствующее сообщение.
    """
    def validate_email(self) -> bool:
        if not match(self.pattern_email, self.email): 
            raise InvalidEmail('Ошибка! Неверно введен Email.')  


    def validate(self) -> bool:  # метод, который запускает все три проверки
        try:
            self.validate_login()       # проверка логина с помощью метода validate_login()
            self.validate_password()    # проверка пароля с помощью метода validate_password()
            self.validate_email()       # проверка email с помощью метода validate_email()

        # если какое-то из исключений было вызвано, возвращаем текст ошибки
        except (InvalidLogin, InvalidPassword, InvalidEmail) as valid_error:
            return valid_error
        
        # если никаких ошибок не было вызвано, возвращаем True
        else:
            return True  
