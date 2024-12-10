from django.core.management.base import BaseCommand
from proj_display.models import School
from proj_display.models import SchoolFiscalData
import pandas as pd


class Command(BaseCommand):
    # Handle does the work in the Command
    def handle(self, *args, **kwargs):
        df = pd.read_csv('/Users/calek/DBMS/dbms_proj/data/SchoolFiscalData/School_Fiscal_Data_SY_20182019_cleaned.csv')

        school_fiscal = []
        SchoolFiscalData.objects.all().delete()
        for index, row in df.iterrows():
            try:
                school = School.objects.get(school_id=row['Schl'])

                school_fiscal.append(SchoolFiscalData(
                    school=school,
                    school_year = '20182019',
                    state_personnel = row['State - Personnel'],
                    state_non_personnel = row['State - Non-Personnel'],
                    local_personnel = row['Local - Personnel'],
                    local_non_personnel = row['Local - Non-Personnel'],
                    federal_personnel = row['Federal - Personnel'],
                    federal_non_personnel = row['Federal - Non-Personnel'],
                ))
            except School.DoesNotExist:
                print(f"Couldn't find {row['Schl']} at index {index}")
            except Exception as e:
                print(f"Error at index {index}: {str(e)}") 

        SchoolFiscalData.objects.bulk_create(school_fiscal)