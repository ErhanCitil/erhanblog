from django.test import TestCase
from .models import *
from django.urls import reverse_lazy
from .views import *
from django.urls import reverse
from django.test import Client
from django.contrib.auth.models import User
# Create your tests here.
class PostTest(TestCase):
    def setUp(self):
        self.post1 = Post.objects.create(title='test', content='test content')
        self.post2 = Post.objects.create(title='test2', content='test content2')
        self.post3 = Post.objects.create(title='test3', content='test content3')

    def test_post_exist(self):
        self.assertEqual(self.post1.title, self.post1.title)
        self.assertEqual(self.post1.content, self.post1.content)
        self.assertEqual(self.post2.title, self.post2.title)
        self.assertEqual(self.post2.content, self.post2.content)
        self.assertEqual(self.post3.title, self.post3.title)
        self.assertEqual(self.post3.content, self.post3.content)

class PostTestView(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password = '12345')
        self.post1 = Post.objects.create(title='test', content='test content')
        self.post2 = Post.objects.create(title='test2', content='test content2')
        self.post3 = Post.objects.create(title='test3', content='test content3')

    def test_post_view(self):
        url = reverse('index')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')

    def test_post_detail_view(self):
        url = reverse('post', args=[self.post1.pk])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog.html')

    def test_post_blogs_view(self):
        url = reverse('blogs')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'blogs.html')

class ImageFieldTest(TestCase):
    def test_image_field(self):
        post = Post.objects.create(title='test', content='test content')
        self.assertFalse(post.image)

    def test_image_field_upload(self):
        post = Post.objects.create(title='test', content='test content')
        post.image = 'test.jpg'
        self.assertEqual(post.image, 'test.jpg')