from django import forms

class LoginForm(forms.Form):
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'placeholder': 'Enter your email', 'class': 'form-control'}),
        label="Email address"
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': '***************', 'class': 'form-control'}),
        label="Password"
    )

