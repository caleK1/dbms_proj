"""
    DBMS Project: Cale King, Eric Lynch, Jacob Seltzer
    Github Repo: https://github.com/caleK1/dbms_proj.git
"""

from django.shortcuts import render
from django.http import HttpResponse
from itertools import islice
import matplotlib.pyplot as plt
import numpy as np
import json
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
from .models import LowIncomePercentPubSchool
from .models import DistrictFiscalData
from .models import PublicSchoolGradRatesSchool
from .models import AidRatio
from .models import PersonalIncome


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
        table_create_fiscal_district(district_aun, selected_year, context, "")
    elif selected_cat == "aid_ratio":
        table_create_aid_ratio_district(district_aun, selected_year, context, "")
    elif selected_cat == "personal_income":
        table_create_personal_income_district(district_aun, selected_year, context, "")
    else:
        pass

    selected_attr = request.GET.get('trendAttrDistrict', 'None')
    context['selected_attr'] = selected_attr
    trend_graph_create_district(district_aun, context, selected_cat, selected_attr)


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
        table_create_demographics(school_id, selected_year, context, "")
    elif selected_cat == "fiscal":
        table_create_fiscal(school_id, selected_year, context, "")
    elif selected_cat == "enroll_low_income":
        table_create_enroll_low_income(school_id, selected_year, context, "")
    elif selected_cat == "pub_school_grad_rates":
        table_create_pub_school_grad_rates(school_id, selected_year, context, "")
    else:
        pass

    selected_attr = request.GET.get('trendAttrSchool', 'None')
    context['selected_attr'] = selected_attr
    trend_graph_create(school_id, context, selected_cat, selected_attr)

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
        context['schls_in_dist'] = School.objects.filter(district_aun=selected_district)

    selected_district2 = request.GET.get('districtCompareDistrict2', None)
    if selected_district2:
        context['selected_district2'] = District.objects.get(district_aun=selected_district2)
        context['schls_in_dist2'] = School.objects.filter(district_aun=selected_district2)

    selected_school = request.GET.get('districtCompareSchool', None)
    if selected_school:
        context['selected_school'] = School.objects.get(school_id=selected_school)

    selected_school2 = request.GET.get('districtCompareSchool2', None)
    if selected_school2:
        context['selected_school2'] = School.objects.get(school_id=selected_school2)

    selected_cat = request.GET.get('categoryCompare', 'demographic')
    context['selected_cat'] = selected_cat

    if not selected_school or not selected_school2:
        if selected_cat == "demographic":
            table_create_demographics_district(selected_district, 'all-years', context, "")
            table_create_demographics_district(selected_district2, 'all-years', context, "_compare")
        elif selected_cat == "fiscal":
            table_create_fiscal_district(selected_district, 'all-years', context, "")
            table_create_fiscal_district(selected_district2, 'all-years', context, "_compare")
        elif selected_cat == "aid_ratio":
            table_create_aid_ratio_district(selected_district, 'all-years', context, "")
            table_create_aid_ratio_district(selected_district2, 'all-years', context, "_compare")
        elif selected_cat == "personal_income":
            table_create_personal_income_district(selected_district, 'all-years', context, "")
            table_create_personal_income_district(selected_district2, 'all-years', context, "_compare")
        else:
            pass
    else:
        if selected_cat == "demographic":
            table_create_demographics(selected_school, 'all-years', context, "")
            table_create_demographics(selected_school2, 'all-years', context, "_compare")
        elif selected_cat == "fiscal":
            table_create_fiscal(selected_school, 'all-years', context, "")
            table_create_fiscal(selected_school2, 'all-years', context, "_compare")
        elif selected_cat == "enroll_low_income":
            table_create_enroll_low_income(selected_school, 'all-years', context, "")
            table_create_enroll_low_income(selected_school2, 'all-years', context, "_compare")
        elif selected_cat == "pub_school_grad_rates":
            table_create_pub_school_grad_rates(selected_school, 'all-years', context, "")
            table_create_pub_school_grad_rates(selected_school2, 'all-years', context, "_compare")
        else:
            pass

    selected_attr = request.GET.get('trendAttrCompare', 'None')
    context['selected_attr'] = selected_attr

    if not selected_school or not selected_school2:
        trend_graph_create_compare_district(selected_district, selected_district2, context, selected_cat, selected_attr)
    else:
        trend_graph_create_compare_school(selected_school, selected_school2, context, selected_cat, selected_attr)

    return render(request, 'compare.html', context)

