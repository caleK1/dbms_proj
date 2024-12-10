import pandas as pd

years=['0809','0910','1011','1112','1213','1314','1415','1516','1617','1718','1819','1920','2021','2122','2223','2324']

for year in years:
    df=pd.read_csv(f'/Users/ericlynch/cs320/dbms_proj/data/PublicSchoolLowIncome/{year}PublicSchoolsPercentLowIncome.csv',skiprows=4)
    df.columns=df.columns.str.strip()
    df.columns=df.columns.str.lower()
    cols=['school number','total enrollment','low income enrollment','percent of enrollment from low income families']
    df=df[cols]
    print(df.head())
    df.to_csv(f'/Users/ericlynch/cs320/dbms_proj/data/PublicSchoolLowIncome/{year}pub_low_pct_clean.csv')
    