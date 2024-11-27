from django.core.management.base import BaseCommand
from proj_display.models import County
import pandas as pd


# Use this command formatting to upload data from database using python3 manage.py <name> from terminal
class Command(BaseCommand):
    help = 'Imports counties from the database'

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
        