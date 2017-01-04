from login.models import UserProfile
from django.contrib.auth.models import User
from django import forms

EMPTY_ITEM_ERROR = "This field is required"

class LoginForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)
        self.fields['password'].widget.attrs['class'] = 'form-control'
        self.fields['password'].widget.attrs['placeholder'] = 'Password'

    class Meta:
        model = User
        fields = ('username', 'password')
        widgets = {
            'username': forms.fields.TextInput(attrs={
                'id':'username',
                'placeholder': 'User name',
                'class': 'form-control',
            }),

        }
        error_messages = {
            'text': {'required': EMPTY_ITEM_ERROR}
        }

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    def __init__(self, *args, **kwargs):
        super(UserForm, self).__init__(*args, **kwargs)
        self.fields['email'].widget.attrs['class'] = 'form-control'
        self.fields['password'].widget.attrs['class'] = 'form-control'
        self.fields['username'].widget.attrs['class'] = 'form-control'

    class Meta:
        model = User
        fields = ('email', 'username', 'password')

class UserProfileForm(forms.ModelForm):

    class Meta:
        model = UserProfile
        fields = ('picture',)
