import pandas as pd
import os

years=['2007-08', '2008-09', '2009-10', '2010-11', '2011-12', '2012-13', '2013-14', '2014-15', '2015-16', '2016-17', '2017-18', '2018-19', '2019-20', '2020-21', '2021-22', '2022-23']

standard_columns = [
    'school number', 'graduate count', 'college bound', 'total college bound %',
    '2- or 4-year college or university', '2- or 4-year university %', 'total postsecondary bound',
    'total postsecondary bound %', 'non-degree-granting postsecondary school', 
    'non-degree-granting postsecondary school %', 'specialized associate degree granting institution',
    'specialized associate degree granting institution %'
]

column_mapping = {
    'school number': ['school number', 'school code', 'school_id'],  # Mapping possible variations
    'graduate count': ['total graduates', 'graduates', 'graduate_total'],
    'college bound': ['college bound', 'college_bound','total college-bound'],
    'total college bound %': ['total college bound %', 'total_college_bound_percentage','total college-bound %'],
    '2- or 4-year college or university': ['2- or 4-year college or university', '2_4_year_college'],
    '2- or 4-year university %': ['2- or 4-year university %', '2_4_year_university_percentage'],
    'total postsecondary bound': ['total postsecondary bound', 'postsecondary_bound'],
    'total postsecondary bound %': ['total postsecondary bound %', 'postsecondary_bound_percentage'],
    'non-degree-granting postsecondary school': ['non-degree-granting postsecondary school', 'non_degree_granting_school'],
    'non-degree-granting postsecondary school %': ['non-degree-granting postsecondary school %', 'non_degree_granting_school_percentage'],
    'specialized associate degree granting institution': ['specialized associate degree granting institution', 'specialized_associate_degree_institution','specialized associate degree-granting institution'],
    'specialized associate degree granting institution %': ['specialized associate degree granting institution %', 'specialized_associate_degree_institution_percentage']
}
def standardize_columns(df):
    # Iterate over the column mapping and rename columns
    for standard_name, variations in column_mapping.items():
        for variation in variations:
            if variation.lower() in df.columns:
                print(f"Renaming column '{variation.lower()}' to '{standard_name}'")
                df.rename(columns={variation.lower(): standard_name}, inplace=True)
    return df

    
for year in years:
    df=pd.read_csv(f'/Users/ericlynch/cs320/dbms_proj/data/GraduatesPublicSchool/raw_school_csv/GraduatesPublicbySchool{year}.csv')
   

    df.columns = df.columns.str.lower()#.str.replace(' ', '_').str.replace('-', '_')
    for column in df.columns:
        print(column)
    df=standardize_columns(df)

    matching_columns = [col for col in standard_columns if col in df.columns]
    df = df[matching_columns]
    #new_df=df[df['school number']== 9999]
    df.drop(df[df['school number']== 9999].index, inplace = True)
   
   
    df.to_csv(f'/Users/ericlynch/cs320/dbms_proj/data/GraduatesPublicSchool/cleaned_school_csv/grad_pub_school_clean_{year}.csv')
   



