from django.shortcuts import render
from .models import Jozve
from django.views.generic import ListView

class JozveList(ListView):
    template_name = "jozve/jozveList.html"
    queryset = Jozve.objects.all()
    