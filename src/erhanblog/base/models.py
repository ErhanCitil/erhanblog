from django.db import models
from django.conf import settings
# Create your models here.
class Author(models.Model):
    name = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return self.name.username

class Article(models.Model):
    title = models.CharField(max_length = 1000)
    content = models.TextField()
    date_posted = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='blogimages/', blank=True, null=True)
    author = models.ManyToManyField(Author, related_name="articles")

    def __str__(self):
        return self.title
    
    def loop_authors(self):
            return ", ".join([str(p).capitalize() for p in self.author.all()])