def trend_graph_create_compare_district(selected_district, selected_district2, context, selected_cat, attr):
    if selected_cat == "demographic":

        demo_attr = ["per_asian", "per_hispanic", "per_pacific_islander", "per_am_indian_or_alaskan_native", "per_african_american", "per_white", "per_two_or_more_races"]
        extra_demo_attr = ["per_english_learner", "per_special_education", "per_gifted_student", "per_military_connected", "per_foster_care", "per_economically_disadvantaged", "per_homeless"]
        gender_attr = ["male", "female"]

        if attr in demo_attr:
            if DistrictDemographic.objects.filter(district=selected_district).exists() and DistrictDemographic.objects.filter(district=selected_district2).exists():
                years = DistrictDemographic.objects.filter(district=selected_district).values('school_year').distinct()
                years_data = [item['school_year'] for item in years]
                values = []
                values2 = []
                for year in years_data:
                    record = DistrictDemographic.objects.filter(district=selected_district, school_year=year).first()
                    record2 = DistrictDemographic.objects.filter(district=selected_district2, school_year=year).first()

                    if record:
                        value = getattr(record, attr, None)
                        values.append(value)
                    else:
                        values.append(None)

                    if record2:
                        value2 = getattr(record2, attr, None)
                        values2.append(value2)
                    else:
                        values2.append(None)

                school1_name = getattr(District.objects.filter(district_aun=selected_district).first(), "district_name", None)
                school2_name = getattr(District.objects.filter(district_aun=selected_district2).first(), "district_name", None)
                trend_data = {
                    'years': years_data,
                    'values': values,
                    'values2': values2,
                    'yLabel': attr,
                    'school1_name': school1_name,
                    'school2_name': school2_name
                }
                print(trend_data)
                context['trend_data_json'] = json.dumps(trend_data)
        if attr in extra_demo_attr:
            if ExtraDemoDistrict.objects.filter(district=selected_district).exists() and ExtraDemoDistrict.objects.filter(district=selected_district2).exists():
                years = ExtraDemoDistrict.objects.filter(district=selected_district).values('school_year').distinct()
                years_data = [item['school_year'] for item in years]
                values = []
                values2 = []
                for year in years_data:
                    record = ExtraDemoDistrict.objects.filter(district=selected_district, school_year=year).first()
                    record2 = ExtraDemoDistrict.objects.filter(district=selected_district2, school_year=year).first()

                    if record:
                        value = getattr(record, attr, None)
                        values.append(value)
                    else:
                        values.append(None)

                    if record2:
                        value2 = getattr(record2, attr, None)
                        values2.append(value2)
                    else:
                        values2.append(None)

                school1_name = getattr(District.objects.filter(district_aun=selected_district).first(), "district_name", None)
                school2_name = getattr(District.objects.filter(district_aun=selected_district2).first(), "district_name", None)
                trend_data = {
                    'years': years_data,
                    'values': values,
                    'values2': values2,
                    'yLabel': attr,
                    'school1_name': school1_name,
                    'school2_name': school2_name
                }
                print(trend_data)
                context['trend_data_json'] = json.dumps(trend_data)
        if attr in gender_attr:
            if GenderDistrict.objects.filter(district=selected_district).exists() and GenderDistrict.objects.filter(district=selected_district2).exists():
                years = GenderDistrict.objects.filter(district=selected_district).values('school_year').distinct()
                years_data = [item['school_year'] for item in years]
                values = []
                values2 = []
                for year in years_data:
                    record = GenderDistrict.objects.filter(district=selected_district, school_year=year).first()
                    record2 = GenderDistrict.objects.filter(district=selected_district2, school_year=year).first()

                    if record:
                        value = getattr(record, attr, None)
                        values.append(value)
                    else:
                        values.append(None)

                    if record2:
                        value2 = getattr(record2, attr, None)
                        values2.append(value2)
                    else:
                        values2.append(None)

                school1_name = getattr(District.objects.filter(district_aun=selected_district).first(), "district_name", None)
                school2_name = getattr(District.objects.filter(district_aun=selected_district2).first(), "district_name", None)
                trend_data = {
                    'years': years_data,
                    'values': values,
                    'values2': values2,
                    'yLabel': attr,
                    'school1_name': school1_name,
                    'school2_name': school2_name
                }
                print(trend_data)
                context['trend_data_json'] = json.dumps(trend_data)
    elif selected_cat == "fiscal":
        if DistrictFiscalData.objects.filter(district=selected_district).exists() and DistrictFiscalData.objects.filter(district=selected_district2).exists():
                years = DistrictFiscalData.objects.filter(district=selected_district).values('school_year').distinct()
                years_data = [item['school_year'] for item in years]
                values = []
                values2 = []
                for year in years_data:
                    record = DistrictFiscalData.objects.filter(district=selected_district, school_year=year).first()
                    record2 = DistrictFiscalData.objects.filter(district=selected_district2, school_year=year).first()

                    if record:
                        value = getattr(record, attr, None)
                        values.append(value)
                    else:
                        values.append(None)

                    if record2:
                        value2 = getattr(record2, attr, None)
                        values2.append(value2)
                    else:
                        values2.append(None)

                school1_name = getattr(District.objects.filter(district_aun=selected_district).first(), "district_name", None)
                school2_name = getattr(District.objects.filter(district_aun=selected_district2).first(), "district_name", None)
                trend_data = {
                    'years': years_data,
                    'values': values,
                    'values2': values2,
                    'yLabel': attr,
                    'school1_name': school1_name,
                    'school2_name': school2_name
                }
                print(trend_data)
                context['trend_data_json'] = json.dumps(trend_data)
    elif selected_cat == "aid_ratio":
        if AidRatio.objects.filter(district=selected_district).exists() and AidRatio.objects.filter(district=selected_district2).exists():
                years = AidRatio.objects.filter(district=selected_district).values('school_year').distinct()
                years_data = [item['school_year'] for item in years]
                values = []
                values2 = []
                for year in years_data:
                    record = AidRatio.objects.filter(district=selected_district, school_year=year).first()
                    record2 = AidRatio.objects.filter(district=selected_district2, school_year=year).first()

                    if record:
                        value = getattr(record, attr, None)
                        values.append(value)
                    else:
                        values.append(None)

                    if record2:
                        value2 = getattr(record2, attr, None)
                        values2.append(value2)
                    else:
                        values2.append(None)

                school1_name = getattr(District.objects.filter(district_aun=selected_district).first(), "district_name", None)
                school2_name = getattr(District.objects.filter(district_aun=selected_district2).first(), "district_name", None)
                trend_data = {
                    'years': years_data,
                    'values': values,
                    'values2': values2,
                    'yLabel': attr,
                    'school1_name': school1_name,
                    'school2_name': school2_name
                }
                print(trend_data)
                context['trend_data_json'] = json.dumps(trend_data)
    elif selected_cat == "personal_income":
        if PersonalIncome.objects.filter(district=selected_district).exists() and PersonalIncome.objects.filter(district=selected_district2).exists():
                years = PersonalIncome.objects.filter(district=selected_district).values('school_year').distinct()
                years_data = sorted([item['school_year'] for item in years], key=lambda x: x)
                values = []
                values2 = []
                for year in years_data:
                    record = PersonalIncome.objects.filter(district=selected_district, school_year=year).first()
                    record2 = PersonalIncome.objects.filter(district=selected_district2, school_year=year).first()

                    if record:
                        value = getattr(record, attr, None)
                        values.append(value)
                    else:
                        values.append(None)

                    if record2:
                        value2 = getattr(record2, attr, None)
                        values2.append(value2)
                    else:
                        values2.append(None)

                school1_name = getattr(District.objects.filter(district_aun=selected_district).first(), "district_name", None)
                school2_name = getattr(District.objects.filter(district_aun=selected_district2).first(), "district_name", None)
                trend_data = {
                    'years': years_data,
                    'values': values,
                    'values2': values2,
                    'yLabel': attr,
                    'school1_name': school1_name,
                    'school2_name': school2_name
                }
                print(trend_data)
                context['trend_data_json'] = json.dumps(trend_data)

