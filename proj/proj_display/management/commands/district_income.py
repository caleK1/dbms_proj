import pandas as pd
from django.core.management.base import BaseCommand
from proj_display.models import PersonalIncome
from proj_display.models import District



def safe_float(value):
    try:
        # If it's a string with a percentage sign, remove the '%' symbol and try to convert to float
        if isinstance(value, str):
            value = value.replace('$', '').replace(',','').strip()
        
        # Attempt to convert to float, handle any errors
        return float(value)
    except (ValueError, TypeError):  # Catch non-convertible values
        return 0.0

class Command(BaseCommand):
    help='Import the data from the Personal income into the database'
    years=['2012','2013','2014','2015','2016','2017','2018','2019','2020','2021']
    
    

    
   
    def handle(self, *args, **kwargs):
        PersonalIncome.objects.all().delete()
        info=[]
        #increase the years to 25 
        save_years=[20122013,20132014,20142015,201521016,20162017,20172018,20182019,20192020,20202021,20212022]
        i=-1

        for year in self.years:
            i+=1
            file_path=f'/Users/ericlynch/cs320/dbms_proj/data/FinancialData/FinancialDataElements/PersonalIncome/cleaned_income{year}.csv'
            try:
                df=pd.read_csv(file_path)
            

                for index,row in df.iterrows():
 
                    try:
                         districts=District.objects.get(district_aun=safe_float(row['aun']))
            
                     
                    except District.DoesNotExist:
                         print('District doesnt exist')
                         continue
                    except Exception as e:
                         print('District doesnt exist')
                         continue
                    try:
                        info.append(PersonalIncome(
                            district = districts,
                            school_year = save_years[i],
                            records = safe_float(row['records']),
                            compensation=safe_float(row['compensation']),
                            net_profits = safe_float(row['netprofits']),
                            dividends_and_interest = safe_float(row['dividends&interest']),
                            misc_income = safe_float(row['miscellaneousincome']),
                            out_of_st_tax_records = safe_float(row['outofstatetaxrecords']),
                            out_of_st_tax_credit = safe_float(row['outofstatetaxcredit']),
                            out_of_st_income = safe_float(row['outofstateincome(calculated)']),
                            total_personal_income = safe_float(row['totalpersonalincome']),
                            adjusted_personal_income = safe_float(row['adjustedpersonalincome'])                                   
                        
                        ))
                    except Exception as e:
                         print(row['AUN'])
                         print(f'Error at index {index} for year {year}: {str(e)}')    
            
                        


            except FileNotFoundError:
                print(f'No file at path for {file_path}. Skipping...')
        PersonalIncome.objects.bulk_create(info)
        print(f'Successfully imported {len(info)} records into the database.')        
