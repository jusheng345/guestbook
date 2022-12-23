from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from .models import Message
from django.urls import reverse_lazy

# Create your views here.

class MessageList(ListView):
    model = Message
    odering = ['-id']

class MessageDetail(DetailView):
    model = Message

class MessageCreate(CreateView):
    model = Message
    fields = ['user', 'subject', 'content']
    success_url = reverse_lazy('msg_list')

