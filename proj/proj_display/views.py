from django.shortcuts import render
from django.http import HttpResponse
from .models import DistrictFastFacts
from .models import SchoolFastFacts
from .models import DistrictFiscalData

# Create your views here.
def home(request):
    return HttpResponse("Hello, world. You're at the proj_display home.")

def districts(request):
    district_list = DistrictFastFacts.objects.all()
    return render(request, 'district_list.html', {'district_list': district_list})

def schools(request):
    school_list = SchoolFastFacts.objects.all()
    return render(request, 'school_list.html', {'school_list': school_list})

def district_view(request, district_name):
    district = DistrictFastFacts.objects.get(name=district_name)
    context = {'district_info' : district}
    return render(request, "district_view.html", context)

def school_view(request, school_name):
    school = SchoolFastFacts.objects.get(name=school_name)
    context = {'school_info' : school}
    return render(request, "school_view.html", context)
