from django.db import models

# Create your models here.
class SchoolFastFacts(models.Model):
	year = models.CharField('School Year', max_length=10)
	name = models.CharField('School Name', max_length=120)
	school_id = models.IntegerField('School ID', primary_key=True)
	district_name = models.CharField('District Name', max_length=120)
	aun = models.IntegerField('AUN')
	street_address = models.CharField('Street Address', max_length=120)
	city_address = models.CharField('City Address', max_length=50)
	state_address = models.CharField('State Address', max_length=10)
	zip_code = models.CharField('Zip Code', max_length=10)
	website = models.URLField('Website Address')
	phone_number = models.CharField('Phone Number', max_length=25)
	grades_offered = models.CharField('Grades Offered', max_length=50)
	title_1_school = models.CharField('Title 1 School', max_length=20)
	enrollment = models.IntegerField('Enrollment')
	gifted_students = models.DecimalField('Gifted Students', max_digits=3, decimal_places=1)
	intermediate_unit_name = models.CharField('Intermediate Unit Name', max_length=120)
	intermediate_unit_website = models.URLField('Intermediate Unit Website Address')
	american_indian_or_alaskan_native = models.DecimalField('American Indian or Alaskan Native', max_digits=3, decimal_places=1)
	asian = models.DecimalField('Asian', max_digits=3, decimal_places=1)
	pacific_islander = models.DecimalField('Pacific Islander', max_digits=3, decimal_places=1)
	african_american = models.DecimalField('Black/African American', max_digits=3, decimal_places=1)
	hispanic = models.DecimalField('Hispanic', max_digits=3, decimal_places=1)
	white = models.DecimalField('White', max_digits=3, decimal_places=1)
	two_or_more_races = models.DecimalField('Two or More Races', max_digits=3, decimal_places=1)
	economically_disadvantaged = models.DecimalField('Economically Disadvantaged', max_digits=3, decimal_places=1)
	english_learner = models.DecimalField('English Learner', max_digits=3, decimal_places=1)
	special_education = models.DecimalField('Special Education', max_digits=3, decimal_places=1)
	female = models.DecimalField('Female', max_digits=3, decimal_places=1)
	male = models.DecimalField('Male', max_digits=3, decimal_places=1)
	career_and_technical_programs = models.CharField('Career and Technical Programs', max_length=40)

	def __str__(self):
		self.name
