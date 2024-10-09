from django.urls import path

from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("districts", views.districts, name="list-districts"),
    path("schools", views.schools, name="list-schools"),
    path("district/<str:district_aun>", views.district_view, name="district-view"),
    path("school/<str:school_id>", views.school_view, name="school-view"),
]