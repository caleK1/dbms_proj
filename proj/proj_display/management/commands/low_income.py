import pandas as pd 
from django.core.management.base import BaseCommand
from proj_display.models import LowIncomePercentPrivateSchool
from proj_display.models import LowIncomePercentPubSchool
from proj_display.models import School


def safe_float(value):
            try:
                return float(value) if pd.notna(value) else 0
            except ValueError:
                return 0

class Command(BaseCommand):
    help='Import the data from the LowIncomePercent into the database'
    years_pub=years=['20082009','20092010','20102011','20112012','20122013','20132014','20142015','20152016','20162017','20172018','20182019','20192020','20202021','20212022','20222023','20232024']
    years_priv=['1314','1415','1516','1617','1718','1819','1920','2021','2022','2223']
   
    
    def handle(self, *args, **kwargs):
        LowIncomePercentPubSchool.objects.all().delete()
        LowIncomePercentPrivateSchool.objects.all().delete()
        low_income_priv_info=[] 
        low_income_pub_info=[]


        for year in self.years_pub:
            file_path=f'/Users/calek/DBMS/dbms_proj/data/PublicSchoolLowIncome/{year}pub_low_pct_clean.csv'
            try:
                df=pd.read_csv(file_path)

                for index,row in df.iterrows():
                    try:
                         schools=School.objects.get(school_id=safe_float(row['school number']))
                    except School.DoesNotExist:
                         continue
                    except Exception as e:
                         continue
                    try:
                        a=row['total enrollment']
                        b=row['low income enrollment']
                        low_income_pub_info.append(LowIncomePercentPubSchool(
                             #if error check what row[school num] is actually getting
                            school=schools,
                            school_year=year,
                            total_enrollment=safe_float(a),
                            low_income_enrollment=safe_float(b),
                            percent_enrollment_from_low_income_families= row['percent of enrollment from low income families']




                        ))
                    except Exception as e:
                         print(row['school number'])
                         print(f'Error at index {index} for year {year}: {str(e)}')    

                        


            except FileNotFoundError:
                print(f'No file at path for {file_path}. Skipping...')
        LowIncomePercentPubSchool.objects.bulk_create(low_income_pub_info)
        print(f'Successfully imported {len(low_income_pub_info)} records into the database.')        

        for year in self.years_priv:
                file_path_priv=f'/Users/calek/DBMS/dbms_proj/data/PrivateSchoolLowIncome/{year}priv_low_pct_clean.csv'
                try:
                    df=pd.read_csv(file_path_priv)

                    for index,row in df.iterrows():
                        try:
                            schools=School.objects.get(school_id=safe_float(row['school number']))
                        except School.DoesNotExist:
                            continue
                        except Exception as e:
                            continue
                        try:
                            low_income_priv_info.append(LowIncomePercentPrivateSchool(
                            #if error check what row[school num] is actually getting
                            school=School.objects.get(school_id=safe_float(row['aun'])),
                            school_year=year,
                            low_income_percentage=safe_float(row['percent'])
                            




                        ))
                        except Exception as e:
                            print(row['school number'])
                            print(f'Error at index {index} for year {year}: {str(e)}')    

                        


                except FileNotFoundError:
                    print(f'No file at path for {file_path_priv}. Skipping...')
        LowIncomePercentPrivateSchool.objects.bulk_create(low_income_priv_info)
        print(f'Successfully imported {len(low_income_priv_info)} records into the database.')        
