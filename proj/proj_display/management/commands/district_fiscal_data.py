from django.core.management.base import BaseCommand
from proj_display.models import District
from proj_display.models import DistrictFiscalData
import pandas as pd


class Command(BaseCommand):
    # Handle does the work in the Command
    def handle(self, *args, **kwargs):

        DistrictFiscalData.objects.all().delete()
        years = ['20162017', '20172018', '20182019']
        district_fiscal = []

        for year in years:
            df = pd.read_csv(f'/Users/calek/DBMS/dbms_proj/data/DistrictFiscalData/DistrictFiscalDataSY{year}_cleaned.csv')

            for index, row in df.iterrows():
                try:
                    district_year = District.objects.get(district_aun=row['AUN'])

                    district_fiscal.append(DistrictFiscalData(
                        district = district_year,
                        school_year = year,
                        average_daily_membership = row['AverageDailyMembership(ADM)'] if pd.notnull(row['AverageDailyMembership(ADM)']) else 0,
                        based_on_instruction = row['BasedonInstruction'] if pd.notnull(row['BasedonInstruction']) else 0,
                        based_on_total = row['BasedonTotal'] if pd.notnull(row['BasedonTotal']) else 0,
                        facilities_acquisition_and_construction = row['FacilitiesAcquisition&Construction'] if pd.notnull(row['FacilitiesAcquisition&Construction']) else 0,
                        federal_revenue = row['Federal Revenue'] if pd.notnull(row['Federal Revenue']) else 0,
                        general_fund_balance = row['GeneralFundBalance'] if pd.notnull(row['GeneralFundBalance']) else 0,
                        local_revenue = row['Local Revenue'] if pd.notnull(row['Local Revenue']) else 0,
                        mv_pi_aid_ratio = row['MV/PIAidRatio'] if pd.notnull(row['MV/PIAidRatio']) else 0,
                        instruction = row['Instruction'] if pd.notnull(row['Instruction']) else 0,
                        state_revenue = row['State Revenue'] if pd.notnull(row['State Revenue']) else 0,
                        non_instructional = row['Non-instructional'] if pd.notnull(row['Non-instructional']) else 0,
                        other_revenue = row['Other Revenue'] if pd.notnull(row['Other Revenue']) else 0,
                        other_financing_uses = row['OtherFinancingUses'] if pd.notnull(row['OtherFinancingUses']) else 0,
                        supporting_services = row['SupportServices'] if pd.notnull(row['SupportServices']) else 0,
                        total_expenditures = row['TotalExpenditures'] if pd.notnull(row['TotalExpenditures']) else 0,
                        total_revenues = row['TotalRevenues'] if pd.notnull(row['TotalRevenues']) else 0,
                    ))
                except District.DoesNotExist:
                    print(f"Couldn't find {row['AUN']} at index {index}")
                except Exception as e:
                    print(f"Error at index {index}: {str(e)}") 

        DistrictFiscalData.objects.bulk_create(district_fiscal)