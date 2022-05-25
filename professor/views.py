from django.shortcuts import render, get_object_or_404
from .models import Class_Name, Student_Number
from django.views.generic import ListView, DetailView, TemplateView

class Home(TemplateView):
    template_name = "clases/home.html"

class Classes(ListView):
    queryset = Class_Name.objects.filter(published=True)
    template_name = "clases/classes.html"
    
class Number(ListView):
    template_name = "clases/studentnumber.html"
    context_object_name = "ob"
    def get_queryset(self):
        name = self.kwargs.get("name")
        p1 = get_object_or_404(Class_Name, name=name)
        slug = self.kwargs.get("slug")
        return Student_Number.objects.filter(class_name__name=p1, slug=slug)