def trend_graph_create_compare_school(selected_school, selected_school2, context, selected_cat, attr):
    if selected_cat == "demographic":

        demo_attr = ["per_asian", "per_hispanic", "per_pacific_islander", "per_am_indian_or_alaskan_native", "per_african_american", "per_white", "per_two_or_more_races"]
        extra_demo_attr = ["per_english_learner", "per_special_education", "per_gifted_student", "per_military_connected", "per_foster_care", "per_economically_disadvantaged", "per_homeless"]
        gender_attr = ["male", "female"]

        if attr in demo_attr:
            if SchoolDemographic.objects.filter(school_id=selected_school).exists() and SchoolDemographic.objects.filter(school_id=selected_school2).exists():
                years = SchoolDemographic.objects.filter(school_id=selected_school).values('school_year').distinct()
                years_data = [item['school_year'] for item in years]
                values = []
                values2 = []
                for year in years_data:
                    record = SchoolDemographic.objects.filter(school_id=selected_school, school_year=year).first()
                    record2 = SchoolDemographic.objects.filter(school_id=selected_school2, school_year=year).first()

                    if record:
                        value = getattr(record, attr, None)
                        values.append(value)
                    else:
                        values.append(None)

                    if record2:
                        value2 = getattr(record2, attr, None)
                        values2.append(value2)
                    else:
                        values2.append(None)

                school1_name = getattr(School.objects.filter(school_id=selected_school).first(), "school_name", None)
                school2_name = getattr(School.objects.filter(school_id=selected_school2).first(), "school_name", None)
                trend_data = {
                    'years': years_data,
                    'values': values,
                    'values2': values2,
                    'yLabel': attr,
                    'school1_name': school1_name,
                    'school2_name': school2_name
                }
                print(trend_data)
                context['trend_data_json'] = json.dumps(trend_data)
        if attr in extra_demo_attr:
            if ExtraDemoSchool.objects.filter(school_id=selected_school).exists() and ExtraDemoSchool.objects.filter(school_id=selected_school2).exists():
                years = ExtraDemoSchool.objects.filter(school_id=selected_school).values('school_year').distinct()
                years_data = [item['school_year'] for item in years]
                values = []
                values2 = []
                for year in years_data:
                    record = ExtraDemoSchool.objects.filter(school_id=selected_school, school_year=year).first()
                    record2 = ExtraDemoSchool.objects.filter(school_id=selected_school2, school_year=year).first()

                    if record:
                        value = getattr(record, attr, None)
                        values.append(value)
                    else:
                        values.append(None)

                    if record2:
                        value2 = getattr(record2, attr, None)
                        values2.append(value2)
                    else:
                        values2.append(None)

                school1_name = getattr(School.objects.filter(school_id=selected_school).first(), "school_name", None)
                school2_name = getattr(School.objects.filter(school_id=selected_school2).first(), "school_name", None)
                trend_data = {
                    'years': years_data,
                    'values': values,
                    'values2': values2,
                    'yLabel': attr,
                    'school1_name': school1_name,
                    'school2_name': school2_name
                }
                print(trend_data)
                context['trend_data_json'] = json.dumps(trend_data)
        if attr in gender_attr:
            if GenderSchool.objects.filter(school_id=selected_school).exists() and GenderSchool.objects.filter(school_id=selected_school2).exists():
                years = GenderSchool.objects.filter(school_id=selected_school).values('school_year').distinct()
                years_data = [item['school_year'] for item in years]
                values = []
                values2 = []
                for year in years_data:
                    record = GenderSchool.objects.filter(school_id=selected_school, school_year=year).first()
                    record2 = GenderSchool.objects.filter(school_id=selected_school2, school_year=year).first()

                    if record:
                        value = getattr(record, attr, None)
                        values.append(value)
                    else:
                        values.append(None)

                    if record2:
                        value2 = getattr(record2, attr, None)
                        values2.append(value2)
                    else:
                        values2.append(None)

                school1_name = getattr(School.objects.filter(school_id=selected_school).first(), "school_name", None)
                school2_name = getattr(School.objects.filter(school_id=selected_school2).first(), "school_name", None)
                trend_data = {
                    'years': years_data,
                    'values': values,
                    'values2': values2,
                    'yLabel': attr,
                    'school1_name': school1_name,
                    'school2_name': school2_name
                }
                print(trend_data)
                context['trend_data_json'] = json.dumps(trend_data)
    elif selected_cat == "fiscal":
        if SchoolFiscalData.objects.filter(school_id=selected_school).exists() and SchoolFiscalData.objects.filter(school_id=selected_school2).exists():
                years = SchoolFiscalData.objects.filter(school_id=selected_school).values('school_year').distinct()
                years_data = [item['school_year'] for item in years]
                values = []
                values2 = []
                for year in years_data:
                    record = SchoolFiscalData.objects.filter(school_id=selected_school, school_year=year).first()
                    record2 = SchoolFiscalData.objects.filter(school_id=selected_school2, school_year=year).first()

                    if record:
                        value = getattr(record, attr, None)
                        values.append(value)
                    else:
                        values.append(None)

                    if record2:
                        value2 = getattr(record2, attr, None)
                        values2.append(value2)
                    else:
                        values2.append(None)

                school1_name = getattr(School.objects.filter(school_id=selected_school).first(), "school_name", None)
                school2_name = getattr(School.objects.filter(school_id=selected_school2).first(), "school_name", None)
                trend_data = {
                    'years': years_data,
                    'values': values,
                    'values2': values2,
                    'yLabel': attr,
                    'school1_name': school1_name,
                    'school2_name': school2_name
                }
                print(trend_data)
                context['trend_data_json'] = json.dumps(trend_data)
    elif selected_cat == "enroll_low_income":
        if LowIncomePercentPubSchool.objects.filter(school_id=selected_school).exists() and LowIncomePercentPubSchool.objects.filter(school_id=selected_school2).exists():
                years = LowIncomePercentPubSchool.objects.filter(school_id=selected_school).values('school_year').distinct()
                years_data = [item['school_year'] for item in years]
                values = []
                values2 = []
                for year in years_data:
                    record = LowIncomePercentPubSchool.objects.filter(school_id=selected_school, school_year=year).first()
                    record2 = LowIncomePercentPubSchool.objects.filter(school_id=selected_school2, school_year=year).first()

                    if record:
                        value = getattr(record, attr, None)
                        values.append(value)
                    else:
                        values.append(None)

                    if record2:
                        value2 = getattr(record2, attr, None)
                        values2.append(value2)
                    else:
                        values2.append(None)

                school1_name = getattr(School.objects.filter(school_id=selected_school).first(), "school_name", None)
                school2_name = getattr(School.objects.filter(school_id=selected_school2).first(), "school_name", None)
                trend_data = {
                    'years': years_data,
                    'values': values,
                    'values2': values2,
                    'yLabel': attr,
                    'school1_name': school1_name,
                    'school2_name': school2_name
                }
                print(trend_data)
                context['trend_data_json'] = json.dumps(trend_data)
    elif selected_cat == "pub_school_grad_rates":
        if PublicSchoolGradRatesSchool.objects.filter(school_id=selected_school).exists() and PublicSchoolGradRatesSchool.objects.filter(school_id=selected_school2).exists():
                years = PublicSchoolGradRatesSchool.objects.filter(school_id=selected_school).values('school_year').distinct()
                years_data = [item['school_year'] for item in years]
                values = []
                values2 = []
                for year in years_data:
                    record = PublicSchoolGradRatesSchool.objects.filter(school_id=selected_school, school_year=year).first()
                    record2 = PublicSchoolGradRatesSchool.objects.filter(school_id=selected_school2, school_year=year).first()

                    if record:
                        value = getattr(record, attr, None)
                        values.append(value)
                    else:
                        values.append(None)

                    if record2:
                        value2 = getattr(record2, attr, None)
                        values2.append(value2)
                    else:
                        values2.append(None)

                school1_name = getattr(School.objects.filter(school_id=selected_school).first(), "school_name", None)
                school2_name = getattr(School.objects.filter(school_id=selected_school2).first(), "school_name", None)
                trend_data = {
                    'years': years_data,
                    'values': values,
                    'values2': values2,
                    'yLabel': attr,
                    'school1_name': school1_name,
                    'school2_name': school2_name
                }
                print(trend_data)
                context['trend_data_json'] = json.dumps(trend_data)
    else:
        pass

