from django.shortcuts import render

from .forms import SignupForm
# Create your views here.

def signupform(request):
	#if form is submitted
	if request.method == 'POST':
		#will handle the request later
		form = SignupForm(request.POST)

		#checking the form is valid or not 
		if form.is_valid():
			#if valid rendering new view with values
			#the form values contains in cleaned_data dictionary
			return render(request, 'result.html', {
					'name': form.cleaned_data['name'],
					'email': form.cleaned_data['email'],
				})

	else:
		#creating a new form
		form = SignupForm()

	#returning form 
	return render(request, 'signupform.html', {'form':form})