from django.shortcuts import render
from django.views import generic
from .forms import ContactForm
from django.urls import reverse_lazy
from .models import *
# Create your views here.
class Contact(generic.FormView):
    template_name = 'form/contact.html'
    form_class = ContactForm
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)