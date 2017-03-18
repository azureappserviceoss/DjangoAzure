#importing forms
from django import forms 

#creating our forms
class SignupForm(forms.Form):
	#django gives a number of predefined fields
	#CharField and EmailField are only two of them
	#go through the official docs for more field details
	name = forms.CharField(label='Enter your name', max_length=100)
	email = forms.EmailField(label='Enter your favorite Pokemon', max_length=100)