def trend_graph_create_district(district_aun, context, selected_cat, attr):
    if selected_cat == "demographic":

        demo_attr = ["per_asian", "per_hispanic", "per_pacific_islander", "per_am_indian_or_alaskan_native", "per_african_american", "per_white", "per_two_or_more_races"]
        extra_demo_attr = ["per_english_learner", "per_special_education", "per_gifted_student", "per_military_connected", "per_foster_care", "per_economically_disadvantaged", "per_homeless"]
        gender_attr = ["male", "female"]

        if attr in demo_attr:
            if DistrictDemographic.objects.filter(district=district_aun).exists():
                years = DistrictDemographic.objects.filter(district=district_aun).values('school_year').distinct()
                years_data = [item['school_year'] for item in years]
                values = []
                for year in years_data:
                    record = DistrictDemographic.objects.filter(district=district_aun, school_year=year).first()

                    if record:
                        value = getattr(record, attr, None)
                        values.append(value)
                    else:
                        values.append(None)
                trend_data = {
                    'years': years_data,
                    'values': values,
                    'yLabel': attr
                }
                context['trend_data_json'] = json.dumps(trend_data)
        if attr in extra_demo_attr:
            if ExtraDemoDistrict.objects.filter(district=district_aun).exists():
                years = ExtraDemoDistrict.objects.filter(district=district_aun).values('school_year').distinct()
                years_data = [item['school_year'] for item in years]
                values = []
                for year in years_data:
                    record = ExtraDemoDistrict.objects.filter(district=district_aun, school_year=year).first()

                    if record:
                        value = getattr(record, attr, None)
                        values.append(value)
                    else:
                        values.append(None)
                trend_data = {
                    'years': years_data,
                    'values': values,
                    'yLabel': attr
                }
                context['trend_data_json'] = json.dumps(trend_data)
        if attr in gender_attr:
            if GenderDistrict.objects.filter(district=district_aun).exists():
                years = GenderDistrict.objects.filter(district=district_aun).values('school_year').distinct()
                years_data = [item['school_year'] for item in years]
                values = []
                for year in years_data:
                    record = GenderDistrict.objects.filter(district=district_aun, school_year=year).first()

                    if record:
                        value = getattr(record, attr, None)
                        values.append(value)
                    else:
                        values.append(None)
                trend_data = {
                    'years': years_data,
                    'values': values,
                    'yLabel': attr
                }
                context['trend_data_json'] = json.dumps(trend_data)
    elif selected_cat == "fiscal":
        if DistrictFiscalData.objects.filter(district=district_aun).exists():
            years = DistrictFiscalData.objects.filter(district=district_aun).values('school_year').distinct()
            years_data = [item['school_year'] for item in years]
            print(attr)
            values = []
            for year in years_data:
                record = DistrictFiscalData.objects.filter(district=district_aun, school_year=year).first()

                if record:
                    value = getattr(record, attr, None)
                    values.append(value)
                else:
                    values.append(None)

            trend_data = {
                'years': years_data,
                'values': values,
                'yLabel': attr
            }
            context['trend_data_json'] = json.dumps(trend_data)
    elif selected_cat == "aid_ratio":
        if AidRatio.objects.filter(district=district_aun).exists():
            years = AidRatio.objects.filter(district=district_aun).values('school_year').distinct()
            years_data = [item['school_year'] for item in years]
            print(attr)
            values = []
            for year in years_data:
                record = AidRatio.objects.filter(district=district_aun, school_year=year).first()

                if record:
                    value = getattr(record, attr, None)
                    values.append(value)
                else:
                    values.append(None)

            trend_data = {
                'years': years_data,
                'values': values,
                'yLabel': attr
            }
            context['trend_data_json'] = json.dumps(trend_data)
    elif selected_cat == "personal_income":
        if PersonalIncome.objects.filter(district=district_aun).exists():
            years = PersonalIncome.objects.filter(district=district_aun).values('school_year').distinct()
            years_data = [item['school_year'] for item in years]
            print(attr)
            values = []
            for year in years_data:
                record = PersonalIncome.objects.filter(district=district_aun, school_year=year).first()

                if record:
                    value = getattr(record, attr, None)
                    values.append(value)
                else:
                    values.append(None)

            trend_data = {
                'years': years_data,
                'values': values,
                'yLabel': attr
            }
            context['trend_data_json'] = json.dumps(trend_data)

