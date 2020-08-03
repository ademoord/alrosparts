# 
#   file: views.py
#	author: andromeda
#   desc: Model parsing and variable retrieval for each URL controller
#
from django.shortcuts 						import render, redirect
from django.http 							import HttpResponse
from .models								import tbProjekte, tbComponent
from django.contrib.auth.forms				import UserCreationForm, AuthenticationForm
from django.contrib.auth 					import logout, authenticate, login
from django.contrib 						import messages
from .forms 								import NewUserForm
from django.contrib.auth.models 			import User



# Create your views here.
def home(request):
	if not request.user.is_authenticated:
	    if request.method == 'POST':
	        form = AuthenticationForm(request=request, data=request.POST)
	        if form.is_valid():
	            username = form.cleaned_data.get('username')
	            password = form.cleaned_data.get('password')
	            user = authenticate(username=username, password=password)
	            if user is not None:
	                login(request, user)
	                messages.info(request, f"Hallo, {user.first_name} {user.last_name}. Welcome to ALROSParts!")
	                return redirect('/') 
	            else:
	                messages.error(request, "Invalid username or password.")
	        else:
	            messages.error(request, "Invalid username or password.")
	    form = AuthenticationForm()
	    return render(request = request,
	                  template_name = "master/login.html",
	                  context={"form":form,
					  	       "title":'Home'})
	return render(request=request,
				  template_name='master/home.html',
				  context={"title":'Home',
				  		   "projekte":tbProjekte.objects.all})
					  

def register(request):
	if request.method == "POST":
		form = NewUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			username = form.cleaned_data.get('username')
			messages.success(request, f"New account created: {username}")
			login(request, user)
			return redirect("master:home")
		else:
			for msg in form.error_messages:
				messages.error(request, f"{msg}: {form.error_messages[msg]}")

			return render(request=request,
			  			  template_name="master/register.html",
			  			  context={"form":form,
				  		   "title":'Register'})

	form = NewUserForm
	return render(request=request,
				  template_name="master/register.html",
				  context={"form":form,
		  	  		   	   "title":'Register'})

def logout_request(request):
	logout(request)
	messages.info(request, "Logged out successfully!")
	return redirect("master:home")


def parts(request):
	return render(request=request,
				  template_name='master/parts.html',
				  context={"title":'Parts',
				  		   "parts":tbComponent.objects.all})

def account(request):
	if request.user.is_authenticated:
		userAcc = request.user
		return render(request=request,
			  template_name='master/account.html',
			  context={"title":userAcc.first_name + "'s Profile",
			  		   "userFullname":userAcc.first_name + " " + userAcc.last_name,
			  		   "userMail":userAcc.email,
			  		   "userStaff":userAcc.is_staff,
			  		   "userLastSeen":userAcc.last_login})
