from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from api import views


urlpatterns = [
    path('contacts/', views.contact_list),
    path('contact/<int:pk>/', views.contact_detail),
]



urlpatterns = format_suffix_patterns(urlpatterns)