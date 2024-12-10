import pandas as pd
from django.core.management.base import BaseCommand
from proj_display.models import KeystoneGradeSchool
from proj_display.models import School

class Command(BaseCommand):
    help = 'Imports the Keystone grade data into the database'

    years = ['2015', '2016', '2017', '2018', '2019', '2021', '2022']

    def handle(self, *args, **kwargs):
        KeystoneGradeSchool.objects.all().delete()
        keystone_info = []

        for year in self.years:
            file_path = f'/Users/ericlynch/cs320/dbms_proj/data/KeystoneExamStateSchoolLevel/{year}KeystoneExamsSchoolLevel_cleaned.csv'
            try:
                df = pd.read_csv(file_path)

                for index, row in df.iterrows():
                    try:
                        keystone_info.append(KeystoneGradeSchool(
                            school=School.objects.get(school_id=row['Schl']), 
                            school_year=year,
                            keystone_subject=row['Subject'],
                            student_group=row['Group'],
                            grade=11,  
                            number_scored=safe_float(row['N Scored']),
                            percent_advanced=safe_float(row['Pct. Advanced']),
                            percent_proficient=safe_float(row['Pct. Proficient']),
                            percent_basic=safe_float(row['Pct. Basic']),
                            percent_below_basic=safe_float(row['Pct. Below Basic'])
                        ))
                        
                        
                    except Exception as e:
                        print(row['Schl'])
                        print(f"Error at index {index} for year {year}: {str(e)}")
            except FileNotFoundError:
                print(f"File for year {year} not found at {file_path}. Skipping...")
            except Exception as e:
                print(f"Error processing file for year {year}: {str(e)}")

        KeystoneGradeSchool.objects.bulk_create(keystone_info)
        print(f"Successfully imported {len(keystone_info)} records into the database.")

def safe_float(value):
            try:
                return float(value)
            except ValueError:
                return 0

