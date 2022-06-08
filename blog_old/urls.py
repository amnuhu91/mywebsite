from django.urls import path
from django.views.generic import TemplateView
from about_me.models import (EmailContact, PhoneContact, Myself,
								BackEndCourse, FrontEndCourse,
								Learn,UsefulLinks,FrontEndTopics
							)
from blog.views import (AddBlog, UpdateBlog, ListBlog, BlogView, DeleteBlog)
from blog.models import Blog
blogs = Blog.objects.all()

context ={}
learn = Learn.objects.all()
links = UsefulLinks.objects.all()
context['learn']= learn
context['links']= links
context['blogs'] = blogs

app_name='blog'
urlpatterns = [


    path('', ListBlog.as_view(), name='blog'),
    path('my-blog/', TemplateView.as_view(template_name='blog/home.html', extra_context=context), name='my-blog'),
    path('add-blog/', AddBlog.as_view(), name='add-blog'),
    path('update-blog/<int:pk>', UpdateBlog.as_view(pk_url_kwarg = 'pk'), name='update-blog'),
    path('read/<int:pk>/<str:title>', BlogView.as_view(), name='read'),
    path('delete/<int:pk>/<str:title>', DeleteBlog.as_view(), name='delete'),
]