from django.core.management.base import BaseCommand
from proj_display.models import District
from proj_display.models import DistrictInfo
from proj_display.models import GenderDistrict
from proj_display.models import DistrictDemographic
from proj_display.models import ExtraDemoDistrict
import pandas as pd


# Use this command formatting to upload data from database using python3 manage.py <name> from terminal
class Command(BaseCommand):

    # Handle does the work in the Command
    def handle(self, *args, **kwargs):
        #School Info stays the same so we will use the most recent information
        df = pd.read_csv('/Users/calek/DBMS/dbms_proj/data/DistrictFastFacts/DistrictFastFacts_20222023_cleaned.csv')

        district_info = []
        DistrictInfo.objects.all().delete()
        for index, row in df.iterrows():
            try:
                district = District.objects.get(district_aun=row['AUN'])

                district_info.append(DistrictInfo(
                    district=district,
                    c_and_t_web = row['Career and Technical Center Website'],
                    c_and_t_enrollment = row['Enrollment in Partnering Career and Technical Center(s)'] if pd.notnull(row['Enrollment in Partnering Career and Technical Center(s)']) else 0,
                    c_and_t_name = row['Career and Technical Center Name'],
                    imu_name = row['Intermediate Unit Name'],
                    imu_website = row['Intermediate Unit Website'],
                    street_address = row['District Address (Street)'],
                    city_address = row['District Address (City)'],
                    zip_code = row['District Zip Code'],
                    website = row['Website'],
                    phone_num = row['Telephone Number'],
                    grades_off = row['Grades Offered'],
                    num_schools = row['Number of Schools'],
                    geographic_size = row['Geographic Size of District (Square Miles)']
                ))
            except District.DoesNotExist:
                print(f"Couldn't find {row['AUN']} at index {index}")
            except Exception as e:
                print(f"Error at index {index}: {str(e)}") 

        DistrictInfo.objects.bulk_create(district_info)
        
        #Iterate through years avaliable
        GenderDistrict.objects.all().delete()
        DistrictDemographic.objects.all().delete()
        ExtraDemoDistrict.objects.all().delete()
        years = ['20172018', '20182019', '20192020', '20202021', '20212022', '20222023']
        gender_district = []
        district_demographic = []
        extra_demo_district = []
        for year in years:
            df = pd.read_csv(f'/Users/calek/DBMS/dbms_proj/data/DistrictFastFacts/DistrictFastFacts_{year}_cleaned.csv')

            for index, row in df.iterrows():
                try:
                    district_year = District.objects.get(district_aun=row['AUN'])

                    gender_district.append(GenderDistrict(
                        district=district_year,
                        school_year=year,
                        male=row['Male'] if pd.notnull(row['Male']) else 0,
                        female=row['Female'] if pd.notnull(row['Female']) else 0
                    ))

                    district_demographic.append(DistrictDemographic(
                        district=district_year,
                        school_year=year,
                        per_asian=row['Asian '] if pd.notnull(row['Asian ']) else 0,
                        per_hispanic=row['Hispanic '] if pd.notnull(row['Hispanic ']) else 0,
                        per_pacific_islander=row['Native Hawaiian or other Pacific Islander '] if pd.notnull(row['Native Hawaiian or other Pacific Islander ']) else 0,
                        per_am_indian_or_alaskan_native=row['American Indian/Alaskan Native '] if pd.notnull(row['American Indian/Alaskan Native ']) else 0,
                        per_african_american=row['Black/African American '] if pd.notnull(row['Black/African American ']) else 0,
                        per_white=row['White '] if pd.notnull(row['White ']) else 0,
                        per_two_or_more_races= row['2 or More Races'] if pd.notnull(row['2 or More Races']) else 0
                    ))

                    extra_demo_district.append(ExtraDemoDistrict(
                        district=district_year,
                        school_year=year,
                        per_english_learner=row['English Learner'] if pd.notnull(row['English Learner']) else 0,
                        per_special_education=row['Special Education'] if pd.notnull(row['Special Education']) else 0,
                        per_gifted_student=row['Percent of Gifted Students'] if pd.notnull(row['Percent of Gifted Students']) else 0,
                        per_military_connected=row['Military Connected'] if pd.notnull(row['Military Connected']) else 0,
                        per_foster_care=row['Foster Care'] if pd.notnull(row['Foster Care']) else 0,
                        per_economically_disadvantaged=row['Economically Disadvantaged'] if pd.notnull(row['Economically Disadvantaged']) else 0,
                        per_homeless=row['Homeless'] if pd.notnull(row['Homeless']) else 0
                    ))

                except District.DoesNotExist:
                    print(f"Couldn't find {row['AUN']} at index {index}")
                except Exception as e:
                    print(f"Error at index {index}: {str(e)}") 

        GenderDistrict.objects.bulk_create(gender_district)
        DistrictDemographic.objects.bulk_create(district_demographic)
        ExtraDemoDistrict.objects.bulk_create(extra_demo_district)