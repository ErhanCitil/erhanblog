from django.test import TestCase
from .models import *
from .views import *
from erhanblog.accounts.models import User
from django.urls import reverse
# Create your tests here.
class ModelsTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='root', password='test')
        self.author = Author.objects.create(author_name=self.user)
        self.post = Article.objects.create(title='test', content='test')
        self.post.author.set([self.author])
        self.post.save()

    def test_author(self):
        self.assertEqual(self.author.author_name.username, 'root')

    def test_title(self):
        self.assertEqual(self.post.title, 'test')

    def test_content(self):
        self.assertEqual(self.post.content, 'test')

    def test_author_name(self):
        self.assertEqual(self.post.loop_authors(), 'Root')

class ViewsTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='root', password='test')
        self.author = Author.objects.create(author_name=self.user)
        self.post = Article.objects.create(title='test', content='test')
        self.post.author.set([self.author])
        self.post.save()

    def test_index(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'index.html')
        self.assertEqual(response.status_code, 200)

    def test_blogs(self):
        response = self.client.get('/blogs/')
        self.assertTemplateUsed(response, 'blogs.html')
        self.assertEqual(response.status_code, 200)

    def test_post(self):
        url = reverse('post', kwargs={'pk': self.post.pk})
        response = self.client.get(url)
        self.assertTemplateUsed(response, 'blog.html')
        self.assertEqual(response.status_code, 200)
        