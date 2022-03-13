from django.urls import path
from django.views.generic import TemplateView
from about_me.views import home_view, email_contact_view, phone_contact_view, FrontCourseDetail,search_topic
app_name = 'about_me'
urlpatterns = [
	path('',home_view, name='home'),
	# path('footer',footer, name='home'),
	path('email/',email_contact_view, name='email'),
	path('phone/',phone_contact_view, name='phone'),
	path('course/<int:pk>/',FrontCourseDetail.as_view(), name='course-detail_old'),
	path('search/<int:pk>/',search_topic, name='course-detail'),
	path('organizational-chart/',TemplateView.as_view(template_name='about_me/orgchart.html'), name='orgchart'),


]
