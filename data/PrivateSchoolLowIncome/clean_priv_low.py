import pandas as pd

years=['1314','1415','1516','1617','1718','1819','1920','2021','2022','2223']

for year in years:
    df=pd.read_csv(f'/Users/ericlynch/cs320/dbms_proj/data/PrivateSchoolLowIncome/{year}PrivateNonpublicSchoolsPercentLowIncome.csv',skiprows=3)
    df.columns=df.columns.str.strip()
    df.columns=df.columns.str.lower()
    cols=['aun','percent']
    df=df[cols]
    print(df.head())
    df.to_csv(f'/Users/ericlynch/cs320/dbms_proj/data/PrivateSchoolLowIncome/{year}priv_low_pct_clean.csv')
    