from django.urls import path, include
# from account.views import MyLogin
from django.contrib.auth import views as auth_views
from myaccount.views import registerUser
#app_name='account'
urlpatterns = [

path("", include("django.contrib.auth.urls")),
path("accounts/login", auth_views.LoginView.as_view(template_name = 'registration/login.html'), name='login'),
path("accounts/logout", auth_views.LogoutView.as_view(), name='logout'),
path('register/',registerUser, name = 'register')
]
