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

    if DistrictFastFacts.objects.filter(aun=district_aun).exists():
        distr_fast_facts = DistrictFastFacts.objects.filter(aun=district_aun)
        context['fast_facts'] = distr_fast_facts

    return render(request, "district_view.html", context)

"""
def district_view_year(request, district_aun, year):
    district = District.objects.get(district_aun=district_aun)
    schools = School.objects.filter(district_aun=district_aun)
    context = {'district_info' : district, 'school_info': schools}

    if DistrictFastFacts.objects.filter(aun=district_aun, year=year).exists():
        distr_fast_facts = DistrictFastFacts.objects.get(aun=district_aun, year=year)
        context['fast_facts'] = distr_fast_facts

    return render(request, "district_view.html", context)
"""
def school_view(request, school_id):
    school = School.objects.get(school_id=school_id)
    context = {'school_info' : school}

    if SchoolFastFacts.objects.filter(school_id=school_id).exists():
        school_fast_facts = SchoolFastFacts.objects.filter(school_id=school_id)
        context['fast_facts'] = school_fast_facts

    return render(request, "school_view.html", context)

def year_view_district(request, district_aun):
    district = District.objects.get(district_aun=district_aun)
    schools = School.objects.filter(district_aun=district_aun)
    context = {'district_info' : district, 'school_info': schools}

    selected_year = request.GET.get('yearDistrict', 'all-years')
    context['selected_year'] = selected_year

    if selected_year != "all-years":
        if DistrictFastFacts.objects.filter(year=selected_year, aun=district_aun).exists():
            district_fast_facts = DistrictFastFacts.objects.filter(year=selected_year, aun=district_aun)
            context['fast_facts'] = district_fast_facts
    else:
        if DistrictFastFacts.objects.filter(aun=district_aun).exists():
            distr_fast_facts = DistrictFastFacts.objects.filter(aun=district_aun)
            context['fast_facts'] = distr_fast_facts


    return render(request, 'district_view.html', context)

def year_view_school(request, school_id):
    school = School.objects.get(school_id=school_id)
    context = {'school_info' : school}

    selected_year = request.GET.get('yearSchool', 'all-years')
    context['selected_year'] = selected_year

    if selected_year != "all-years":
        if SchoolFastFacts.objects.filter(year=selected_year, school_id=school_id).exists():
            school_fast_facts = SchoolFastFacts.objects.filter(year=selected_year, school_id=school_id)
            context['fast_facts'] = school_fast_facts
    else:
        if SchoolFastFacts.objects.filter(school_id=school_id).exists():
            school_fast_facts = SchoolFastFacts.objects.filter(school_id=school_id)
            context['fast_facts'] = school_fast_facts


    return render(request, 'school_view.html', context)