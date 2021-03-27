from django import forms

class UserForm(forms.Form):
    username = forms.CharField(label='', max_length=100,
        widget= forms.TextInput(attrs={'placeholder':'Username'})
    )
    email = forms.CharField(label='', max_length=100,
        widget= forms.TextInput(attrs={'placeholder':'Email'})
    )
    first_name = forms.CharField(label='', max_length=100,
        widget= forms.TextInput(attrs={'placeholder':'First Name'})
    )
    last_name = forms.CharField(label='', max_length=100,
        widget= forms.TextInput(attrs={'placeholder':'Last Name'})
    )
    password = forms.CharField(
        label='', 
        max_length=100,
        widget= forms.PasswordInput(attrs={'placeholder':'Password'})
    )
    bio = forms.CharField(label='', widget=forms.Textarea(attrs={'placeholder':'Bio'}))

class LoginForm(forms.Form):
    username = forms.CharField(label='', max_length=100,
        widget= forms.TextInput(attrs={'placeholder':'Username'})
    )
    password = forms.CharField(
        label='', 
        max_length=100,
        widget= forms.PasswordInput(attrs={'placeholder':'Password'})
    )
