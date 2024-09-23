from django.urls import path

from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("districts", views.districts, name="list-districts"),
    path("schools", views.schools, name="list-schools"),

]