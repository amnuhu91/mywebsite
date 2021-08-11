from django.shortcuts import render
from django.contrib.auth.views import LoginView
from account.forms import UserRegisterForm
from django.contrib.auth import login, authenticate
# Create your views here

# class MyLogin(LoginView):
#     template_name = 'registration/login.html'

def registerUser(request):
    
    if request.method=='POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            user = authenticate(email=email, password=password)
    else:
        form = UserRegisterForm()
    return render(request,'account/register.html',{'form':form})


