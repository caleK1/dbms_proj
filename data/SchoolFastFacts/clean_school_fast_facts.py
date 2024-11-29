import pandas as pd

years = ['20172018', '20182019', '20192020', '20202021', '20222023']
for year in years:
	df = pd.read_csv(f'/Users/calek/DBMS/dbms_proj/data/SchoolFastFacts/SchoolFastFacts_{year}.csv')

	pivot_df = df.pivot_table(
		index=['DistrictName', 'SchoolName', 'AUN', 'Schl'],
		columns='DataElement',
		values='DisplayValue',
		aggfunc='first'
		)

	pivot_df.columns.name = None

	pivot_df.reset_index(inplace=False)

	pivot_df.to_csv(f'/Users/calek/DBMS/dbms_proj/data/SchoolFastFacts/SchoolFastFacts_{year}_cleaned.csv')