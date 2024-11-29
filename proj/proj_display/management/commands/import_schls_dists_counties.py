from django.core.management.base import BaseCommand
from proj_display.models import County
from proj_display.models import District
from proj_display.models import School
import pandas as pd


# Use this command formatting to upload data from database using python3 manage.py <name> from terminal
class Command(BaseCommand):
    help = 'Imports counties to the database'

    # Handle does the work in the Command
    def handle(self, *args, **kwargs):
        # Would need to change to make it your directory
        df = pd.read_csv('/Users/calek/DBMS/dbms_proj/data/EnrollmentPublic/Enrollment_Public_Schools_2022_23.csv')

        #Add all instances of unique counties
        county_names = df['County'].unique()

        #Take off the last element 'nan'
        county_names = county_names[:-1]

        #Delete all existing data in the County table to not duplicate
        County.objects.all().delete()

        #Create the County objects
        counties = []
        for county in county_names:
        	counties.append(County(county_name=county))

       	#Bulk add those objects into the database
        County.objects.bulk_create(counties)

        District.objects.all().delete()

        #Add Districts
        districts = []

        #iterate through all the rows in the file
        for index, row in df.iterrows():
        	try:
        		# Check if 'district_aun' doesn't exist
        		if pd.isna(row['AUN']):
        			print(f"Skipping district with blank AUN at index {index}")
        			continue  # Skip this row and move to the next one

        		#Match the county to the existing county objects
        		county = County.objects.get(county_name=row['County'])

        		#Create the district object
        		districts.append(District(district_aun=row['AUN'], district_name=row['LEA Name'], county_id=county))

        	#Error checking
        	except County.DoesNotExist:
        		print(f"Couldn't find {row['County']} at index {index}")
        	except Exception as e:
        		print(f"Error at index {index}: {str(e)}")

        #Put all the districts into the database
        District.objects.bulk_create(districts)
       
        #Get schools
        df_schools = pd.read_csv('/Users/calek/DBMS/dbms_proj/data/EnrollmentPublic/Enrollment_Public_Schools_2022_23_schls_cleaned.csv')
        
        School.objects.all().delete()

        schools = []

        for index, row in df_schools.iterrows():
        	try:
        		if pd.isna(row['School Number']):
        			print(f"Skipping school with blank id at index {index}")
        			continue

        		schls_district = District.objects.get(district_aun=row['AUN'])

        		schools.append(School(school_id=row['School Number'], school_name=row['School Name'], district_aun=schls_district))

        	except District.DoesNotExist:
        		print(f"Couldn't find {row['AUN']} at index {index}")
        	except Exception as e:
        		print(f"Error at index {index}: {str(e)}")  

        School.objects.bulk_create(schools)