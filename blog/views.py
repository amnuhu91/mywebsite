from django.shortcuts import render
from django.views.generic import TemplateView, CreateView, ListView, UpdateView, DeleteView, DetailView
from blog.models import Blog
from about_me.views import *
#class BlogHome(TemplateView):
class AddBlog(CreateView):
    model = Blog
    success_url ='/blog/add-blog'
    extra_context= ext_context
    fields  = ('title','body','image')


class UpdateBlog(UpdateView):
    model = Blog
    fields =  ('title','body','image')
    success_url ='/blog/add-blog'
    extra_context= ext_context

class ListBlog(ListView):
    model = Blog
  
    extra_context= ext_context
    paginate_by = 5
class BlogView(DetailView):
    model = Blog
    #related_post = Blog.objects.exclude(title=title)
    extra_context= ext_context
    pk_url_kwarg = 'pk'
    slug_url_kwarg = 'title'
