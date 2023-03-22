from django.shortcuts import render
from django.views.generic import View,CreateView,FormView,TemplateView,ListView
from django.urls import reverse_lazy
from stack.forms import QuestionForm
from stack.models import Questions

# Create your views here.

# class IndexView(TemplateView):
#     template_name="index.html"

class IndexView(CreateView,ListView):
    template_name="index.html"
    form_class= QuestionForm
    model=Questions
    success_url=reverse_lazy("home")

    context_object_name:str="questions"
    # def get_queryset(self):
    #     return Questions.objects.all()
    
    