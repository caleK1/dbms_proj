from django.core.management.base import BaseCommand
from proj_display.models import School
from proj_display.models import SchoolInfo
from proj_display.models import GenderSchool
from proj_display.models import SchoolDemographic
from proj_display.models import ExtraDemoSchool
import pandas as pd


# Use this command formatting to upload data from database using python3 manage.py <name> from terminal
class Command(BaseCommand):
    help = 'Imports fast facts to the database'

    # Handle does the work in the Command
    def handle(self, *args, **kwargs):
        #School Info stays the same so we will use the most recent information
        df = pd.read_csv('/Users/calek/DBMS/dbms_proj/data/SchoolFastFacts/SchoolFastFacts_20222023_cleaned.csv')

        school_info = []
        SchoolInfo.objects.all().delete()
        for index, row in df.iterrows():
            try:
                school = School.objects.get(school_id=row['Schl'])

                #Title 1 school should be a boolean value
                if row['Title I School'] == "Yes":
                    title_1_val = True
                else:
                    title_1_val = False

                school_info.append(SchoolInfo(
                    school_id=school,
                    street_address=row['School Address (Street)'],
                    city_address=row['School Address (City)'],
                    zip_code=row['School Zip Code'],
                    website=row['Website'],
                    phone_num=row['Telephone Number'],
                    grades_offered=row['Grades Offered'],
                    title_1=title_1_val
                ))
            except School.DoesNotExist:
                print(f"Couldn't find {row['Schl']} at index {index}")
            except Exception as e:
                print(f"Error at index {index}: {str(e)}") 

        SchoolInfo.objects.bulk_create(school_info)
        
        #Iterate through years avaliable
        GenderSchool.objects.all().delete()
        SchoolDemographic.objects.all().delete()
        ExtraDemoSchool.objects.all().delete()
        years = ['20172018', '20182019', '20192020', '20202021', '20222023']
        gender_school = []
        school_demographic = []
        extra_demo_school = []
        for year in years:
            df = pd.read_csv(f'/Users/calek/DBMS/dbms_proj/data/SchoolFastFacts/SchoolFastFacts_{year}_cleaned.csv')

            for index, row in df.iterrows():
                try:
                    school_year = School.objects.get(school_id=row['Schl'])

                    gender_school.append(GenderSchool(
                        school_id=school_year,
                        school_year=year,
                        male=row['Male (School)'] if pd.notnull(row['Male (School)']) else 0,
                        female=row['Female (School)'] if pd.notnull(row['Female (School)']) else 0
                    ))

                    school_demographic.append(SchoolDemographic(
                        school_id=school_year,
                        school_year=year,
                        per_asian=row['Asian - Percent Enrollment by Race/Ethnicity'] if pd.notnull(row['Asian - Percent Enrollment by Race/Ethnicity']) else 0,
                        per_hispanic=row['Hispanic - Percent Enrollment by Race/Ethnicity'] if pd.notnull(row['Hispanic - Percent Enrollment by Race/Ethnicity']) else 0,
                        per_pacific_islander=row['Native Hawaiian or other Pacific Islander - Percent Enrollment by Race/Ethnicity'] if pd.notnull(row['Native Hawaiian or other Pacific Islander - Percent Enrollment by Race/Ethnicity']) else 0,
                        per_am_indian_or_alaskan_native=row['American Indian/Alaskan Native - Percent Enrollment by Race/Ethnicity'] if pd.notnull(row['American Indian/Alaskan Native - Percent Enrollment by Race/Ethnicity']) else 0,
                        per_african_american=row['Black/African American - Percent Enrollment by Race/Ethnicity'] if pd.notnull(row['Black/African American - Percent Enrollment by Race/Ethnicity']) else 0,
                        per_white=row['White - Percent Enrollment by Race/Ethnicity'] if pd.notnull(row['White - Percent Enrollment by Race/Ethnicity']) else 0,
                        per_two_or_more_races= row['2 or More Races - Percent Enrollment by Race/Ethnicity'] if pd.notnull(row['2 or More Races - Percent Enrollment by Race/Ethnicity']) else 0
                    ))

                    extra_demo_school.append(ExtraDemoSchool(
                        school_id=school_year,
                        school_year=year,
                        per_english_learner=row['English Learner - Percent Enrollment by Student Groups'] if pd.notnull(row['English Learner - Percent Enrollment by Student Groups']) else 0,
                        per_special_education=row['Special Education - Percent Enrollment by Student Groups'] if pd.notnull(row['Special Education - Percent Enrollment by Student Groups']) else 0,
                        per_gifted_student=row['Percent of Gifted Students'] if pd.notnull(row['Percent of Gifted Students']) else 0,
                        per_military_connected=row['Military Connected - Percent Enrollment by Student Groups'] if pd.notnull(row['Military Connected - Percent Enrollment by Student Groups']) else 0,
                        per_foster_care=row['Foster Care - Percent Enrollment by Student Groups'] if pd.notnull(row['Foster Care - Percent Enrollment by Student Groups']) else 0,
                        per_economically_disadvantaged=row['Economically Disadvantaged - Percent Enrollment by Student Groups'] if pd.notnull(row['Economically Disadvantaged - Percent Enrollment by Student Groups']) else 0,
                        per_homeless=row['Homeless - Percent Enrollment by Student Groups'] if pd.notnull(row['Homeless - Percent Enrollment by Student Groups']) else 0
                    ))

                except School.DoesNotExist:
                    print(f"Couldn't find {row['Schl']} at index {index}")
                except Exception as e:
                    print(f"Error at index {index}: {str(e)}") 

        GenderSchool.objects.bulk_create(gender_school)
        SchoolDemographic.objects.bulk_create(school_demographic)
        ExtraDemoSchool.objects.bulk_create(extra_demo_school)

