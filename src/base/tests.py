from django.test import TestCase
from .models import *
from django.urls import reverse_lazy
from .views import *
from django.urls import reverse

from erhanblog.accounts.models import User
# Create your tests here.
class PostTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='test', password='test')
        self.post = Post.objects.create(title='test', content='test', author=self.user)
        self.post.save()

    def test_title(self):
        self.assertEqual(self.post.title, 'test')

    def test_content(self):
        self.assertEqual(self.post.content, 'test')
    
    def test_author(self):
        self.assertEqual(self.post.author, self.user)
    

class PostTestViews(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='test', password='test')
        self.post = Post.objects.create(title='test', content='test', author=self.user)

    def test_index(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')

    def test_post_view(self):
        response = self.client.get(reverse('post', args=[self.post.pk]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog.html')

    def test_blogs(self):
        response = self.client.get(reverse('blogs'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'blogs.html')

class ImageFieldTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='test', password='test')
        self.post = Post.objects.create(title='test', content='test', author=self.user, image='blogimages/1.jpg')

    def test_image(self):
        self.assertEqual(self.post.image, 'blogimages/1.jpg')