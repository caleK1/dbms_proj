import pandas as pd
df = pd.read_csv(f'/Users/calek/DBMS/dbms_proj/data/SchoolFiscalData/School_Fiscal_Data_SY_20182019.csv')

pivot_df = df.pivot_table(
	index='Schl',
	columns='DataElement',
	values='DisplayValue',
	aggfunc='first'
	)

pivot_df.columns.name = None

pivot_df.reset_index(inplace=False)

pivot_df.to_csv(f'/Users/calek/DBMS/dbms_proj/data/SchoolFiscalData/School_Fiscal_Data_SY_20182019_cleaned.csv')