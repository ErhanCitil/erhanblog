from django.shortcuts import render
from django.views import generic
from .models import *
from django.urls import reverse_lazy
# Create your views here.
class Index(generic.ListView):
    template_name = 'index.html'
    context_object_name = 'posts'
    model = Article

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['posts'] = Article.objects.all().order_by('?')[:3]
        return context

class PostDetail(generic.DetailView):
    template_name = 'blog.html'
    model = Article
    context_object_name = 'post'

class Blogs(generic.ListView):
    template_name = 'blogs.html'
    context_object_name = 'posts'
    model = Article