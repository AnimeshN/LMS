from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login , logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages


# Create your views here.

def login_user(req):
	if req.method == 'POST':
		uname = req.POST['username']
		passw = req.POST['password']
		user = authenticate(req,username=uname, password=passw)
		if (user is not None) and (uname == 'admin'):
			login(req,user)
			return redirect('ncertuser')
		elif (user is not None) and (uname == 'teacher'):
			login(req,user)
			return redirect('teacheruser')
		elif (user is not None) and (uname == 'district'):
			login(req,user)
			return redirect('districtuser')
		elif (user is not None) and (uname == 'school'):
			login(req,user)
			return redirect('schooluser')	
	return render(req,'lms/login.html',{})


def home(req):
	return render(req,'lms/home.html',{})	

# def ncertAdmin(req):
# 	return render(req,'lms/ncertuser.html',{})

def districtManagement(req):
	return render(req,'lms/dmuser.html',{})

def schoolManagement(req):
	return render(req,'lms/smuser.html',{})

def teacherUser(req):
	return render(req,'lms/teacheruser.html',{})

def logout_user(req):
	logout(req)
	return render(req,'lms/home.html',{})

def ncertAdmin(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            # login(request, user)
            messages.success(request,('You successfully Registered user'))
            return redirect('ncertuser')
    else:
        form = UserCreationForm()
    return render(request, 'lms/ncertuser.html', {'form': form})