def trend_graph_create(school_id, context, selected_cat, attr):
    if selected_cat == "demographic":

        demo_attr = ["per_asian", "per_hispanic", "per_pacific_islander", "per_am_indian_or_alaskan_native", "per_african_american", "per_white", "per_two_or_more_races"]
        extra_demo_attr = ["per_english_learner", "per_special_education", "per_gifted_student", "per_military_connected", "per_foster_care", "per_economically_disadvantaged", "per_homeless"]
        gender_attr = ["male", "female"]

        if attr in demo_attr:
            if SchoolDemographic.objects.filter(school_id=school_id).exists():
                years = SchoolDemographic.objects.filter(school_id=school_id).values('school_year').distinct()
                years_data = [item['school_year'] for item in years]
                values = []
                for year in years_data:
                    record = SchoolDemographic.objects.filter(school_id=school_id, school_year=year).first()

                    if record:
                        value = getattr(record, attr, None)
                        values.append(value)
                    else:
                        values.append(None)
                trend_data = {
                    'years': years_data,
                    'values': values,
                    'yLabel': attr
                }
                context['trend_data_json'] = json.dumps(trend_data)
        if attr in extra_demo_attr:
            if ExtraDemoSchool.objects.filter(school_id=school_id).exists():
                years = ExtraDemoSchool.objects.filter(school_id=school_id).values('school_year').distinct()
                years_data = [item['school_year'] for item in years]
                values = []
                for year in years_data:
                    record = ExtraDemoSchool.objects.filter(school_id=school_id, school_year=year).first()

                    if record:
                        value = getattr(record, attr, None)
                        values.append(value)
                    else:
                        values.append(None)
                trend_data = {
                    'years': years_data,
                    'values': values,
                    'yLabel': attr
                }
                context['trend_data_json'] = json.dumps(trend_data)
        if attr in gender_attr:
            if GenderSchool.objects.filter(school_id=school_id).exists():
                years = GenderSchool.objects.filter(school_id=school_id).values('school_year').distinct()
                years_data = [item['school_year'] for item in years]
                values = []
                for year in years_data:
                    record = GenderSchool.objects.filter(school_id=school_id, school_year=year).first()

                    if record:
                        value = getattr(record, attr, None)
                        values.append(value)
                    else:
                        values.append(None)
                trend_data = {
                    'years': years_data,
                    'values': values,
                    'yLabel': attr
                }
                context['trend_data_json'] = json.dumps(trend_data)
    elif selected_cat == "fiscal":
        if SchoolFiscalData.objects.filter(school_id=school_id).exists():
            years = SchoolFiscalData.objects.filter(school_id=school_id).values('school_year').distinct()
            years_data = [item['school_year'] for item in years]
            print(attr)
            values = []
            for year in years_data:
                record = SchoolFiscalData.objects.filter(school_id=school_id, school_year=year).first()

                if record:
                    value = getattr(record, attr, None)
                    values.append(value)
                else:
                    values.append(None)

            trend_data = {
                'years': years_data,
                'values': values,
                'yLabel': attr
            }
            context['trend_data_json'] = json.dumps(trend_data)
    elif selected_cat == "enroll_low_income":
        if LowIncomePercentPubSchool.objects.filter(school_id=school_id).exists():
            years = LowIncomePercentPubSchool.objects.filter(school_id=school_id).values('school_year').distinct()
            years_data = [item['school_year'] for item in years]
            print(attr)
            values = []
            for year in years_data:
                record = LowIncomePercentPubSchool.objects.filter(school_id=school_id, school_year=year).first()

                if record:
                    value = getattr(record, attr, None)
                    values.append(value)
                else:
                    values.append(None)

            trend_data = {
                'years': years_data,
                'values': values,
                'yLabel': attr
            }
            context['trend_data_json'] = json.dumps(trend_data)
    elif selected_cat == "pub_school_grad_rates":
        if PublicSchoolGradRatesSchool.objects.filter(school_id=school_id).exists():
            years = PublicSchoolGradRatesSchool.objects.filter(school_id=school_id).values('school_year').distinct()
            years_data = [item['school_year'] for item in years]
            print(attr)
            values = []
            for year in years_data:
                record = PublicSchoolGradRatesSchool.objects.filter(school_id=school_id, school_year=year).first()

                if record:
                    value = getattr(record, attr, None)
                    values.append(value)
                else:
                    values.append(None)

            trend_data = {
                'years': years_data,
                'values': values,
                'yLabel': attr
            }
            context['trend_data_json'] = json.dumps(trend_data)
    else:
        pass

def table_create_enroll_low_income(school_id, selected_year, context, add):
    if selected_year != "all-years":
        #School Demographic
        if LowIncomePercentPubSchool.objects.filter(school_year=selected_year, school_id=school_id).exists():
            cat_info = LowIncomePercentPubSchool.objects.get(school_year=selected_year, school_id=school_id)

            fields = []
            fields_pairing = dict()
            i = 0
            for field in LowIncomePercentPubSchool._meta.get_fields():
                if not field.is_relation and i != 0:
                    fields.append(field.verbose_name)
                    if i != 2:
                        fields_pairing.update({field.verbose_name: field.name})
                i = i + 1
            context[f'cat_headers{add}'] = fields
            context[f'attributes{add}'] = fields_pairing

            cat_info_dict = cat_info.__dict__
            good_cat_info_dict = dict(islice(cat_info_dict.items(), 3, None))
            context[f'cat_info{add}'] = good_cat_info_dict.values()
            context['table_name'] = 'Low Income Enrollment'
    else:
        if LowIncomePercentPubSchool.objects.filter(school_id=school_id).exists():
            cat_info = LowIncomePercentPubSchool.objects.filter(school_id=school_id)

            fields = []
            fields_pairing = dict()

            i = 0
            for field in LowIncomePercentPubSchool._meta.get_fields():
                if not field.is_relation and i != 0:
                    fields.append(field.verbose_name)
                    if i != 2:
                        fields_pairing.update({field.verbose_name: field.name})
                i = i + 1
            context[f'cat_headers{add}'] = fields
            context[f'attributes{add}'] = fields_pairing.items()

            cat_info_list = []
            cat_info_headers = []

            i = 0
            for info in cat_info:
                cat_info_dict = info.__dict__
                good_cat_info_dict = dict(islice(cat_info_dict.items(), 3, None))
                cat_info_list.append(good_cat_info_dict)

            context[f'cat_info{add}'] = cat_info_list
            context['table_name'] = 'Low Income Enrollment'

