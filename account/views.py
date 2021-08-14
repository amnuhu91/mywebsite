from django.shortcuts import render
from django.contrib.auth.views import LoginView
from account.forms import UserRegisterForm, Registration
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate, login
from about_me.views import ext_context

# class MyLogin(LoginView):
#     template_name = 'registration/login.html'

def registerUser(request):
    context = {}
    context.update(ext_context)
    if request.user.is_authenticated:
        path = request.get_full_path()
        print(path)
    if request.method=='POST':
        form = Registration(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data['email']
            password = form.cleaned_data['password1']
            obj = authenticate(request,email = email, password = password)
            login(request, obj)
            print(email)
            print(password)
    else:
        form = Registration()
        context['form'] = form
    return render(request,'account/register.html',context)


