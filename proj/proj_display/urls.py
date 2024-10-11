from django.urls import path

from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("districts", views.districts, name="list-districts"),
    path("schools", views.schools, name="list-schools"),
    path("district/<str:district_aun>", views.district_view, name="district-view"),
    #path("district/<str:district_aun>/<str:year>/", views.district_view_year, name="district-view-year"),
    path("school/<str:school_id>", views.school_view, name="school-view"),
    path('yearDistrict/<str:district_aun>', views.year_view_district, name='year_view_district'),
    path('yearSchool/<str:school_id>', views.year_view_school, name='year_view_school'),
]