def table_create_demographics(school_id, selected_year, context, add):
    if selected_year != "all-years":
        #School Demographic
        if SchoolDemographic.objects.filter(school_year=selected_year, school_id=school_id).exists():
            cat_info = SchoolDemographic.objects.get(school_year=selected_year, school_id=school_id)

            fields = []
            fields_pairing = dict()
            i = 0
            for field in SchoolDemographic._meta.get_fields():
                if not field.is_relation and i != 0:
                    fields.append(field.verbose_name)
                    if i != 2:
                        fields_pairing.update({field.verbose_name: field.name})
                i = i + 1
            context[f'cat_headers{add}'] = fields
            context[f'attributes{add}'] = fields_pairing.items()

            cat_info_dict = cat_info.__dict__
            good_cat_info_dict = dict(islice(cat_info_dict.items(), 3, None))
            context[f'cat_info{add}'] = good_cat_info_dict.values()
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
            fields_pairing = dict()
            i = 0

            for field in ExtraDemoSchool._meta.get_fields():
                if not field.is_relation and i != 0:
                    fields.append(field.verbose_name)
                    if i != 2:
                        fields_pairing.update({field.verbose_name: field.name})
                i = i + 1
            context[f'cat_headers2{add}'] = fields
            context[f'attributes2{add}'] = fields_pairing.items()

            cat_info_dict2 = cat_info2.__dict__
            good_cat_info_dict2 = dict(islice(cat_info_dict2.items(), 3, None))
            context[f'cat_info2{add}'] = good_cat_info_dict2.values()
            context['table_name2'] = 'More Demographic Information'

        #Gender School
        if GenderSchool.objects.filter(school_year=selected_year, school_id=school_id).exists():
            cat_info3 = GenderSchool.objects.get(school_year=selected_year, school_id=school_id)

            fields = []
            fields_pairing = dict()

            i = 0
            for field in GenderSchool._meta.get_fields():
                if not field.is_relation and i != 0:
                    fields.append(field.verbose_name)
                    if i != 2:
                        fields_pairing.update({field.verbose_name: field.name})
                i = i + 1
            context[f'cat_headers3{add}'] = fields
            context[f'attributes3{add}'] = fields_pairing.items()

            cat_info_dict3 = cat_info3.__dict__
            good_cat_info_dict3 = dict(islice(cat_info_dict3.items(), 3, None))
            context[f'cat_info3{add}'] = good_cat_info_dict3.values()
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
            fields_pairing = dict()
            i = 0
            for field in SchoolDemographic._meta.get_fields():
                if not field.is_relation and i != 0:
                    fields.append(field.verbose_name)
                    if i != 2:
                        fields_pairing.update({field.verbose_name: field.name})
                i = i + 1
            context[f'cat_headers{add}'] = fields
            context[f'attributes{add}'] = fields_pairing.items()

            cat_info_list = []
            cat_info_headers = []

            i = 0
            for info in cat_info:
                cat_info_dict = info.__dict__
                good_cat_info_dict = dict(islice(cat_info_dict.items(), 3, None))
                cat_info_list.append(good_cat_info_dict)

            context[f'cat_info{add}'] = cat_info_list
            context['table_name'] = 'Demographic Information'

        #Extra Demographic
        if ExtraDemoSchool.objects.filter(school_id=school_id).exists():
            cat_info2 = ExtraDemoSchool.objects.filter(school_id=school_id)

            fields = []
            fields_pairing = dict()

            i = 0
            for field in ExtraDemoSchool._meta.get_fields():
                if not field.is_relation and i != 0:
                    fields.append(field.verbose_name)
                    if i != 2:
                        fields_pairing.update({field.verbose_name: field.name})
                i = i + 1
            context[f'cat_headers2{add}'] = fields
            context[f'attributes2{add}'] = fields_pairing.items()

            cat_info_list2 = []
            cat_info_headers2 = []

            i = 0
            for info in cat_info2:
                cat_info_dict2 = info.__dict__
                good_cat_info_dict2 = dict(islice(cat_info_dict2.items(), 3, None))
                cat_info_list2.append(good_cat_info_dict2)

            context[f'cat_info2{add}'] = cat_info_list2
            context['table_name2'] = 'More Demographic Information'

        #Gender School
        if GenderSchool.objects.filter(school_id=school_id).exists():
            cat_info3 = GenderSchool.objects.filter(school_id=school_id)

            fields = []
            fields_pairing = dict()

            i = 0
            for field in GenderSchool._meta.get_fields():
                if not field.is_relation and i != 0:
                    fields.append(field.verbose_name)
                    if i != 2:
                        fields_pairing.update({field.verbose_name: field.name})
                i = i + 1
            context[f'cat_headers3{add}'] = fields
            context[f'attributes3{add}'] = fields_pairing.items()

            cat_info_list3 = []
            cat_info_headers3 = []

            i = 0
            for info in cat_info3:
                cat_info_dict3 = info.__dict__
                good_cat_info_dict3 = dict(islice(cat_info_dict3.items(), 3, None))
                cat_info_list3.append(good_cat_info_dict3)

            context[f'cat_info3{add}'] = cat_info_list3
            context['table_name3'] = 'Gender Information'

