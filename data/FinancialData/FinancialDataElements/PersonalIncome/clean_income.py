import pandas as pd

years=['2012','2013','2014','2015','2016','2017','2018','2019','2020','2021']



for year in years:
    df=pd.read_excel(f'/Users/ericlynch/cs320/dbms_proj/data/FinancialData/FinancialDataElements/PersonalIncome/Personal Income {year}.xlsx')
    df.columns=df.columns.str.strip()
    df.columns=df.columns.str.lower()
    df.columns=df.columns.str.replace(r'\s+', ' ', regex=True)
    df.columns=df.columns.str.replace(' ','')
    df.columns=df.columns.str.replace('-','')
    cols=['aun','records','compensation','netprofits','miscellaneousincome','dividends&interest','outofstatetaxrecords','outofstatetaxcredit','outofstateincome(calculated)','totalpersonalincome','adjustedpersonalincome']
    df=df[cols]
    df.to_csv(f'/Users/ericlynch/cs320/dbms_proj/data/FinancialData/FinancialDataElements/PersonalIncome/cleaned_income{year}.csv')
    

