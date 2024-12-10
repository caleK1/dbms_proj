"""
    DBMS Project: Cale King, Eric Lynch, Jacob Seltzer
    Github Repo: https://github.com/caleK1/dbms_proj.git
"""

from django.shortcuts import render
from django.http import HttpResponse
from itertools import islice
import matplotlib.pyplot as plt
import numpy as np
from .models import School
from .models import District
from .models import County
from .models import SchoolInfo
from .models import GenderSchool
from .models import SchoolDemographic
from .models import ExtraDemoSchool
from .models import DistrictInfo
from .models import GenderDistrict
from .models import DistrictDemographic
from .models import ExtraDemoDistrict
from .models import SchoolFiscalData


# Create your views here.
def home(request):
    return HttpResponse("Hello, world. You're at the proj_display home.")

def districts(request):
    district_list = District.objects.all()
    county_list = County.objects.all()
    context = {'district_list': district_list, 'county_list': county_list}

    selected_county = request.GET.get('districtListCounty', None)
    if selected_county:
        context['selected_county'] = County.objects.get(county_id=selected_county)
        context['dist_in_county'] = District.objects.filter(county_id=selected_county)

    selected_district = request.GET.get('districtListDistrict', None)
    if selected_district:
        context['selected_district'] = District.objects.get(district_aun=selected_district)

    return render(request, 'district_list.html', context)

def schools(request):
    district_list = District.objects.all()
    county_list = County.objects.all()
    school_list = School.objects.all()
    context = {'district_list': district_list, 'county_list': county_list, 'school_list': school_list}

    selected_county = request.GET.get('schoolListCounty', None)
    if selected_county:
        context['selected_county'] = County.objects.get(county_id=selected_county)
        context['dist_in_county'] = District.objects.filter(county_id=selected_county)

    selected_district = request.GET.get('schoolListDistrict', None)
    if selected_district:
        context['selected_district'] = District.objects.get(district_aun=selected_district)
        context['schools_in_dist'] = School.objects.filter(district_aun=selected_district)

    selected_school = request.GET.get('schoolListSchool', None)
    if selected_school:
        context['selected_school'] = School.objects.get(school_id=selected_school)

    return render(request, 'school_list.html', context)

def district_view(request, district_aun):
    district = District.objects.get(district_aun=district_aun)
    schools = School.objects.filter(district_aun=district_aun)
    context = {'district_info' : district, 'school_info': schools}

    fast_facts = DistrictInfo.objects.get(district=district_aun)
    context['fast_facts'] = fast_facts

    return render(request, "district_view.html", context)

# def district_view_year(request, district_aun, year):
#     district = District.objects.get(district_aun=district_aun)
#     schools = School.objects.filter(district_aun=district_aun)
#     context = {'district_info' : district, 'school_info': schools}

#     if DistrictInfo.objects.filter(district=district_aun, year=year).exists():
#         distr_fast_facts = DistrictInfo.objects.get(district=district_aun, year=year)
#         context['fast_facts'] = distr_fast_facts

#     selected_year = request.GET.get('yearSchool', 'all-years')
#     context['selected_year'] = selected_year

#     if selected_year != "all-years":
#         if DistrictDemographic.objects.filter(school_year=selected_year, district=district_aun).exists():
#             district_demo = DistrictDemographic.objects.filter(school_year=selected_year, district=district_aun)
#             context['district_demo'] = district_demo
#     else:
#         if DistrictDemographic.objects.filter(district=district_aun).exists():
#             district_demo = DistrictDemographic.objects.filter(district=district_aun)
#             context['district_demo'] = district_demo

#     return render(request, "district_view.html", context)

def school_view(request, school_id):
    school = School.objects.get(school_id=school_id)

    context = {'school_info' : school}

    fast_facts = SchoolInfo.objects.get(school_id=school_id)
    context['fast_facts'] = fast_facts

    return render(request, "school_view.html", context)

def year_view_district(request, district_aun):
    district = District.objects.get(district_aun=district_aun)
    schools = School.objects.filter(district_aun=district_aun)
    context = {'district_info' : district, 'school_info': schools}

    fast_facts = DistrictInfo.objects.get(district=district_aun)
    context['fast_facts'] = fast_facts

    selected_year = request.GET.get('yearDistrict', 'all-years')
    context['selected_year'] = selected_year

    selected_cat = request.GET.get('categoryDistrict', 'demographic')
    context['selected_cat'] = selected_cat

    if selected_cat == "demographic":
        table_create_demographics_district(district_aun, selected_year, context, "")
    elif selected_cat == "fiscal":
        pass
    else:
        pass


    return render(request, 'district_view.html', context)

