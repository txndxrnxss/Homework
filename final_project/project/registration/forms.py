from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm

class LoginForm(forms.Form):

    """
    Класс, представляющий форму для входа пользователя.
    """

    # Создание поля для ввода никнейма пользователя.
    nickname = forms.CharField()

    # Создание поля для ввода пароля пользователя с типом виджета "PasswordInput".
    password = forms.CharField(widget=forms.PasswordInput)


class SignUpForm(UserCreationForm):

    """
    Класс, представляющий форму регистрации нового пользователя.
    """
    
    # Поле для ввода адреса электронной почты, с требованием его заполнения.
    email = forms.EmailField(required=True)

    class Meta:

        # Использование стандартной модели User Django для создания пользователей.
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    # Переопределение метода save() для сохранения адреса электронной почты в модели User.
    def save(self, commit=True):
        user = super(SignUpForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user
