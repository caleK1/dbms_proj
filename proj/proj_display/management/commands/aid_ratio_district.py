import pandas as pd
from django.core.management.base import BaseCommand
from proj_display.models import AidRatio
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
    help='Import the data from the LowIncomePercent into the database'
    years=['2013-2014', '2014-2015', '2015-2016', '2016-2017', '2017-2018', '2018-2019', '2019-2020', '2020-2021', '2021-2022', '2022-2023','2023-2024','2024-2025']
    
    

    
   
    def handle(self, *args, **kwargs):
        AidRatio.objects.all().delete()
        info=[]
        #increase the years to 25 
        save_years=[20132014,20142015,201521016,20162017,20172018,20182019,20192020,20202021,20212022,20222023,20232024,20242025]
        i=-1

        for year in self.years:
            i+=1
            file_path=f'/Users/ericlynch/cs320/dbms_proj/data/FinancialData/FinancialDataElements/AidRatios/cleaned_adr{year}.csv'
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
                        info.append(AidRatio(
                            district = districts,
                            school_year = save_years[i],
                            market_value = safe_float(row['marketvalue']),
                            personal_income = safe_float(row['personalincome']),
                            wadm = safe_float(row['wadm']),
                            mv_per_wadm = safe_float(row['mvperwadm']),
                            market_value_aid_ratio = safe_float(row['market_value_aid_ratio']),
                            pi_per_wadm = safe_float(row['piperwadm']),
                            personal_income_aid_ratio = safe_float(row['personal_income_aid_ratio']),
                            market_value_personal_income_aid_ratio = safe_float(row['mvpi'])
                        
                        ))
                    except Exception as e:
                         print(row['AUN'])
                         print(f'Error at index {index} for year {year}: {str(e)}')    
            
                        


            except FileNotFoundError:
                print(f'No file at path for {file_path}. Skipping...')
        AidRatio.objects.bulk_create(info)
        print(f'Successfully imported {len(info)} records into the database.')        
