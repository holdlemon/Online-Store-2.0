from django.contrib.auth.forms import UserCreationForm

from catalog.forms import StyleFormMixin
from users.models import User

class UserRegisterForm(StyleFormMixin, UserCreationForm):
    class Meta:
        model = User
        fields = ('email', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["password1"].label = "Пароль"
        self.fields["password2"].label = (
            "Повторите пароль"
        )

        self.fields["password1"].help_text = (
            "- Ваш пароль не должен быть слишком похож на другую личную информацию.<br>"
            "- Ваш пароль должен содержать как минимум 8 символов.<br>"
            "- Ваш пароль не должен быть распространённым.<br>"
            "- Ваш пароль не должен состоять только из цифр."
        )

        self.fields["password2"].help_text = "Введите еще раз свой пароль."