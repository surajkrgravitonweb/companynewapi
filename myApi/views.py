from django.shortcuts import render
from rest_framework import viewsets
from .models import Form1,Form2
from .serializers import Form1Serializers,Form2Serializers
# Create your views here.

class Form1ViewSet(viewsets.ModelViewSet):
    queryset=Form1.objects.all()
    serializer_class=Form1Serializers


class Form2ViewSet(viewsets.ModelViewSet):
    queryset=Form2.objects.all()
    serializer_class=Form2Serializers

class Form3ViewSet(viewsets.ModelViewSet):
    queryset=Form2.objects.all()
    serializer_class=Form2Serializers