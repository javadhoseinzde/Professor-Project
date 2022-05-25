from django.urls import path
from .views import ArticleList, ArticleDetail
app_name = "Article"
urlpatterns = [
    path("articlelist", ArticleList.as_view(), name="ArticleLists"),
    path('article/<slug:slug>/',ArticleDetail.as_view(), name='ArticleDetail')
    ]