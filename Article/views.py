from django.shortcuts import render
from .models import Articles
from django.views.generic import ListView, DetailView
# Create your views here.
class ArticleList(ListView):
    queryset = Articles.objects.filter(published=True)
    template_name = "Article/ArticleList.html" 

class ArticleDetail(DetailView):
    template_name = "Article/ArticleDetail.html"
    def get_queryset(self):
        slug = self.kwargs.get("slug")
        article = Articles.objects.filter(slug=slug)
        return Articles.objects.filter(slug=slug)