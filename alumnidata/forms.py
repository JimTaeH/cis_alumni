from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import fields, widgets
from alumnidata.models import Profile


# Create your forms here.

class NewUserForm(UserCreationForm):
	email = forms.EmailField(max_length=254, required=True)
	username = forms.CharField(max_length=30, required=True, help_text=None)
	password1 = forms.CharField(max_length=30, min_length=8, required=True, help_text="Maximum is 30 character. Please use lowercase UPPERCASE and 0-9", widget=forms.PasswordInput)
	password2 = forms.CharField(max_length=30, min_length=8, required=True, help_text="Confirm Your Password", widget=forms.PasswordInput)

	class Meta:
		model = User
		fields = ("username", "first_name", "last_name", "email", "password1", "password2")

	def save(self, commit=True):
		user = super(NewUserForm, self).save(commit=False)
		user.email = self.cleaned_data['email']
		if commit:
			user.save()
		return user

class UserForm(forms.ModelForm):
	class Meta:
		model = User
		fields = ('username', 'first_name', 'last_name', 'email')