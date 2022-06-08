from django.shortcuts import render
from django.views.generic import TemplateView, CreateView, ListView, UpdateView, DeleteView, DetailView
from django.db.models import Q
from blog.models import Blog
from about_me.views import *
from django.contrib.auth.mixins import LoginRequiredMixin
#class BlogHome(TemplateView):

from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

class SuperUserRequiredMixin(LoginRequiredMixin, UserPassesTestMixin):

    def test_func(self):
        return self.request.user.is_superuser
class AddBlog(SuperUserRequiredMixin, CreateView):
    model = Blog
    success_url ='/blog/add-blog'
    extra_context= ext_context
    fields  = ('title','body','image')


class UpdateBlog(SuperUserRequiredMixin,UpdateView):
    model = Blog
    fields =  ('title','body','image')
    success_url ='/blog/add-blog'
    extra_context= ext_context

class ListBlog(ListView):
    model = Blog
    
    extra_context= ext_context
    paginate_by = 5
    def dispatch(self, request, *args, **kwargs):
    # Try to dispatch to the right method; if a method doesn't exist,
    # defer to the error handler. Also defer to the error handler if the
    # request method isn't on the approved list.
        print(request.path)
        if request.method.lower() in self.http_method_names:
            handler = getattr(self, request.method.lower(), self.http_method_not_allowed)
        else:
            handler = self.http_method_not_allowed
        return handler(request, *args, **kwargs)
class BlogView(DetailView):
    model = Blog
    #pk=request.GET.get('pk')
    related_post = Blog.objects.exclude(pk=1)
    ext_context['related'] = related_post
    extra_context= ext_context
    pk_url_kwarg = 'pk'
    slug_url_kwarg = 'title'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['additional_post'] = Blog.objects.exclude(pk=self.kwargs.get('pk'))[:5]
        rel = self.kwargs.get('title').split("-")
        print(len(rel))
        print("rel 0",rel[0])
        if len(rel) >=2:
            for i in rel:
                print(i)
                pass
        context['related']  = Blog.objects.filter(Q(title__icontains=rel[0]) | Q(title__icontains=rel[1])).filter(~Q(pk=self.kwargs.get('pk')))
        return context


class DeleteBlog(SuperUserRequiredMixin, DeleteView):
    model = Blog
    pk_url_kwarg = 'pk'
    slug_url_kwarg = 'slug'
    template_name_suffix = '_delete'
    success_url ="/blog/"