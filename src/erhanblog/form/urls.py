from django.urls import path
from .views import *

urlpatterns = [
        path('contact/', Contact.as_view(), name='contact'),
]