def year_view_school(request, school_id):
    school = School.objects.get(school_id=school_id)
    context = {'school_info' : school}

    fast_facts = SchoolInfo.objects.get(school_id=school_id)
    context['fast_facts'] = fast_facts

    selected_year = request.GET.get('yearSchool', 'all-years')
    context['selected_year'] = selected_year

    selected_cat = request.GET.get('categorySchool', 'demographic')
    context['selected_cat'] = selected_cat

    if selected_cat == "demographic":
        table_create_demographics(school_id, selected_year, context)
    elif selected_cat == "fiscal":
        table_create_fiscal(school_id, selected_year, context)
    else:
        pass


    return render(request, 'school_view.html', context)

def compare(request):
    county_list = County.objects.all()
    district_list = District.objects.all()
    school_list = School.objects.all()
    context = {'county_list' : county_list, 'district_list' : district_list, 'school_list' : school_list}

    selected_county = request.GET.get('districtCompareCounty', None)
    if selected_county:
        context['selected_county'] = County.objects.get(county_id=selected_county)
        context['dist_in_county'] = District.objects.filter(county_id=selected_county)

    selected_county2 = request.GET.get('districtCompareCounty2', None)
    if selected_county2:
        context['selected_county2'] = County.objects.get(county_id=selected_county2)
        context['dist_in_county2'] = District.objects.filter(county_id=selected_county2)

    context['selected_year'] = 'all-years'
    selected_district = request.GET.get('districtCompareDistrict', None)
    if selected_district:
        context['selected_district'] = District.objects.get(district_aun=selected_district)
        # if DistrictDemographic.objects.filter(district=selected_district).exists():
        #     context['selected_district_demo'] = DistrictDemographic.objects.filter(district=selected_district)
        table_create_demographics_district(selected_district, 'all-years', context, "")

    selected_district2 = request.GET.get('districtCompareDistrict2', None)
    if selected_district2:
        context['selected_district2'] = District.objects.get(district_aun=selected_district2)
        # if DistrictDemographic.objects.filter(district=selected_district).exists():
        #     context['selected_district_demo2'] = DistrictDemographic.objects.filter(district=selected_district2)
        table_create_demographics_district(selected_district2, 'all-years', context, "_compare")

    return render(request, 'compare.html', context)