def table_create_demographics_district(district_aun, selected_year, context, add):
    if selected_year != "all-years":
        #School Demographic
        if DistrictDemographic.objects.filter(school_year=selected_year, district=district_aun).exists():
            cat_info = DistrictDemographic.objects.get(school_year=selected_year, district=district_aun)

            fields = []
            fields_pairing = dict()

            i = 0
            for field in DistrictDemographic._meta.get_fields():
                if not field.is_relation and i != 0:
                    fields.append(field.verbose_name)
                    if i != 2:
                        fields_pairing.update({field.verbose_name: field.name})
                i = i + 1
            context[f'cat_headers{add}'] = fields
            context[f'attributes{add}'] = fields_pairing.items()

            cat_info_dict = cat_info.__dict__
            good_cat_info_dict = dict(islice(cat_info_dict.items(), 3, None))
            context[f'cat_info{add}'] = good_cat_info_dict.values()
            context['table_name'] = 'Demographic Information'

        #Extra Demographic
        if ExtraDemoDistrict.objects.filter(school_year=selected_year, district=district_aun).exists():
            cat_info2 = ExtraDemoDistrict.objects.get(school_year=selected_year, district=district_aun)

            fields = []
            fields_pairing = dict()

            i = 0
            for field in ExtraDemoDistrict._meta.get_fields():
                if not field.is_relation and i != 0:
                    fields.append(field.verbose_name)
                    if i != 2:
                        fields_pairing.update({field.verbose_name: field.name})
                i = i + 1
            context[f'cat_headers2{add}'] = fields
            context[f'attributes2{add}'] = fields_pairing.items()

            cat_info_dict2 = cat_info2.__dict__
            good_cat_info_dict2 = dict(islice(cat_info_dict2.items(), 3, None))
            context[f'cat_info2{add}'] = good_cat_info_dict2.values()
            context[f'table_name2{add}'] = 'More Demographic Information'

        #Gender School
        if GenderDistrict.objects.filter(school_year=selected_year, district=district_aun).exists():
            cat_info3 = GenderDistrict.objects.get(school_year=selected_year, district=district_aun)

            fields = []
            fields_pairing = dict()

            i = 0
            for field in GenderDistrict._meta.get_fields():
                if not field.is_relation and i != 0:
                    fields.append(field.verbose_name)
                    if i != 2:
                        fields_pairing.update({field.verbose_name: field.name})
                i = i + 1
            context[f'cat_headers3{add}'] = fields
            context[f'attributes3{add}'] = fields_pairing.items()

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
            fields_pairing = dict()

            i = 0
            for field in DistrictDemographic._meta.get_fields():
                if not field.is_relation and i != 0:
                    fields.append(field.verbose_name)
                    if i != 2:
                        fields_pairing.update({field.verbose_name: field.name})
                i = i + 1
            context[f'cat_headers{add}'] = fields
            context[f'attributes{add}'] = fields_pairing.items()

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
            fields_pairing = dict()

            i = 0
            for field in ExtraDemoDistrict._meta.get_fields():
                if not field.is_relation and i != 0:
                    fields.append(field.verbose_name)
                    if i != 2:
                        fields_pairing.update({field.verbose_name: field.name})
                i = i + 1
            context[f'cat_headers2{add}'] = fields
            context[f'attributes2{add}'] = fields_pairing.items()

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
            fields_pairing = dict()

            i = 0
            for field in GenderDistrict._meta.get_fields():
                if not field.is_relation and i != 0:
                    fields.append(field.verbose_name)
                    if i != 2:
                        fields_pairing.update({field.verbose_name: field.name})
                i = i + 1
            context[f'cat_headers3{add}'] = fields
            context[f'attributes3{add}'] = fields_pairing.items()

            cat_info_list3 = []
            cat_info_headers3 = []

            i = 0
            for info in cat_info3:
                cat_info_dict3 = info.__dict__
                good_cat_info_dict3 = dict(islice(cat_info_dict3.items(), 3, None))
                cat_info_list3.append(good_cat_info_dict3)

            context[f'cat_info3{add}'] = cat_info_list3
            context[f'table_name3{add}'] = 'Gender Information'

def table_create_fiscal(school_id, selected_year, context, add):
    if selected_year != "all-years":
        #School Demographic
        if SchoolFiscalData.objects.filter(school_year=selected_year, school_id=school_id).exists():
            cat_info = SchoolFiscalData.objects.get(school_year=selected_year, school_id=school_id)

            fields = []
            fields_pairing = dict()

            i = 0
            for field in SchoolFiscalData._meta.get_fields():
                if not field.is_relation and i != 0:
                    fields.append(field.verbose_name)
                    if i != 2:
                        fields_pairing.update({field.verbose_name: field.name})
                i = i + 1
            context[f'cat_headers{add}'] = fields
            context[f'attributes{add}'] = fields_pairing.items()

            cat_info_dict = cat_info.__dict__
            good_cat_info_dict = dict(islice(cat_info_dict.items(), 3, None))
            context[f'cat_info{add}'] = good_cat_info_dict.values()
            context['table_name'] = 'Fiscal Information'
    else:
        if SchoolFiscalData.objects.filter(school_id=school_id).exists():
            cat_info = SchoolFiscalData.objects.filter(school_id=school_id)

            fields = []
            fields_pairing = dict()

            i = 0
            for field in SchoolFiscalData._meta.get_fields():
                if not field.is_relation and i != 0:
                    fields.append(field.verbose_name)
                    if i != 2:
                        fields_pairing.update({field.verbose_name: field.name})
                i = i + 1
            context[f'cat_headers{add}'] = fields
            context[f'attributes{add}'] = fields_pairing.items()

            cat_info_list = []
            cat_info_headers = []

            i = 0
            for info in cat_info:
                cat_info_dict = info.__dict__
                good_cat_info_dict = dict(islice(cat_info_dict.items(), 3, None))
                cat_info_list.append(good_cat_info_dict)

            context[f'cat_info{add}'] = cat_info_list
            context['table_name'] = 'Fiscal Information'

def table_create_fiscal_district(district_aun, selected_year, context, add):
    if selected_year != "all-years":
        #School Demographic
        if DistrictFiscalData.objects.filter(school_year=selected_year, district=district_aun).exists():
            cat_info = DistrictFiscalData.objects.get(school_year=selected_year, district=district_aun)

            fields = []
            fields_pairing = dict()

            i = 0
            for field in DistrictFiscalData._meta.get_fields():
                if not field.is_relation and i != 0:
                    fields.append(field.verbose_name)
                    if i != 2:
                        fields_pairing.update({field.verbose_name: field.name})
                i = i + 1
            context[f'cat_headers{add}'] = fields
            context[f'attributes{add}'] = fields_pairing.items()

            cat_info_dict = cat_info.__dict__
            good_cat_info_dict = dict(islice(cat_info_dict.items(), 3, None))
            context[f'cat_info{add}'] = good_cat_info_dict.values()
            context['table_name'] = 'Fiscal Information'
    else:
        if DistrictFiscalData.objects.filter(district=district_aun).exists():
            cat_info = DistrictFiscalData.objects.filter(district=district_aun)

            fields = []
            fields_pairing = dict()

            i = 0
            for field in DistrictFiscalData._meta.get_fields():
                if not field.is_relation and i != 0:
                    fields.append(field.verbose_name)
                    if i != 2:
                        fields_pairing.update({field.verbose_name: field.name})
                i = i + 1
            context[f'cat_headers{add}'] = fields
            context[f'attributes{add}'] = fields_pairing.items()

            cat_info_list = []
            cat_info_headers = []

            i = 0
            for info in cat_info:
                cat_info_dict = info.__dict__
                good_cat_info_dict = dict(islice(cat_info_dict.items(), 3, None))
                cat_info_list.append(good_cat_info_dict)

            context[f'cat_info{add}'] = cat_info_list
            context['table_name'] = 'Fiscal Information'

