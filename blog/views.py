from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from django.contrib.postgres.search import (
    SearchVector, SearchQuery, SearchRank
)
from django.http import HttpResponseRedirect, HttpResponse
from django.views.generic.edit import FormMixin, FormView
from django.core.mail import send_mail
from django.db.models import Count
from taggit.models import Tag

from .models import Post, Comment
from .forms import CommentForm, EmailPostForm, PostBlog
from django.views.generic import TemplateView, CreateView
from blog.models import Post

from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from slugify import slugify
import requests as rq

class SuperUserRequiredMixin(LoginRequiredMixin, UserPassesTestMixin):

    def test_func(self):
        return self.request.user.is_superuser
class AddBlog(SuperUserRequiredMixin, CreateView):
    model = Post
    success_url ='/blog/'
    fields  = ('title','body','image','status','tags')

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.author = self.request.user
        #self.object.slug = self.request.title
        self.object.save()
        form.save_m2m()
        return HttpResponseRedirect(self.get_success_url())



class PostListView(ListView):
    paginate_by = 5
    template_name = 'blog/post-list.html'

    def dispatch(self, request, *args, **kwargs):
        #print(request.path)
        return super(PostListView,self).dispatch(request, *args, **kwargs)

    def get_queryset(self, **kwargs):
        queryset = Post.published.all()
        tag_slug = self.kwargs.get('tag_slug')
        query = self.request.GET.get('query')
        category = self.kwargs.get('category')
        print(category)
        if tag_slug:
            tag = get_object_or_404(Tag, slug=tag_slug)
            queryset = queryset.filter(tags__in=[tag])
        if query:
            search_vector = SearchVector('title', weight='A') +\
                SearchVector('body', weight='B')
            search_query = SearchQuery(query)

            queryset = Post.published.annotate(
                rank=SearchRank(search_vector, search_query)
            ).filter(rank__gte=0.3).order_by('-rank')
        if category:
            queryset = Post.objects.filter(category__icontains=category)
            #print(queryset)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        #category = self.kwargs.get('category')
        context["tag"] = self.kwargs.get('tag_slug')
        context["query"] = self.request.GET.get('query')
        context['url'] = self.kwargs.get('category')
        return context


class PostDetailView(FormMixin, DetailView):
    template_name = 'blog/post-detail.html'
    form_class = CommentForm

    def get_object(self):
        obj = get_object_or_404(Post, status='published',
                                slug=self.kwargs.get('slug'),
                                publish__year=self.kwargs.get('year'),
                                publish__month=self.kwargs.get('month'),
                                publish__day=self.kwargs.get('day')
                                )
        return obj

    def get_success_url(self):
        return self.get_object().get_absolute_url()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        post = self.get_object()

        post_tags_ids = post.tags.values_list('id', flat=True)
        similar_posts = Post.published.filter(tags__in=post_tags_ids)\
            .exclude(id=post.id)
        similar_posts = similar_posts.annotate(same_tags=Count('tags'))\
            .order_by('-same_tags', '-publish')[:4]

        comments = Comment.objects.filter(post=post, active=True)
        context["similar_posts"] = similar_posts
        context['comments'] = comments
        context['form'] = self.get_form()
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form()

        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = self.get_object()
            comment.save()
            return self.form_valid(form)
        else:
            print("Invalid form")
            return self.form_invalid(form)


class PostShareView(FormView):
    form_class = EmailPostForm
    template_name = 'blog/post-share.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["post"] = get_object_or_404(
            Post, id=self.kwargs.get('post_id'))
        context["sent"] = False
        return context

    def form_valid(self, form):
        context = self.get_context_data()
        # Send Email
        cd = form.cleaned_data
        post = context['post']
        post_url = self.request.build_absolute_uri(
            post.get_absolute_url()
        )
        subject = f"{cd['name']} recommends you read {post.title}"
        message = f"Read {post.title} at {post_url}\n\n" \
            f"{cd['name']}\'s comments: {cd['comments']}"
        send_mail(subject, message, 'admin@myblog.com', [cd['to']])

        context['sent'] = True
        context['form'] = form
        return self.render_to_response(context)


def get_news(request,category='business',country='ng'):
    country = country
    category = category
    data = ''
    api_key = "afe93d1a9da34815947707f91bef5284"
    url = f"https://newsapi.org/v2/top-headlines?country={country}&category={category}&apiKey={api_key}"
    
    
    
    try:

        response = rq.get(url, timeout=5)
    except Exception as e:
        #raise e
        print("request timeout")
        data = 'request timeout'
    else:
        print("we get news from api")
        print(url)
        news = response.json()
        print(news["articles"][:5])
        print('*'*20)
        print(news["articles"][0]["title"])
        data = "yes there is a news"

        return render(request,'blog/news.htm', {"data":data,"news":news["articles"]})
    return HttpResponse("request timeout")

