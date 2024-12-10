import pandas as pd


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


df=pd.read_excel(f'/Users/ericlynch/cs320/dbms_proj/data/GraduatesPublicSchool/GraduatesPublicbySchool2008-09.xls',sheet_name=4,skiprows=3)
print(df.columns)