def table_create_pub_school_grad_rates(school_id, selected_year, context, add):
    if selected_year != "all-years":
        #School Demographic
        if PublicSchoolGradRatesSchool.objects.filter(school_year=selected_year, school_id=school_id).exists():
            cat_info = PublicSchoolGradRatesSchool.objects.get(school_year=selected_year, school_id=school_id)

            fields = []
            fields_pairing = dict()

            i = 0
            for field in PublicSchoolGradRatesSchool._meta.get_fields():
                if not field.is_relation and i != 0:
                    fields.append(field.verbose_name)
                    if i != 2:
                        fields_pairing.update({field.verbose_name: field.name})
                i = i + 1
            context[f'cat_headers{add}'] = fields
            context[f'attributes{add}'] = fields_pairing.items()

            cat_info_dict = cat_info.__dict__
            good_cat_info_dict = dict(islice(cat_info_dict.items(), 3, None))
            context[f'cat_info{add}'] = good_cat_info_dict.values()
            context['table_name'] = 'Public School Graduation Rates'
    else:
        if PublicSchoolGradRatesSchool.objects.filter(school_id=school_id).exists():
            cat_info = PublicSchoolGradRatesSchool.objects.filter(school_id=school_id)

            fields = []
            fields_pairing = dict()

            i = 0
            for field in PublicSchoolGradRatesSchool._meta.get_fields():
                if not field.is_relation and i != 0:
                    fields.append(field.verbose_name)
                    if i != 2:
                        fields_pairing.update({field.verbose_name: field.name})
                i = i + 1
            context[f'cat_headers{add}'] = fields
            context[f'attributes{add}'] = fields_pairing.items()

            cat_info_list = []
            cat_info_headers = []

            i = 0
            for info in cat_info:
                cat_info_dict = info.__dict__
                good_cat_info_dict = dict(islice(cat_info_dict.items(), 3, None))
                cat_info_list.append(good_cat_info_dict)

            context[f'cat_info{add}'] = cat_info_list
            context['table_name'] = 'Public School Graduation Rates'

def table_create_aid_ratio_district(district_aun, selected_year, context, add):
    if selected_year != "all-years":
        #School Demographic
        if AidRatio.objects.filter(school_year=selected_year, district=district_aun).exists():
            cat_info = AidRatio.objects.get(school_year=selected_year, district=district_aun)

            fields = []
            fields_pairing = dict()

            i = 0
            for field in AidRatio._meta.get_fields():
                if not field.is_relation and i != 0:
                    fields.append(field.verbose_name)
                    if i != 2:
                        fields_pairing.update({field.verbose_name: field.name})
                i = i + 1
            context[f'cat_headers{add}'] = fields
            context[f'attributes{add}'] = fields_pairing.items()

            cat_info_dict = cat_info.__dict__
            good_cat_info_dict = dict(islice(cat_info_dict.items(), 3, None))
            context[f'cat_info{add}'] = good_cat_info_dict.values()
            context['table_name'] = 'Fiscal Information'
    else:
        if AidRatio.objects.filter(district=district_aun).exists():
            cat_info = AidRatio.objects.filter(district=district_aun)

            fields = []
            fields_pairing = dict()

            i = 0
            for field in AidRatio._meta.get_fields():
                if not field.is_relation and i != 0:
                    fields.append(field.verbose_name)
                    if i != 2:
                        fields_pairing.update({field.verbose_name: field.name})
                i = i + 1
            context[f'cat_headers{add}'] = fields
            context[f'attributes{add}'] = fields_pairing.items()

            cat_info_list = []
            cat_info_headers = []

            i = 0
            for info in cat_info:
                cat_info_dict = info.__dict__
                good_cat_info_dict = dict(islice(cat_info_dict.items(), 3, None))
                cat_info_list.append(good_cat_info_dict)

            context[f'cat_info{add}'] = cat_info_list
            context['table_name'] = 'Aid Ratios'

def table_create_personal_income_district(district_aun, selected_year, context, add):
    if selected_year != "all-years":
        #School Demographic
        if PersonalIncome.objects.filter(school_year=selected_year, district=district_aun).exists():
            cat_info = PersonalIncome.objects.get(school_year=selected_year, district=district_aun)

            fields = []
            fields_pairing = dict()

            i = 0
            for field in PersonalIncome._meta.get_fields():
                if not field.is_relation and i != 0:
                    fields.append(field.verbose_name)
                    if i != 2:
                        fields_pairing.update({field.verbose_name: field.name})
                i = i + 1
            context[f'cat_headers{add}'] = fields
            context[f'attributes{add}'] = fields_pairing.items()

            cat_info_dict = cat_info.__dict__
            good_cat_info_dict = dict(islice(cat_info_dict.items(), 3, None))
            context[f'cat_info{add}'] = good_cat_info_dict.values()
            context['table_name'] = 'Personal Income'
    else:
        if PersonalIncome.objects.filter(district=district_aun).exists():
            cat_info = AidRatio.objects.filter(district=district_aun)

            fields = []
            fields_pairing = dict()

            i = 0
            for field in PersonalIncome._meta.get_fields():
                if not field.is_relation and i != 0:
                    fields.append(field.verbose_name)
                    if i != 2:
                        fields_pairing.update({field.verbose_name: field.name})
                i = i + 1
            context[f'cat_headers{add}'] = fields
            context[f'attributes{add}'] = fields_pairing.items()

            cat_info_list = []
            cat_info_headers = []

            i = 0
            for info in cat_info:
                cat_info_dict = info.__dict__
                good_cat_info_dict = dict(islice(cat_info_dict.items(), 3, None))
                cat_info_list.append(good_cat_info_dict)

            context[f'cat_info{add}'] = cat_info_list
            context['table_name'] = 'Personal Income'