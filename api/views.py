from django.shortcuts import render

# Create your views here.
from stack.models import Questions
from rest_framework import viewsets
from rest_framework.response import Response
from api.serializers import QuestionSerializer


class QuestionView(viewsets.ModelViewSet):
    serializer_class = QuestionSerializer
    queryset = Questions.objects.all()
    
