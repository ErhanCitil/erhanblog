from django.db import models
from django.conf import settings
# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL,  null = True, default=1)
    image = models.ImageField(upload_to='blogimages/', blank=True, null=True)

    def __str__(self):
        return self.title