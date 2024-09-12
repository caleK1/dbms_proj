import csv
from view.models import AcademicPerformance

def import_academic_performance(file_path):
	with open(file_path, 'r') as file:
		reader = csv.DictReader(file)
		for row in reader:
			AcademicPerformance.objects.create(
					LEA_name = row['LEA Name'],
					school_name = row['School Name'],
					AUN = row['AUN'],
					school_number = row['School Number'],
					data_element = row ['Data Element'],
					display_value = row ['Display Value']
				)

if __name__ == '__main__':
	csv_file_path = "C:/Users/calek/DBMS/dbms_proj/data/AcademicPerformance/SPP.APD.2016.2017.csv"
	import_academic_performance(csv_file_path)