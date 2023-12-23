from django import forms
from django.contrib.auth.forms import UserCreationForm

class UserRegisterForm(UserCreationForm):
    username = forms.CharField(label='Login:', required=True)
    first_name = forms.CharField(label='First name:', required=True)
    last_name = forms.CharField(label='Last name:', required=True)
    email = forms.EmailField(required=True)

    error_messages = {
        'duplicate_username': "This first name is already taken.",
        'password_mismatch': "Passwords are different.",
    }

    field_order = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        super(UserRegisterForm, self).__init__(*args, **kwargs)

        self.fields['email'].help_text = 'Input your e-mail'
        self.fields['username'].help_text = 'Username can include letters and @ . + - _'
        self.fields['password1'].help_text = """
        Password can't be your first name.

        Password has to include 8 chars and more.

        Password can't be very simple.

        Password can't include only numbers.
        """
        self.fields['password2'].help_text = 'Write your password again, please.'
        self.fields['username'].widget.attrs['maxlength'] = 20
        # self.fields['username'].widget.attrs['class'] = 'w-100'