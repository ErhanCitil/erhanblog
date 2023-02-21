from django.shortcuts import render
from django.views import generic
from .models import *
from django.urls import reverse_lazy
from erhanblog.form.forms import CreateArticleForm

from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.
class Index(generic.ListView):
    template_name = 'base/index.html'
    context_object_name = 'posts'
    model = Article

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['posts'] = Article.objects.all().order_by('?')[:3]
        return context

class PostDetail(generic.DetailView):
    template_name = 'base/blog.html'
    model = Article
    context_object_name = 'post'

class Blogs(generic.ListView):
    template_name = 'base/blogs.html'
    context_object_name = 'posts'
    model = Article

class CreateArticle(LoginRequiredMixin, generic.CreateView):
    template_name = 'base/create_article.html'
    model = Article
    form_class = CreateArticleForm
    success_url = reverse_lazy('index')