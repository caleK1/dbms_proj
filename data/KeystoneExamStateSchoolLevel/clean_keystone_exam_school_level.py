import pandas as pd


# List of years
years = ['2015', '2016', '2017', '2018', '2019','2021','2022']

# Loop through each year and process the corresponding file
for year in years:
    # Read the CSV file for the current year
    df = pd.read_csv(f'/Users/ericlynch/cs320/dbms_proj/data/KeystoneExamStateSchoolLevel/{year}KeystoneExamsSchoolLevelData.csv')
    print(df.head())
    df.columns=df.columns.str.strip()
    # Create a pivot table
    df=df[['Schl','Subject','Group','N Scored','Pct. Advanced','Pct. Proficient','Pct. Basic','Pct. Below Basic']]
    df['Schl'] = df['Schl'].fillna(0).astype(int).astype(str).str.zfill(4)

    # Save the cleaned pivoted DataFrame to a new CSV file
    df.to_csv(f'/Users/ericlynch/cs320/dbms_proj/data/KeystoneExamStateSchoolLevel/{year}KeystoneExamsSchoolLevel_cleaned.csv', index=False)