def table_create_demographics(school_id, selected_year, context):
    if selected_year != "all-years":
        #School Demographic
        if SchoolDemographic.objects.filter(school_year=selected_year, school_id=school_id).exists():
            cat_info = SchoolDemographic.objects.get(school_year=selected_year, school_id=school_id)

            fields = []
            i = 0
            for field in SchoolDemographic._meta.get_fields():
                if not field.is_relation and i != 0:
                    fields.append(field.verbose_name)
                i = i + 1
            context['cat_headers'] = fields

            cat_info_dict = cat_info.__dict__
            good_cat_info_dict = dict(islice(cat_info_dict.items(), 3, None))
            context['cat_info'] = good_cat_info_dict.values()
            context['table_name'] = 'Demographic Information'

            demo_pie_chart = dict()
            i = 0
            for val in fields:
                if i != 0:
                    demo_pie_chart.update({fields[i]: list(good_cat_info_dict.values())[i]})
                i = i + 1

            context['cat_graph'] = demo_pie_chart

        #Extra Demographic
        if ExtraDemoSchool.objects.filter(school_year=selected_year, school_id=school_id).exists():
            cat_info2 = ExtraDemoSchool.objects.get(school_year=selected_year, school_id=school_id)

            fields = []
            i = 0
            for field in ExtraDemoSchool._meta.get_fields():
                if not field.is_relation and i != 0:
                    fields.append(field.verbose_name)
                i = i + 1
            context['cat_headers2'] = fields

            cat_info_dict2 = cat_info2.__dict__
            good_cat_info_dict2 = dict(islice(cat_info_dict2.items(), 3, None))
            context['cat_info2'] = good_cat_info_dict2.values()
            context['table_name2'] = 'More Demographic Information'

        #Gender School
        if GenderSchool.objects.filter(school_year=selected_year, school_id=school_id).exists():
            cat_info3 = GenderSchool.objects.get(school_year=selected_year, school_id=school_id)

            fields = []
            i = 0
            for field in GenderSchool._meta.get_fields():
                if not field.is_relation and i != 0:
                    fields.append(field.verbose_name)
                i = i + 1
            context['cat_headers3'] = fields

            cat_info_dict3 = cat_info3.__dict__
            good_cat_info_dict3 = dict(islice(cat_info_dict3.items(), 3, None))
            context['cat_info3'] = good_cat_info_dict3.values()
            context['table_name3'] = 'Gender Information'

            gender_pie_chart = {fields[1]: list(good_cat_info_dict3.values())[1], fields[2]: list(good_cat_info_dict3.values())[2]}
            context['cat_graph3'] = gender_pie_chart

            # y = np.array([list(good_cat_info_dict3.values())[1], list(good_cat_info_dict3.values())[2]])
            # mylabels = [fields[1], fields[2]]
            # fig = plt.pie(y, labels=mylabels)
            # html_str = mpld3.fig_to_html(fig)
            # context['html_str'] = html_str

    else:
        if SchoolDemographic.objects.filter(school_id=school_id).exists():
            cat_info = SchoolDemographic.objects.filter(school_id=school_id)

            fields = []
            i = 0
            for field in SchoolDemographic._meta.get_fields():
                if not field.is_relation and i != 0:
                    fields.append(field.verbose_name)
                i = i + 1
            context['cat_headers'] = fields

            cat_info_list = []
            cat_info_headers = []

            i = 0
            for info in cat_info:
                cat_info_dict = info.__dict__
                good_cat_info_dict = dict(islice(cat_info_dict.items(), 3, None))
                cat_info_list.append(good_cat_info_dict)

            context['cat_info'] = cat_info_list
            context['table_name'] = 'Demographic Information'

        #Extra Demographic
        if ExtraDemoSchool.objects.filter(school_id=school_id).exists():
            cat_info2 = ExtraDemoSchool.objects.filter(school_id=school_id)

            fields = []
            i = 0
            for field in ExtraDemoSchool._meta.get_fields():
                if not field.is_relation and i != 0:
                    fields.append(field.verbose_name)
                i = i + 1
            context['cat_headers2'] = fields

            cat_info_list2 = []
            cat_info_headers2 = []

            i = 0
            for info in cat_info2:
                cat_info_dict2 = info.__dict__
                good_cat_info_dict2 = dict(islice(cat_info_dict2.items(), 3, None))
                cat_info_list2.append(good_cat_info_dict2)

            context['cat_info2'] = cat_info_list2
            context['table_name2'] = 'More Demographic Information'

        #Gender School
        if GenderSchool.objects.filter(school_id=school_id).exists():
            cat_info3 = GenderSchool.objects.filter(school_id=school_id)

            fields = []
            i = 0
            for field in GenderSchool._meta.get_fields():
                if not field.is_relation and i != 0:
                    fields.append(field.verbose_name)
                i = i + 1
            context['cat_headers3'] = fields

            cat_info_list3 = []
            cat_info_headers3 = []

            i = 0
            for info in cat_info3:
                cat_info_dict3 = info.__dict__
                good_cat_info_dict3 = dict(islice(cat_info_dict3.items(), 3, None))
                cat_info_list3.append(good_cat_info_dict3)

            context['cat_info3'] = cat_info_list3
            context['table_name3'] = 'Gender Information'

