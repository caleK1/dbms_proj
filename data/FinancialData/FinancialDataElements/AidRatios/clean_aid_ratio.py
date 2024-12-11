import pandas as pd

years=['2013-2014', '2014-2015', '2015-2016', '2016-2017', '2017-2018', '2018-2019', '2019-2020', '2020-2021', '2021-2022', '2022-2023','2023-2024','2024-2025']



for year in years:
    df=pd.read_csv(f'/Users/ericlynch/cs320/dbms_proj/data/FinancialData/FinancialDataElements/AidRatios/Finances AidRatio {year}.csv')
    df.columns=df.columns.str.strip()
    df.columns=df.columns.str.lower()
    df.columns=df.columns.str.replace(r'\s+', ' ', regex=True)
    df.columns=df.columns.str.replace(' ','')
    cols=['aun','marketvalue','personalincome','wadm','mvperwadm','market_value_aid_ratio','piperwadm','personal_income_aid_ratio','mvpi']
    df=df[cols]
    df.to_csv(f'/Users/ericlynch/cs320/dbms_proj/data/FinancialData/FinancialDataElements/AidRatios/cleaned_adr{year}.csv')
    




    