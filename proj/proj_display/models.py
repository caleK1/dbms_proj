from django.db import models

# Create your models here.

class School(models.Model):
	school_name = models.CharField('School Name', max_length=120)
	district_aun = models.ForeignKey('District', blank=True, null=True, on_delete=models.CASCADE)
	school_id = models.IntegerField('School ID', primary_key=True)

	def __str__(self):
		return self.school_name

class District(models.Model):
	district_aun = models.IntegerField('AUN', primary_key = True)
	district_name = models.CharField('District Name', max_length=120)
	county_id = models.ForeignKey('County', to_field='county_id', blank=True, null=True, on_delete=models.CASCADE)

	def __str__(self):
		return self.district_name

class County(models.Model):
	county_id = models.IntegerField('County ID', primary_key = True)
	county_name = models.CharField('County Name', max_length=120)

	def __str__(self):
		return self.county_name


class SchoolFastFacts(models.Model):
	year = models.CharField('School Year', max_length=10)
	school_id = models.ForeignKey('School', blank=True, null=True, on_delete=models.CASCADE)
	street_address = models.CharField('Street Address', max_length=120)
	city_address = models.CharField('City Address', max_length=50)
	state_address = models.CharField('State Address', max_length=10)
	zip_code = models.CharField('Zip Code', max_length=10)
	website = models.URLField('Website Address')
	phone_number = models.CharField('Phone Number', max_length=25)
	grades_offered = models.CharField('Grades Offered', max_length=50)
	title_1_school = models.CharField('Title 1 School', max_length=20)
	enrollment = models.IntegerField('Enrollment')
	gifted_students = models.DecimalField('Gifted Students', max_digits=4, decimal_places=2)
	intermediate_unit_name = models.CharField('Intermediate Unit Name', max_length=120)
	intermediate_unit_website = models.URLField('Intermediate Unit Website Address')
	american_indian_or_alaskan_native = models.DecimalField('American Indian or Alaskan Native', max_digits=4, decimal_places=2)
	asian = models.DecimalField('Asian', max_digits=4, decimal_places=2)
	pacific_islander = models.DecimalField('Pacific Islander', max_digits=4, decimal_places=2)
	african_american = models.DecimalField('Black/African American', max_digits=4, decimal_places=2)
	hispanic = models.DecimalField('Hispanic', max_digits=4, decimal_places=2)
	white = models.DecimalField('White', max_digits=4, decimal_places=2)
	two_or_more_races = models.DecimalField('Two or More Races', max_digits=4, decimal_places=2)
	economically_disadvantaged = models.DecimalField('Economically Disadvantaged', max_digits=4, decimal_places=2)
	english_learner = models.DecimalField('English Learner', max_digits=4, decimal_places=2)
	special_education = models.DecimalField('Special Education', max_digits=4, decimal_places=2)
	female = models.DecimalField('Female', max_digits=4, decimal_places=2)
	male = models.DecimalField('Male', max_digits=4, decimal_places=2)
	career_and_technical_programs = models.CharField('Career and Technical Programs', max_length=120, blank=True)

	def __str__(self):
		return f"{self.school_id}"

class DistrictFastFacts(models.Model):
	year = models.CharField('District Year', max_length=10)
	aun = models.ForeignKey('District', blank=True, null=True, on_delete=models.CASCADE)
	two_or_more_races = models.DecimalField('Two or More Races', max_digits=4, decimal_places=2)
	american_indian_or_alaskan_native = models.DecimalField('American Indian or Alaskan Native', max_digits=4, decimal_places=2)
	asian = models.DecimalField('Asian', max_digits=4, decimal_places=2)
	african_american = models.DecimalField('Black/African American', max_digits=4, decimal_places=2)
	career_and_technical_center_name = models.CharField('Career and Technical Center Name', max_length=120)
	career_and_technical_center_website = models.URLField('Career and Technical Center Website Address', blank=True)
	charter_school_enrollment = models.IntegerField('Charter School Enrollment')
	city_address = models.CharField('City Address', max_length=50)
	state_address = models.CharField('State Address', max_length=10)
	street_address = models.CharField('Street Address', max_length=120)
	enrollment = models.IntegerField('Enrollment')
	zip_code = models.CharField('Zip Code', max_length=10)
	economically_disadvantaged = models.DecimalField('Economically Disadvantaged', max_digits=4, decimal_places=2)
	english_learner = models.DecimalField('English Learner', max_digits=4, decimal_places=2)
	enrollment_in_partnering_career_technical_centers = models.IntegerField('Enrollment in Partnering Career/Technical Centers')
	female = models.DecimalField('Female', max_digits=4, decimal_places=2)
	foster_care = models.DecimalField('Foster Care', max_digits=4, decimal_places=2)
	geographic_size = models.DecimalField('Geographic Size (miles)', max_digits=8, decimal_places=2)
	grades_offered = models.CharField('Grades Offered', max_length=50)
	hispanic = models.DecimalField('Hispanic', max_digits=4, decimal_places=2)
	homeless = models.DecimalField('Homeless', max_digits=4, decimal_places=2)
	intermediate_unit_name = models.CharField('Intermediate Unit Name', max_length=120)
	intermediate_unit_website = intermediate_unit_website = models.URLField('Intermediate Unit Website Address')
	male = models.DecimalField('Male', max_digits=4, decimal_places=2)
	miliitary_connected = models.DecimalField('Military Connected', max_digits=4, decimal_places=2)
	pacific_islander = models.DecimalField('Pacific Islander', max_digits=4, decimal_places=2)
	num_of_schools = models.IntegerField('Number of Schools')
	gifted_students = models.DecimalField('Gifted Students', max_digits=4, decimal_places=2)
	special_education = models.DecimalField('Special Education', max_digits=4, decimal_places=2)
	phone_number = models.CharField('Phone Number', max_length=25)
	website = models.URLField('Website Address')
	white = models.DecimalField('White', max_digits=4, decimal_places=2)

	def __str__(self):
		return f"{self.aun}"
	
	##take anything besides ethnicity outside of the demographic 
class Demographic(models.Model):
	year=models.CharField("School Year", max_length=10)
	school_id = models.ForeignKey("School", blank=True, null=True , on_delete=models.CASCADE)
	asian = models.DecimalField('Asian', max_digits=4, decimal_places=2)
	pacific_islander = models.DecimalField('Pacific Islander', max_digits=4, decimal_places=2)
	african_american = models.DecimalField('Black/African American', max_digits=4, decimal_places=2)
	hispanic = models.DecimalField('Hispanic', max_digits=4, decimal_places=2)
	white = models.DecimalField('White', max_digits=4, decimal_places=2)
	two_or_more_races = models.DecimalField('Two or More Races', max_digits=4, decimal_places=2)
	economically_disadvantaged = models.DecimalField('Economically Disadvantaged', max_digits=4, decimal_places=2)
	english_learner = models.DecimalField('English Learner', max_digits=4, decimal_places=2)
	special_education = models.DecimalField('Special Education', max_digits=4, decimal_places=2)
	def __str__(self):
		return f"{self.school_id}"

class Gender(models.Model):
	school_id=models.ForeignKey("School",on_delete=models.CASCADE,null=True,blank=True)
	male=models.DecimalField("Male", max_digits=4,decimal_places=2)
	female=models.DecimalField("Female", max_digits=4,decimal_places=2)
	def __str__(self):	
		return f"{self.school_id}"