def table_create_demographics_district(district_aun, selected_year, context, add):
    if selected_year != "all-years":
        #School Demographic
        if DistrictDemographic.objects.filter(school_year=selected_year, district=district_aun).exists():
            cat_info = DistrictDemographic.objects.get(school_year=selected_year, district=district_aun)

            fields = []
            i = 0
            for field in DistrictDemographic._meta.get_fields():
                if not field.is_relation and i != 0:
                    fields.append(field.verbose_name)
                i = i + 1
            context[f'cat_headers{add}'] = fields

            cat_info_dict = cat_info.__dict__
            good_cat_info_dict = dict(islice(cat_info_dict.items(), 3, None))
            context[f'cat_info{add}'] = good_cat_info_dict.values()
            context['table_name'] = 'Demographic Information'

        #Extra Demographic
        if ExtraDemoDistrict.objects.filter(school_year=selected_year, district=district_aun).exists():
            cat_info2 = ExtraDemoDistrict.objects.get(school_year=selected_year, district=district_aun)

            fields = []
            i = 0
            for field in ExtraDemoDistrict._meta.get_fields():
                if not field.is_relation and i != 0:
                    fields.append(field.verbose_name)
                i = i + 1
            context[f'cat_headers2{add}'] = fields

            cat_info_dict2 = cat_info2.__dict__
            good_cat_info_dict2 = dict(islice(cat_info_dict2.items(), 3, None))
            context[f'cat_info2{add}'] = good_cat_info_dict2.values()
            context[f'table_name2{add}'] = 'More Demographic Information'

        #Gender School
        if GenderDistrict.objects.filter(school_year=selected_year, district=district_aun).exists():
            cat_info3 = GenderDistrict.objects.get(school_year=selected_year, district=district_aun)

            fields = []
            i = 0
            for field in GenderDistrict._meta.get_fields():
                if not field.is_relation and i != 0:
                    fields.append(field.verbose_name)
                i = i + 1
            context[f'cat_headers3{add}'] = fields

            cat_info_dict3 = cat_info3.__dict__
            good_cat_info_dict3 = dict(islice(cat_info_dict3.items(), 3, None))
            context[f'cat_info3{add}'] = good_cat_info_dict3.values()
            context[f'table_name3{add}'] = 'Gender Information'

            gender_pie_chart = {fields[1]: list(good_cat_info_dict3.values())[1], fields[2]: list(good_cat_info_dict3.values())[2]}
            context['cat_graph3'] = gender_pie_chart

    else:
        if DistrictDemographic.objects.filter(district=district_aun).exists():
            cat_info = DistrictDemographic.objects.filter(district=district_aun)

            fields = []
            i = 0
            for field in DistrictDemographic._meta.get_fields():
                if not field.is_relation and i != 0:
                    fields.append(field.verbose_name)
                i = i + 1
            context[f'cat_headers{add}'] = fields

            cat_info_list = []
            cat_info_headers = []

            i = 0
            for info in cat_info:
                cat_info_dict = info.__dict__
                good_cat_info_dict = dict(islice(cat_info_dict.items(), 3, None))
                cat_info_list.append(good_cat_info_dict)

            context[f'cat_info{add}'] = cat_info_list
            context[f'table_name{add}'] = 'Demographic Information'

        #Extra Demographic
        if ExtraDemoDistrict.objects.filter(district=district_aun).exists():
            cat_info2 = ExtraDemoDistrict.objects.filter(district=district_aun)

            fields = []
            i = 0
            for field in ExtraDemoDistrict._meta.get_fields():
                if not field.is_relation and i != 0:
                    fields.append(field.verbose_name)
                i = i + 1
            context[f'cat_headers2{add}'] = fields

            cat_info_list2 = []
            cat_info_headers2 = []

            i = 0
            for info in cat_info2:
                cat_info_dict2 = info.__dict__
                good_cat_info_dict2 = dict(islice(cat_info_dict2.items(), 3, None))
                cat_info_list2.append(good_cat_info_dict2)

            context[f'cat_info2{add}'] = cat_info_list2
            context[f'table_name2{add}'] = 'More Demographic Information'

        #Gender School
        if GenderDistrict.objects.filter(district=district_aun).exists():
            cat_info3 = GenderDistrict.objects.filter(district=district_aun)

            fields = []
            i = 0
            for field in GenderDistrict._meta.get_fields():
                if not field.is_relation and i != 0:
                    fields.append(field.verbose_name)
                i = i + 1
            context[f'cat_headers3{add}'] = fields

            cat_info_list3 = []
            cat_info_headers3 = []

            i = 0
            for info in cat_info3:
                cat_info_dict3 = info.__dict__
                good_cat_info_dict3 = dict(islice(cat_info_dict3.items(), 3, None))
                cat_info_list3.append(good_cat_info_dict3)

            context[f'cat_info3{add}'] = cat_info_list3
            context[f'table_name3{add}'] = 'Gender Information'

def table_create_fiscal(school_id, selected_year, context):
    if selected_year != "all-years":
        #School Demographic
        if SchoolFiscalData.objects.filter(school_year=selected_year, school_id=school_id).exists():
            cat_info = SchoolFiscalData.objects.get(school_year=selected_year, school_id=school_id)

            fields = []
            i = 0
            for field in SchoolFiscalData._meta.get_fields():
                if not field.is_relation and i != 0:
                    fields.append(field.verbose_name)
                i = i + 1
            context['cat_headers'] = fields

            cat_info_dict = cat_info.__dict__
            good_cat_info_dict = dict(islice(cat_info_dict.items(), 3, None))
            context['cat_info'] = good_cat_info_dict.values()
            context['table_name'] = 'Fiscal Information'
    else:
        if SchoolFiscalData.objects.filter(school_id=school_id).exists():
            cat_info = SchoolFiscalData.objects.filter(school_id=school_id)

            fields = []
            i = 0
            for field in SchoolFiscalData._meta.get_fields():
                if not field.is_relation and i != 0:
                    fields.append(field.verbose_name)
                i = i + 1
            context['cat_headers'] = fields

            cat_info_list = []
            cat_info_headers = []

            i = 0
            for info in cat_info:
                cat_info_dict = info.__dict__
                good_cat_info_dict = dict(islice(cat_info_dict.items(), 3, None))
                cat_info_list.append(good_cat_info_dict)

            context['cat_info'] = cat_info_list
            context['table_name'] = 'Fiscal Information'