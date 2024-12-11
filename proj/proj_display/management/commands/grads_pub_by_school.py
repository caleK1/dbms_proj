import pandas as pd
from django.core.management.base import BaseCommand
from proj_display.models import PublicSchoolGradRatesSchool
from proj_display.models import School



def safe_float(value):
    try:
        # If it's a string with a percentage sign, remove the '%' symbol and try to convert to float
        if isinstance(value, str):
            value = value.replace('%', '').replace(',','').strip()
        
        # Attempt to convert to float, handle any errors
        return float(value)
    except (ValueError, TypeError):  # Catch non-convertible values
        return 0.0

class Command(BaseCommand):
    help='Import the data from the LowIncomePercent into the database'
    years=['2007-08', '2008-09', '2009-10', '2010-11', '2011-12', '2012-13', '2013-14', '2014-15', '2015-16', '2016-17', '2017-18', '2018-19', '2019-20', '2020-21', '2021-22', '2022-23']
    
    

    
   
    def handle(self, *args, **kwargs):
        tally=0
        PublicSchoolGradRatesSchool.objects.all().delete()
        info=[]
        save_years=[20072008,20082009,20092010,20102011,20112012,20122013,20132014,20142015,201521016,20162017,20172018,20182019,20192020,20202021,20212022,20222023]
        i=-1

        for year in self.years:
            i+=1
            file_path=f'/Users/ericlynch/cs320/dbms_proj/data/GraduatesPublicSchool/cleaned_school_csv/grad_pub_school_clean_{year}.csv'
            try:
                df=pd.read_csv(file_path)
            

                for index,row in df.iterrows():

                    #temp1= safe_float(row['specialized associate degree granting institution %'])
                    #temp2=safe_float(row['2- or 4-year university %'])
                    #if(temp1==None):
                     #   temp1=0.0
                    #if(temp2==None):
                     #   temp2=0.0    
                           
                    try:
                         schools=School.objects.get(school_id=safe_float(row['school number']))
                         grads=safe_float(row['college bound'])
                         four_year=safe_float(row['2- or 4-year college or university'])
                         special=safe_float(row['specialized associate degree granting institution'])
                        
                             

                    except School.DoesNotExist:
                         continue
                    except Exception as e:
                         continue
                    try:
                        info.append(PublicSchoolGradRatesSchool(
                            school=schools,
                            school_year=save_years[i],
                            total_graduates = safe_float(row['graduate count']),
                            total_college_bound =grads ,
                            total_college_bound_percentage = safe_float(row['total college bound %']),
                            two_four_year_college_university = safe_float(row['2- or 4-year college or university']),
                            two_four_year_college_university_percentage =round(four_year/grads,2)*100,
                            total_postsecondary_bound = safe_float(row['total postsecondary bound']),
                            total_postsecondary_bound_percentage = safe_float(row['total postsecondary bound %']),
                            non_degree_getting_postsecondary_school = safe_float(row['non-degree-granting postsecondary school']),
                            non_degree_getting_postsecondary_school_percentage = safe_float(row['non-degree-granting postsecondary school %']),
                            specialized_associate_degree_getting_institution = safe_float(row['specialized associate degree granting institution']),
                            specialized_associate_degree_getting_institution_percentage = round(special/grads,2)*100




                        ))
                    except Exception as e:
                         print(row['school number'])
                         print(row['total postsecondary bound %'])
                         print(f'Error at index {index} for year {year}: {str(e)}')    
            
                        


            except FileNotFoundError:
                print(f'No file at path for {file_path}. Skipping...')
        PublicSchoolGradRatesSchool.objects.bulk_create(info)
        print(f'Successfully imported {len(info)} records into the database.')        
