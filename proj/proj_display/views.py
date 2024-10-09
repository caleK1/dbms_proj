from django.shortcuts import render
from django.http import HttpResponse
from .models import DistrictFastFacts
from .models import SchoolFastFacts
from .models import School
from .models import District
from .models import County

# Create your views here.
def home(request):
    return HttpResponse("Hello, world. You're at the proj_display home.")

def districts(request):
    district_list = District.objects.all()
    county_list = County.objects.all()
    context = {'district_list': district_list, 'county_list': county_list}
    return render(request, 'district_list.html', context)

def schools(request):
    school_list = School.objects.all()
    return render(request, 'school_list.html', {'school_list': school_list})

def district_view(request, district_aun):
    district = District.objects.get(district_aun=district_aun)
    schools = School.objects.filter(district_aun=district_aun)
    context = {'district_info' : district, 'school_info': schools}
    return render(request, "district_view.html", context)

def school_view(request, school_id):
    school = School.objects.get(school_id=school_id)
    context = {'school_info' : school}
    return render(request, "school_view.html", context)