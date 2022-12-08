from django.test import TestCase
from .models import *
from .forms import *
from .views import *
from django.urls import reverse
# Create your tests here.
class ContactModelTest(TestCase):
    def setUp(self):
        self.contact = ContactModel.objects.create(
            name='test', email='test@gmail.com', message='Test message')
    def test_contact_model(self):
        self.assertEqual(self.contact.name, self.contact.name)
        self.assertEqual(self.contact.email, self.contact.email)
        self.assertEqual(self.contact.message, self.contact.message)

class ContactViewTest(TestCase):
    def setUp(self):
        self.contact1 = ContactModel.objects.create(name='erhan', email='erhancitil@test.nl', message='test message3')
        self.contact2 = ContactModel.objects.create(name='alex', email='alex123@live.nl', message='test message2')
        self.contact3 = ContactModel.objects.create(name='test', email='test@gmail.nl', message='test message1')

    def test_contact_view(self):
        url = reverse('contact')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'contact.html')
