from django.shortcuts import render
from django.views.generic import ListView , CreateView
from .models import Model
from django.urls import reverse_lazy

# Create your views here.
class List(ListView):
    template_name = "list.html"
    model = Model
    context_object_name = 'list'

class Create(CreateView):
    template_name = "create.html"
    model = Model
    fields = ("title" , "contents" )
    success_url = reverse_lazy("list")