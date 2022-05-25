from django.urls import path
from .views import Classes, Number, Home
app_name ="student-number"
urlpatterns = [
    path("", Home.as_view(), name="home"),
    path("list-nomarat", Classes.as_view(), name="Classes"),
    path("number/<slug:slug>/<str:name>/", Number.as_view(), name="number"),
]