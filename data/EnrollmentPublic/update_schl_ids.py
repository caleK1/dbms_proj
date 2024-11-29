import pandas as pd

df = pd.read_csv('/Users/calek/DBMS/dbms_proj/data/EnrollmentPublic/Enrollment_Public_Schools_2022_23_schls.csv')

# counter = 10001
# for index, row in df.iterrows():
# 	if row['School Number'] == 0000 or row['School Number'] == 9999:
# 		row['School Number'] = counter
# 		counter = counter + 1

df = df[~df['School Number'].isin([9999, 0000, 0])]
df.reset_index(drop=True, inplace=True)

df.to_csv('/Users/calek/DBMS/dbms_proj/data/EnrollmentPublic/Enrollment_Public_Schools_2022_23_schls_cleaned.csv', index=False)