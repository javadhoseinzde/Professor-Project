from django.urls import path
from .views import JozveList

app_name = "jozve"

urlpatterns = [
    path("list-jozve",JozveList.as_view(), name="list-jozve")
]