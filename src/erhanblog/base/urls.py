from django.urls import path
from .views import *

urlpatterns = [
    path('', Index.as_view(), name='index'),
    path('post/<int:pk>/', PostDetail.as_view(), name='post'),
    path('blogs/', Blogs.as_view(), name='blogs'),
    path('create-article/', CreateArticle.as_view(), name='create'),
    path('article-list/', ArticleList.as_view(), name='article-list'),
]