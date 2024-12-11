import pandas as pd

years = ['20162017', '20172018', '20182019']
for year in years:
	df = pd.read_csv(f'/Users/calek/DBMS/dbms_proj/data/DistrictFiscalData/DistrictFiscalDataSY{year}.csv')

	pivot_df = df.pivot_table(
		index='AUN',
		columns='DataElement',
		values='DisplayValue',
		aggfunc='first'
		)

	pivot_df.columns.name = None

	pivot_df.reset_index(inplace=False)

	#Get rid of $
	for column in pivot_df.columns:
		if pivot_df[column].dtype == "object":
			pivot_df[column] = pivot_df[column].replace({'\$': '', ',':''}, regex=True)
			df[column] = pd.to_numeric(pivot_df[column], errors='coerce')

	pivot_df.to_csv(f'/Users/calek/DBMS/dbms_proj/data/DistrictFiscalData/DistrictFiscalDataSY{year}_cleaned.csv')