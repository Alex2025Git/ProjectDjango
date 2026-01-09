
from django.contrib.auth.forms import UserCreationForm

from users.models import User
from django.forms import ModelForm, BooleanField


class StyleFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for fild_name, fild in self.fields.items():
            if isinstance(fild, BooleanField):
                fild.widget.attrs['class'] = 'form-check-input'
            else:
                fild.widget.attrs['class'] = 'form-control'


class UserRegisterForm(StyleFormMixin, UserCreationForm):
    class Meta:
        model = User
        fields = ('email', 'password1', 'password2')

class ProfileForm(StyleFormMixin, ModelForm):
    class Meta:
        model = User
        fields = ('nik_name','email','phone_number','avatar')