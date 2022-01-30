from django import forms


class UserRegistrationForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Eenter username'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Eenter Emali'}))
    password = forms.CharField(widget=forms.PasswordInput({'class': 'form-control'}))
