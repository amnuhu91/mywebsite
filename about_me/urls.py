from django.urls import path
from about_me.views import home_view, email_contact_view, phone_contact_view, FrontCourseDetail
app_name = 'about_me'
urlpatterns = [
	path('',home_view, name='home'),
	# path('footer',footer, name='home'),
	path('email/',email_contact_view, name='email'),
	path('phone/',phone_contact_view, name='phone'),
	path('course/<int:pk>/',FrontCourseDetail.as_view(), name='course-detail'),

]
