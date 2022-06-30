from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from api import views


urlpatterns = [
    path('contacts/', views.contact_list),
    path('contact/<int:pk>/', views.contact_detail),
    path('back-end/', views.BackendCourseList.as_view()),
    path('back-end/<int:pk>/', views.BackendCourseDetail.as_view()),
    path('posts/', views.PostList.as_view()),
    path('post/<int:pk>/', views.PostDetail.as_view())
]



urlpatterns = format_suffix_patterns(urlpatterns)