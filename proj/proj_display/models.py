"""
    DBMS Project: Cale King, Eric Lynch, Jacob Seltzer
    Github Repo: https://github.com/caleK1/dbms_proj.git
"""

from django.db import models

# Create your models here.

class County(models.Model):
    county_id = models.AutoField(primary_key=True)
    county_name = models.CharField(max_length=100)

    def __str__(self):
        return self.county_name

class District(models.Model):
    district_aun = models.IntegerField(primary_key=True)
    district_name = models.CharField(max_length=100)
    county_id = models.ForeignKey(County, on_delete=models.CASCADE, default=-1)

    def __str__(self):
        return self.district_name

class School(models.Model):
    school_id = models.IntegerField(primary_key=True)
    school_name = models.CharField(max_length=100)
    district_aun = models.ForeignKey(District, on_delete=models.CASCADE)

    def __str__(self):
        return self.school_name

class SchoolInfo(models.Model):
    school_id = models.OneToOneField(School, on_delete=models.CASCADE, primary_key=True)
    street_address = models.CharField(max_length=50)
    city_address = models.CharField(max_length=25)
    zip_code = models.IntegerField()
    website = models.CharField(max_length=50)
    phone_num = models.CharField(max_length=25)
    grades_offered = models.CharField(max_length=25)
    title_1 = models.BooleanField()

    def __str__(self):
        return f"Info for {self.school_id}"

class GenderSchool(models.Model):
    school_id = models.ForeignKey(School, on_delete=models.CASCADE)
    school_year = models.IntegerField(verbose_name="School Year")
    male = models.FloatField(verbose_name="Male")
    female = models.FloatField(verbose_name="Female")

    class Meta:
        unique_together = ('school_id', 'school_year')

    def __str__(self):
        return f"Gender distribution for {self.school} in {self.school_year}"

class SchoolDemographic(models.Model):
    school_id = models.ForeignKey(School, on_delete=models.CASCADE)
    school_year = models.IntegerField(verbose_name="School Year")
    per_asian = models.FloatField(verbose_name="Asian %")
    per_hispanic = models.FloatField(verbose_name="Hispanic %")
    per_pacific_islander = models.FloatField(verbose_name="Pacific Islander %")
    per_am_indian_or_alaskan_native = models.FloatField(verbose_name="American Indian or Alaskan Native %")
    per_african_american = models.FloatField(verbose_name="African American/Black %")
    per_white = models.FloatField(verbose_name="White %")
    per_two_or_more_races = models.FloatField(verbose_name="2 or More Races %")

    class Meta:
        unique_together = ('school_id', 'school_year')

    def __str__(self):
        return f"Demographics for {self.school} in {self.school_year}"

class ExtraDemoSchool(models.Model):
    school_id = models.ForeignKey(School, on_delete=models.CASCADE)
    school_year = models.IntegerField(verbose_name="School Year")
    per_english_learner = models.FloatField(verbose_name="English Learner %")
    per_special_education = models.FloatField(verbose_name="Special Education %")
    per_gifted_student = models.FloatField(verbose_name="Gifted Student %")
    per_military_connected = models.FloatField(verbose_name="Military Connected %")
    per_foster_care = models.FloatField(verbose_name="Foster Care %")
    per_economically_disadvantaged = models.FloatField(verbose_name="Economically Disadvantaged %")
    per_homeless = models.FloatField(verbose_name="Homeless %")

    class Meta:
        unique_together = ('school_id', 'school_year')

    def __str__(self):
        return f"Extra demographics for {self.school_id} in {self.school_year}"

class GenderDistrict(models.Model):
    district = models.ForeignKey(District, on_delete=models.CASCADE)
    school_year = models.IntegerField(verbose_name="School Year")
    male = models.FloatField(verbose_name="Male %")
    female = models.FloatField(verbose_name="Female %")

    class Meta:
        unique_together = ('district', 'school_year')

    def __str__(self):
        return f"Gender distribution for {self.district} in {self.school_year}"

class DistrictDemographic(models.Model):
    district = models.ForeignKey(District, on_delete=models.CASCADE)
    school_year = models.IntegerField(verbose_name="School Year")
    per_african_american = models.FloatField(verbose_name="African American/Black %")
    per_am_indian_or_alaskan_native = models.FloatField(verbose_name="American Indian or Alaskan Native %")
    per_pacific_islander = models.FloatField(verbose_name="Pacific Islander %")
    per_two_or_more_races = models.FloatField(verbose_name="2 or More Races %")
    per_white = models.FloatField(verbose_name="White %")
    per_hispanic = models.FloatField(verbose_name="Hispanic %")
    per_asian = models.FloatField(verbose_name="Asian %")

    class Meta:
        unique_together = ('district', 'school_year')

    def __str__(self):
        return f"Demographics for {self.district} in {self.school_year}"

class ExtraDemoDistrict(models.Model):
    district = models.ForeignKey(District, on_delete=models.CASCADE)
    school_year = models.IntegerField(verbose_name="School Year")
    per_military_connected = models.FloatField(verbose_name="Military Connected %")
    per_gifted_student = models.FloatField(verbose_name="Gifted Student %")
    per_special_education = models.FloatField(verbose_name="Special Education %")
    per_english_learner = models.FloatField(verbose_name="English Learner %")
    per_foster_care = models.FloatField(verbose_name="Foster Care %")
    per_homeless = models.FloatField(verbose_name="Homeless %")
    per_economically_disadvantaged = models.FloatField(verbose_name="Economically Disadvantaged %")

    class Meta:
        unique_together = ('district', 'school_year')

    def __str__(self):
        return f"Extra demographics for {self.district} in {self.school_year}"

class DistrictInfo(models.Model):
    district = models.OneToOneField(District, on_delete=models.CASCADE, primary_key=True)
    c_and_t_web = models.CharField(max_length=50)
    c_and_t_enrollment = models.IntegerField()
    c_and_t_name = models.CharField(max_length=100)
    imu_name = models.CharField(max_length=100)
    imu_website = models.CharField(max_length=50)
    street_address = models.CharField(max_length=50)
    city_address = models.CharField(max_length=25)
    zip_code = models.IntegerField()
    website = models.CharField(max_length=50)
    phone_num = models.CharField(max_length=50)
    grades_off = models.CharField(max_length=25)
    num_schools = models.IntegerField()
    geographic_size = models.FloatField()

    def __str__(self):
        return f"District Info for {self.district}"

class SchoolFiscalData(models.Model):
    school = models.ForeignKey(School, on_delete=models.CASCADE)
    school_year = models.IntegerField(verbose_name="School Year")
    state_personnel = models.FloatField(verbose_name="State Personnel")
    state_non_personnel = models.FloatField(verbose_name="State Non-Personnel")
    local_personnel = models.FloatField(verbose_name="Local Personnel")
    local_non_personnel = models.FloatField(verbose_name="Local Non-Personnel")
    federal_personnel = models.FloatField(verbose_name="Federal Personnel")
    federal_non_personnel = models.FloatField(verbose_name="Federal Non-Personnel")

    class Meta:
        unique_together = ('school', 'school_year')
        verbose_name = 'School Fiscal Data'
        verbose_name_plural = 'School Fiscal Data'

    def __str__(self):
        return f"Fiscal Data for {self.school} in {self.school_year}"


class DistrictFiscalData(models.Model):
    district = models.ForeignKey(District, on_delete=models.CASCADE)
    school_year = models.IntegerField()
    average_daily_membership = models.FloatField()
    based_on_instruction = models.FloatField()
    based_on_total = models.FloatField()
    facilities_acquisition_and_construction = models.FloatField()
    federal_revenue = models.FloatField()
    general_fund_balance = models.FloatField()
    local_revenue = models.FloatField()
    mv_pi_aid_ratio = models.FloatField()
    instruction = models.FloatField()
    state_revenue = models.FloatField()
    non_instructional = models.FloatField()
    other_revenue = models.FloatField()
    other_financing_uses = models.FloatField()
    supporting_services = models.FloatField()
    total_expenditures = models.FloatField()
    total_revenues = models.FloatField()

    class Meta:
        unique_together = ('district', 'school_year')
        verbose_name = 'District Fiscal Data'
        verbose_name_plural = 'District Fiscal Data'

    def __str__(self):
        return f"Fiscal Data for {self.district} in {self.school_year}"


class ExpendituresGeneral(models.Model):
    district = models.ForeignKey(District, on_delete=models.CASCADE)
    school_year = models.IntegerField()
    current_expenditures = models.FloatField()
    other_expenditures = models.FloatField()
    actual_instruction_summer = models.FloatField()
    instructional_staff = models.FloatField()
    administration = models.FloatField()
    pupil_health = models.FloatField()
    business = models.FloatField()

    class Meta:
        unique_together = ('district', 'school_year')
        verbose_name = 'Expenditures General'
        verbose_name_plural = 'Expenditures General'

    def __str__(self):
        return f"General Expenditures for {self.district} in {self.school_year}"


class ExpendituresPrograms(models.Model):
    district = models.ForeignKey(District, on_delete=models.CASCADE)
    school_year = models.IntegerField()
    regular_programs = models.FloatField()
    special_programs = models.FloatField()
    vocational_programs = models.FloatField()
    other_institutional_programs = models.FloatField()
    non_public_programs = models.FloatField()
    adult_education_programs = models.FloatField()
    higher_education_programs = models.FloatField()
    higher_ed_programs_secondary = models.FloatField()
    pre_kindergarten = models.FloatField()

    class Meta:
        unique_together = ('district', 'school_year')
        verbose_name = 'Expenditures Programs'
        verbose_name_plural = 'Expenditures Programs'

    def __str__(self):
        return f"Program Expenditures for {self.district} in {self.school_year}"


class ExpendituresServices(models.Model):
    district = models.ForeignKey(District, on_delete=models.CASCADE)
    school_year = models.IntegerField()
    instruction = models.FloatField()
    support_services = models.FloatField()
    noninstructional_services = models.FloatField()
    improvement_services = models.FloatField()
    support_services_students = models.FloatField()
    operation_of_plant_services = models.FloatField()
    students_transportation_services = models.FloatField()
    central = models.FloatField()
    other_support_services = models.FloatField()

    class Meta:
        unique_together = ('district', 'school_year')
        verbose_name = 'Expenditures Services'
        verbose_name_plural = 'Expenditures Services'

    def __str__(self):
        return f"Service Expenditures for {self.district} in {self.school_year}"


class ExpendituresPerAdm(models.Model):
    district = models.ForeignKey(District, on_delete=models.CASCADE)
    school_year = models.IntegerField()
    adm = models.FloatField()
    weighted_adm = models.FloatField()
    instruction_per_adm = models.FloatField()
    support_services_per_adm = models.FloatField()
    non_instructional_per_adm = models.FloatField()
    current_exp_per_adm = models.FloatField()
    facilities_construction_per_adm = models.FloatField()
    other_financing_uses_per_adm = models.FloatField()
    total_exp_per_adm = models.FloatField()

    class Meta:
        unique_together = ('district', 'school_year')
        verbose_name = 'Expenditures Per ADM'
        verbose_name_plural = 'Expenditures Per ADM'

    def __str__(self):
        return f"Expenditures per ADM for {self.district} in {self.school_year}"


class RevenuesBySource(models.Model):
    district = models.ForeignKey(District, on_delete=models.CASCADE)
    school_year = models.IntegerField()
    total_revenue = models.FloatField()
    local_taxes = models.FloatField()
    local_other = models.FloatField()
    total_local_revenue = models.FloatField()
    local_per_of_total_revenue = models.FloatField()
    total_state_revenue = models.FloatField()
    state_per_of_total_revenue = models.FloatField()
    revenue_from_federal_sources = models.FloatField()
    federal_per_of_total_revenue = models.FloatField()
    total_other_revenue = models.FloatField()
    other_per_of_total_revenue = models.FloatField()

    class Meta:
        unique_together = ('district', 'school_year')
        verbose_name = 'Revenues by Source'
        verbose_name_plural = 'Revenues by Source'

    def __str__(self):
        return f"Revenues by Source for {self.district} in {self.school_year}"

class RevenuesPerAdm(models.Model):
    district = models.ForeignKey(District, on_delete=models.CASCADE)
    school_year = models.IntegerField()
    adm = models.FloatField()
    total_revenue_per_adm = models.FloatField()
    total_rank_total = models.IntegerField()
    local_revenue_per_adm = models.FloatField()
    total_rank_local = models.IntegerField()
    state_revenue_per_adm = models.FloatField()
    total_rank_state = models.IntegerField()
    federal_revenue_per_adm = models.FloatField()
    total_rank_federal = models.IntegerField()
    other_revenue_per_adm = models.FloatField()
    total_rank_other = models.IntegerField()

    class Meta:
        unique_together = ('district', 'school_year')
        verbose_name = 'Revenues per ADM'
        verbose_name_plural = 'Revenues per ADM'

    def __str__(self):
        return f"Revenues per ADM for {self.district} in {self.school_year}"


class RevenuesTaxesColl(models.Model):
    district = models.ForeignKey(District, on_delete=models.CASCADE)
    school_year = models.IntegerField()
    total_taxes_collected = models.FloatField()
    real_estate_taxes_collected = models.FloatField()
    public_utility_realty_taxes_collected = models.FloatField()
    payment_in_lieu_taxes_collected = models.FloatField()
    per_capita_taxes_collected = models.FloatField()
    first_class_sd_taxes_collected = models.FloatField()
    delinquent_taxes_collected = models.FloatField()
    steb_market_value = models.FloatField()
    equalized_mills = models.FloatField()

    class Meta:
        unique_together = ('district', 'school_year')
        verbose_name = 'Revenues Taxes Collection'
        verbose_name_plural = 'Revenues Taxes Collection'

    def __str__(self):
        return f"Revenues Taxes Collection for {self.district} in {self.school_year}"


class AidRatio(models.Model):
    district = models.ForeignKey(District, on_delete=models.CASCADE)
    school_year = models.IntegerField()
    market_value = models.FloatField()
    personal_income = models.FloatField()
    wadm = models.FloatField()
    mv_per_wadm = models.FloatField()
    market_value_aid_ratio = models.FloatField()
    pi_per_wadm = models.FloatField()
    personal_income_aid_ratio = models.FloatField()
    market_value_personal_income_aid_ratio = models.FloatField()

    class Meta:
        unique_together = ('district', 'school_year')
        verbose_name = 'Aid Ratio'
        verbose_name_plural = 'Aid Ratios'

    def __str__(self):
        return f"Aid Ratio for {self.district} in {self.school_year}"


class AdmGeneral(models.Model):
    district = models.ForeignKey(District, on_delete=models.CASCADE)
    school_year = models.IntegerField()
    adm = models.FloatField()
    wadm = models.FloatField()
    adjusted_adm = models.FloatField()
    adm_pde_363 = models.FloatField()

    class Meta:
        unique_together = ('district', 'school_year')
        verbose_name = 'ADM General'
        verbose_name_plural = 'ADM General'

    def __str__(self):
        return f"ADM General for {self.district} in {self.school_year}"


class AdmGrades(models.Model):
    district = models.ForeignKey(District, on_delete=models.CASCADE)
    school_year = models.IntegerField()
    adm_pre_kindergarten_ht = models.FloatField()
    adm_pre_kindergarten_ft = models.FloatField()
    adm_kindergarten_ht4 = models.FloatField()
    adm_kindergarten_ft4 = models.FloatField()
    adm_kindergarten_ht5 = models.FloatField()
    adm_kindergarten_ft5 = models.FloatField()
    adm_elementary = models.FloatField()
    adm_secondary = models.FloatField()

    class Meta:
        unique_together = ('district', 'school_year')
        verbose_name = 'ADM by Grades'
        verbose_name_plural = 'ADM by Grades'

    def __str__(self):
        return f"ADM by Grades for {self.district} in {self.school_year}"


class WadmGrades(models.Model):
    district = models.ForeignKey(District, on_delete=models.CASCADE)
    school_year = models.IntegerField()
    wadm_pre_kindergarten_ht = models.FloatField()
    wadm_pre_kindergarten_ft = models.FloatField()
    wadm_kindergarten_ht4 = models.FloatField()
    wadm_kindergarten_ft4 = models.FloatField()
    wadm_kindergarten_ht5 = models.FloatField()
    wadm_kindergarten_ft5 = models.FloatField()
    wadm_elementary = models.FloatField()
    wadm_secondary = models.FloatField()
    adjustment_factor = models.FloatField()

    class Meta:
        unique_together = ('district', 'school_year')
        verbose_name = 'WADM by Grades'
        verbose_name_plural = 'WADM by Grades'

    def __str__(self):
        return f"WADM by Grades for {self.district} in {self.school_year}"


class Misc(models.Model):
    district = models.ForeignKey(District, on_delete=models.CASCADE)
    school_year = models.IntegerField()
    mv_pi_aid_ratio = models.FloatField()
    adm = models.FloatField()
    wadm = models.FloatField()
    eq_mills = models.FloatField()
    pop_per_sq_mile = models.FloatField()
    aie_per_wadm = models.FloatField()
    total_exp_per_adm = models.FloatField()

    class Meta:
        unique_together = ('district', 'school_year')
        verbose_name = 'Miscellaneous Data'
        verbose_name_plural = 'Miscellaneous Data'

    def __str__(self):
        return f"Miscellaneous Data for {self.district} in {self.school_year}"

class MiscRank(models.Model):
    district = models.ForeignKey(District, on_delete=models.CASCADE)
    school_year = models.IntegerField()
    mv_pi_rk = models.IntegerField()
    wadm_rk = models.IntegerField()
    eq_mills_rk = models.IntegerField()
    pop_per_sq_mile_rk = models.IntegerField()
    aie_per_wadm_rk = models.IntegerField()
    total_exp_per_adm_rk = models.IntegerField()

    class Meta:
        unique_together = ('district', 'school_year')
        verbose_name = 'Misc Rank'
        verbose_name_plural = 'Misc Rank'

    def __str__(self):
        return f"Misc Rank for {self.district} in {self.school_year}"


class PersonalIncome(models.Model):
    district = models.ForeignKey(District, on_delete=models.CASCADE)
    school_year = models.IntegerField()
    records = models.IntegerField()
    compensation = models.FloatField()
    net_profits = models.FloatField()
    dividends_and_interest = models.FloatField()
    misc_income = models.FloatField()
    out_of_st_tax_records = models.IntegerField()
    out_of_st_tax_credit = models.FloatField()
    out_of_st_income = models.FloatField()
    total_personal_income = models.FloatField()
    adjusted_personal_income = models.FloatField()

    class Meta:
        unique_together = ('district', 'school_year')
        verbose_name = 'Personal Income'
        verbose_name_plural = 'Personal Income'

    def __str__(self):
        return f"Personal Income for {self.district} in {self.school_year}"


class RealEstateTax(models.Model):
    district = models.ForeignKey(District, on_delete=models.CASCADE)
    school_year = models.IntegerField()
    municipality_and_other = models.CharField(max_length=100)
    real_estate_mills = models.FloatField()
    additional_community_college_mills = models.FloatField()

    class Meta:
        unique_together = ('district', 'school_year')
        verbose_name = 'Real Estate Tax'
        verbose_name_plural = 'Real Estate Taxes'

    def __str__(self):
        return f"Real Estate Tax for {self.district} in {self.school_year}"


class BasicEduFunding(models.Model):
    district = models.ForeignKey(District, on_delete=models.CASCADE)
    school_year = models.IntegerField()
    final_bef = models.FloatField()
    base_bef = models.FloatField()
    student_weighted_distribution = models.FloatField()

    class Meta:
        unique_together = ('district', 'school_year')
        verbose_name = 'Basic Education Funding'
        verbose_name_plural = 'Basic Education Funding'

    def __str__(self):
        return f"Basic Education Funding for {self.district} in {self.school_year}"


class SecCareerTechnicalFund(models.Model):
    district = models.ForeignKey(District, on_delete=models.CASCADE)
    school_year = models.IntegerField()
    final_sctes = models.FloatField()
    aie_per_wadm = models.FloatField()
    ber = models.FloatField()
    vocational_adm = models.FloatField()
    voc_adm_multiplier = models.FloatField()

    class Meta:
        unique_together = ('district', 'school_year')
        verbose_name = 'Secondary Career Technical Fund'
        verbose_name_plural = 'Secondary Career Technical Fund'

    def __str__(self):
        return f"Secondary Career Technical Fund for {self.district} in {self.school_year}"


class SpecialEduFunding(models.Model):
    district = models.ForeignKey(District, on_delete=models.CASCADE)
    school_year = models.IntegerField()
    final_sef = models.FloatField()
    base_sef = models.FloatField()
    student_based_allocation = models.FloatField()

    class Meta:
        unique_together = ('district', 'school_year')
        verbose_name = 'Special Education Funding'
        verbose_name_plural = 'Special Education Funding'

    def __str__(self):
        return f"Special Education Funding for {self.district} in {self.school_year}"


class LowIncomePercentPubSchool(models.Model):
    school = models.ForeignKey(School, on_delete=models.CASCADE)
    school_year = models.IntegerField()
    total_enrollment = models.IntegerField()
    low_income_enrollment = models.IntegerField()
    percent_enrollment_from_low_income_families = models.FloatField()

    class Meta:
        unique_together = ('school', 'school_year')
        verbose_name = 'Low Income Percent for Public Schools'
        verbose_name_plural = 'Low Income Percent for Public Schools'

    def __str__(self):
        return f"Low Income Percent for Public School {self.school} in {self.school_year}"


class LowIncomePercentDistrict(models.Model):
    district = models.ForeignKey(District, on_delete=models.CASCADE)
    school_year = models.IntegerField()
    total_enrollment = models.IntegerField()
    low_income_enrollment = models.IntegerField()
    percent_of_enrollment_from_low_income_families = models.FloatField()

    class Meta:
        unique_together = ('district', 'school_year')
        verbose_name = 'Low Income Percent for District'
        verbose_name_plural = 'Low Income Percent for Districts'

    def __str__(self):
        return f"Low Income Percent for District {self.district} in {self.school_year}"


class LowIncomePercentPrivateSchool(models.Model):
    school = models.ForeignKey(School, on_delete=models.CASCADE)
    school_year = models.IntegerField()
    low_income_percentage = models.FloatField()

    class Meta:
        unique_together = ('school', 'school_year')
        verbose_name = 'Low Income Percent for Private Schools'
        verbose_name_plural = 'Low Income Percent for Private Schools'

    def __str__(self):
        return f"Low Income Percent for Private School {self.school} in {self.school_year}"


class PssaSchool(models.Model):
    school = models.ForeignKey(School, on_delete=models.CASCADE)
    school_year = models.IntegerField()
    pssa_subject = models.CharField(max_length=100)
    group_students = models.CharField(max_length=75)
    grade = models.IntegerField()
    number_scored = models.FloatField()
    percent_advanced = models.FloatField()
    percent_proficient = models.FloatField()
    percent_basic = models.FloatField()
    percent_below_basic = models.FloatField()
    percent_proficient_and_above = models.FloatField()

    class Meta:
        unique_together = ('school', 'school_year')
        verbose_name = 'PSSA School Data'
        verbose_name_plural = 'PSSA School Data'

    def __str__(self):
        return f"PSSA Data for {self.school} in {self.school_year}"


class ApPercentGapMetAll(models.Model):
    school = models.ForeignKey(School, on_delete=models.CASCADE)
    school_year = models.IntegerField()
    math_percent_required_gap_closure_met_all = models.FloatField()
    ela_lit_percent_required_gap_closure_met_all = models.FloatField()
    science_bio_percent_required_gap_closure_met_all = models.FloatField()
    ela_percent_required_gap_closure_met_all = models.FloatField()
    bio_percent_required_gap_closure_met_all = models.FloatField()
    algebra_percent_required_gap_closure_met_all = models.FloatField()
    science_percent_required_gap_closure_met_all = models.FloatField()
    math_alg_percent_required_gap_closure_met_all = models.FloatField()
    lit_percent_required_gap_closure_met_all = models.FloatField()

    class Meta:
        unique_together = ('school', 'school_year')
        verbose_name = 'AP Percent Gap Met All'
        verbose_name_plural = 'AP Percent Gap Met All'

    def __str__(self):
        return f"AP Percent Gap Met All for {self.school} in {self.school_year}"


class ApPercentGapMetHus(models.Model):
    school = models.ForeignKey(School, on_delete=models.CASCADE)
    school_year = models.IntegerField()
    math_percent_required_gap_closure_met_hus = models.FloatField()
    ela_lit_percent_required_gap_closure_met_hus = models.FloatField()
    science_bio_percent_required_gap_closure_met_hus = models.FloatField()
    ela_percent_required_gap_closure_met_hus = models.FloatField()
    bio_percent_required_gap_closure_met_hus = models.FloatField()
    algebra_percent_required_gap_closure_met_hus = models.FloatField()
    science_percent_required_gap_closure_met_hus = models.FloatField()
    math_alg_percent_required_gap_closure_met_hus = models.FloatField()
    lit_percent_required_gap_closure_met_hus = models.FloatField()

    class Meta:
        unique_together = ('school', 'school_year')
        verbose_name = 'AP Percent Gap Met HUS'
        verbose_name_plural = 'AP Percent Gap Met HUS'

    def __str__(self):
        return f"AP Percent Gap Met HUS for {self.school} in {self.school_year}"


class ApGeneral(models.Model):
    school = models.ForeignKey(School, on_delete=models.CASCADE)
    school_year = models.IntegerField()
    promotion_rate_all_students = models.FloatField()
    ap_ib_college_credit = models.FloatField()
    attendance_rate = models.FloatField()
    calculated_score = models.FloatField()
    cohort_grad_rate = models.FloatField()
    industry_standards_based_competency_assessments_percent = models.FloatField()
    percent_industry_standards_based_competency_assessments_advanced = models.FloatField()
    final_academic_score = models.FloatField()
    percent_3_higher_ap_4_higher_ib = models.FloatField()
    grade_12_enrollment = models.IntegerField()

    class Meta:
        unique_together = ('school', 'school_year')
        verbose_name = 'AP General'
        verbose_name_plural = 'AP General'

    def __str__(self):
        return f"AP General for {self.school} in {self.school_year}"


class ApPssaKeystone(models.Model):
    school = models.ForeignKey(School, on_delete=models.CASCADE)
    school_year = models.IntegerField()
    ela_meeting_annual_academic_growth_expectations = models.FloatField()
    ela_percent_proficient_or_advanced_pssa = models.FloatField()
    math_meeting_annual_academic_growth_expectations = models.FloatField()
    math_percent_proficient_or_advanced_keystone = models.FloatField()
    science_bio_meeting_annual_academic_growth_exp = models.FloatField()
    science_bio_percent_proficient_advanced_pssa_keystone = models.FloatField()
    percent_pssa_keystone_advanced_ela_lit = models.FloatField()
    percent_pssa_keystone_advanced_math_alg = models.FloatField()
    percent_pssa_keystone_advanced_scnice_bio = models.FloatField()
    grade_3_percent_proficient_advanced = models.FloatField()

    class Meta:
        unique_together = ('school', 'school_year')
        verbose_name = 'AP PSSA Keystone'
        verbose_name_plural = 'AP PSSA Keystone'

    def __str__(self):
        return f"AP PSSA Keystone for {self.school} in {self.school_year}"


class ApSatAct(models.Model):
    school = models.ForeignKey(School, on_delete=models.CASCADE)
    school_year = models.IntegerField()
    sat_act_college_ready_benchmark = models.FloatField()
    num_grade_12_meeting_benchmarks = models.IntegerField()
    number_grade_12_with_22_higher_act = models.IntegerField()
    number_grade_12_with_3_higher_ap_4_higher_ib = models.IntegerField()
    number_grade_12_taking_plan = models.IntegerField()
    number_grade_12_taking_psat = models.IntegerField()
    psat_plan_participation = models.FloatField()

    class Meta:
        unique_together = ('school', 'school_year')
        verbose_name = 'AP SAT ACT'
        verbose_name_plural = 'AP SAT ACT'

    def __str__(self):
        return f"AP SAT ACT for {self.school} in {self.school_year}"


class PublicSchoolGradRatesDistrict(models.Model):
    district = models.ForeignKey(District, on_delete=models.CASCADE)
    school_year = models.IntegerField()
    total_graduates = models.IntegerField()
    total_college_bound = models.IntegerField()
    total_college_bound_percentage = models.FloatField()
    two_four_year_college_university = models.IntegerField()
    two_four_year_college_university_percentage = models.FloatField()
    total_postsecondary_bound = models.IntegerField()
    total_postsecondary_bound_percentage = models.FloatField()
    non_degree_getting_postsecondary_school = models.IntegerField()
    non_degree_getting_postsecondary_school_percentage = models.FloatField()
    specialized_associate_degree_getting_institution = models.IntegerField()
    specialized_associate_degree_getting_institution_percentage = models.FloatField()

    class Meta:
        unique_together = ('district', 'school_year')
        verbose_name = 'Public School Grad Rates District'
        verbose_name_plural = 'Public School Grad Rates District'

    def __str__(self):
        return f"Public School Grad Rates District for {self.district} in {self.school_year}"


class PublicSchoolGradRatesSchool(models.Model):
    school = models.ForeignKey(School, on_delete=models.CASCADE)
    school_year = models.IntegerField()
    total_graduates = models.IntegerField()
    total_college_bound = models.IntegerField()
    total_college_bound_percentage = models.FloatField()
    two_four_year_college_university = models.IntegerField()
    two_four_year_college_university_percentage = models.FloatField()
    total_postsecondary_bound = models.IntegerField()
    total_postsecondary_bound_percentage = models.FloatField()
    non_degree_getting_postsecondary_school = models.IntegerField()
    non_degree_getting_postsecondary_school_percentage = models.FloatField()
    specialized_associate_degree_getting_institution = models.IntegerField()
    specialized_associate_degree_getting_institution_percentage = models.FloatField()

    class Meta:
        unique_together = ('school', 'school_year')
        verbose_name = 'Public School Grad Rates School'
        verbose_name_plural = 'Public School Grad Rates School'

    def __str__(self):
        return f"Public School Grad Rates School for {self.school} in {self.school_year}"


class PublicSchoolDropoutsSchool(models.Model):
    school = models.ForeignKey(School, on_delete=models.CASCADE)
    school_year = models.IntegerField()
    oct_1_enrollment_grades_7_12 = models.IntegerField()
    male_dropouts = models.IntegerField()
    female_dropouts = models.IntegerField()
    dropouts = models.IntegerField()
    dropout_rate = models.FloatField()

    class Meta:
        unique_together = ('school', 'school_year')
        verbose_name = 'Public School Dropouts School'
        verbose_name_plural = 'Public School Dropouts School'

    def __str__(self):
        return f"Public School Dropouts for {self.school} in {self.school_year}"


class PublicSchoolDropoutsDistrict(models.Model):
    district = models.ForeignKey(District, on_delete=models.CASCADE)
    school_year = models.IntegerField()
    oct_1_enrollment_grades_7_12 = models.IntegerField()
    male_dropouts = models.IntegerField()
    female_dropouts = models.IntegerField()
    dropouts = models.IntegerField()
    dropout_rate = models.FloatField()

    class Meta:
        unique_together = ('district', 'school_year')
        verbose_name = 'Public School Dropouts District'
        verbose_name_plural = 'Public School Dropouts District'

    def __str__(self):
        return f"Public School Dropouts for {self.district} in {self.school_year}"


class KeystoneGradeSchool(models.Model):
    school = models.ForeignKey(School, on_delete=models.CASCADE)
    school_year = models.IntegerField()
    keystone_subject = models.CharField(max_length=25)
    student_group = models.CharField(max_length=75)
    grade = models.IntegerField()
    number_scored = models.IntegerField()
    percent_advanced = models.FloatField()
    percent_proficient = models.FloatField()
    percent_basic = models.FloatField()
    percent_below_basic = models.FloatField()

    class Meta:
        unique_together = ('school', 'school_year')
        verbose_name = 'Keystone Grade School'
        verbose_name_plural = 'Keystone Grade School'

    def __str__(self):
        return f"Keystone Grade Data for {self.school} in {self.school_year}"


class GradRateByRaceSchool(models.Model):
    school = models.ForeignKey(School, on_delete=models.CASCADE)
    school_year = models.IntegerField()
    x_year_cohort = models.IntegerField()
    aian_grad_rate = models.FloatField()
    native_hawaiin_pacific_islander_grad_rate = models.FloatField()
    asian_grad_rate = models.FloatField()
    black_grad_rate = models.FloatField()
    hispanic_grad_rate = models.FloatField()
    white_grad_rate = models.FloatField()
    multi_racial_grad_rate = models.FloatField()

    class Meta:
        unique_together = ('school', 'school_year')
        verbose_name = 'Grad Rate by Race School'
        verbose_name_plural = 'Grad Rate by Race School'

    def __str__(self):
        return f"Grad Rate by Race for {self.school} in {self.school_year}"


class GradRateByCategorySchool(models.Model):
    school = models.ForeignKey(School, on_delete=models.CASCADE)
    school_year = models.IntegerField()
    x_year_cohort = models.IntegerField()
    cohort_grad_rate = models.FloatField()
    male_grad_rate = models.FloatField()
    female_grad_rate = models.FloatField()
    special_ed_grad_rate = models.FloatField()
    el_grad_rate = models.FloatField()
    econ_disadvantaged_grad_rate = models.FloatField()
    migrant_grad_rate = models.FloatField()
    foster_grad_rate = models.FloatField()
    homeless_grad_rate = models.FloatField()
    military_grad_rate = models.FloatField()

    class Meta:
        unique_together = ('school', 'school_year')
        verbose_name = 'Grad Rate by Category School'
        verbose_name_plural = 'Grad Rate by Category School'

    def __str__(self):
        return f"Grad Rate by Category for {self.school} in {self.school_year}"


class TotalGradsSchool(models.Model):
    school = models.ForeignKey(School, on_delete=models.CASCADE)
    school_year = models.IntegerField()
    x_year_cohort = models.IntegerField()
    grads = models.IntegerField()
    cohort = models.IntegerField()

    class Meta:
        unique_together = ('school', 'school_year')
        verbose_name = 'Total Grads School'
        verbose_name_plural = 'Total Grads School'

    def __str__(self):
        return f"Total Grads for {self.school} in {self.school_year}"


class GradRateByRaceDistrict(models.Model):
    district = models.ForeignKey(District, on_delete=models.CASCADE)
    school_year = models.IntegerField()
    x_year_cohort = models.IntegerField()
    aian_grad_rate = models.FloatField()
    native_hawaiin_pacific_islander_grad_rate = models.FloatField()
    asian_grad_rate = models.FloatField()
    black_grad_rate = models.FloatField()
    hispanic_grad_rate = models.FloatField()
    white_grad_rate = models.FloatField()
    multi_racial_grad_rate = models.FloatField()

    class Meta:
        unique_together = ('district', 'school_year')
        verbose_name = 'Grad Rate by Race District'
        verbose_name_plural = 'Grad Rate by Race District'

    def __str__(self):
        return f"Grad Rate by Race for {self.district} in {self.school_year}"


class GradRateByCategoryDistrict(models.Model):
    district = models.ForeignKey(District, on_delete=models.CASCADE)
    school_year = models.IntegerField()
    x_year_cohort = models.IntegerField()
    cohort_grad_rate = models.FloatField()
    male_grad_rate = models.FloatField()
    female_grad_rate = models.FloatField()
    special_ed_grad_rate = models.FloatField()
    el_grad_rate = models.FloatField()
    econ_disadvantaged_grad_rate = models.FloatField()
    migrant_grad_rate = models.FloatField()
    foster_grad_rate = models.FloatField()
    homeless_grad_rate = models.FloatField()
    military_grad_rate = models.FloatField()

    class Meta:
        unique_together = ('district', 'school_year')
        verbose_name = 'Grad Rate by Category District'
        verbose_name_plural = 'Grad Rate by Category District'

    def __str__(self):
        return f"Grad Rate by Category for {self.district} in {self.school_year}"


class TotalGradsDistrict(models.Model):
    district = models.ForeignKey(District, on_delete=models.CASCADE)
    school_year = models.IntegerField()
    x_year_cohort = models.IntegerField()
    grads = models.IntegerField()
    cohort = models.IntegerField()

    class Meta:
        unique_together = ('district', 'school_year')
        verbose_name = 'Total Grads District'
        verbose_name_plural = 'Total Grads District'

    def __str__(self):
        return f"Total Grads for {self.district} in {self.school_year}"


class PrivateNonPublicElemEnrollmentPrivatePaid(models.Model):
    school = models.ForeignKey(School, on_delete=models.CASCADE)
    school_year = models.IntegerField()
    k4 = models.IntegerField()
    k5 = models.IntegerField()
    grade_1 = models.IntegerField()
    grade_2 = models.IntegerField()
    grade_3 = models.IntegerField()
    grade_4 = models.IntegerField()
    grade_5 = models.IntegerField()
    grade_6 = models.IntegerField()
    grade_7E = models.IntegerField()
    grade_8E = models.IntegerField()
    total_elementary_ungraded = models.IntegerField()
    non_resident = models.IntegerField()
    resident = models.IntegerField()
    total_elementary_enrollment = models.IntegerField()

    class Meta:
        unique_together = ('school', 'school_year')
        verbose_name = 'Private Non-Public Elementary Enrollment (Private Paid)'
        verbose_name_plural = 'Private Non-Public Elementary Enrollment (Private Paid)'

    def __str__(self):
        return f"Private Non-Public Elem Enrollment (Private Paid) for {self.school} in {self.school_year}"


class PrivateNonPublicElemEnrollmentFullyPublicPaid(models.Model):
    school = models.ForeignKey(School, on_delete=models.CASCADE)
    school_year = models.IntegerField()
    k4 = models.IntegerField()
    k5 = models.IntegerField()
    grade_1 = models.IntegerField()
    grade_2 = models.IntegerField()
    grade_3 = models.IntegerField()
    grade_4 = models.IntegerField()
    grade_5 = models.IntegerField()
    grade_6 = models.IntegerField()
    grade_7E = models.IntegerField()
    grade_8E = models.IntegerField()
    total_elementary_ungraded = models.IntegerField()
    non_resident = models.IntegerField()
    resident = models.IntegerField()
    total_elementary_enrollment = models.IntegerField()

    class Meta:
        unique_together = ('school', 'school_year')
        verbose_name = 'Private Non-Public Elementary Enrollment (Fully Public Paid)'
        verbose_name_plural = 'Private Non-Public Elementary Enrollment (Fully Public Paid)'

    def __str__(self):
        return f"Private Non-Public Elem Enrollment (Fully Public Paid) for {self.school} in {self.school_year}"


class PrivateNonPublicSecondaryEnrollmentPrivatePaid(models.Model):
    school = models.ForeignKey(School, on_delete=models.CASCADE)
    school_year = models.IntegerField()
    grade_9 = models.IntegerField()
    grade_10 = models.IntegerField()
    grade_11 = models.IntegerField()
    grade_12 = models.IntegerField()
    secondary_ungraded = models.IntegerField()
    non_resident = models.IntegerField()
    resident = models.IntegerField()
    total_secondary_enrollment = models.IntegerField()

    class Meta:
        unique_together = ('school', 'school_year')
        verbose_name = 'Private Non-Public Secondary Enrollment (Private Paid)'
        verbose_name_plural = 'Private Non-Public Secondary Enrollment (Private Paid)'

    def __str__(self):
        return f"Private Non-Public Secondary Enrollment (Private Paid) for {self.school} in {self.school_year}"


class PrivateNonPublicSecondaryEnrollmentFullyPublicPaid(models.Model):
    school = models.ForeignKey(School, on_delete=models.CASCADE)
    school_year = models.IntegerField()
    grade_9 = models.IntegerField()
    grade_10 = models.IntegerField()
    grade_11 = models.IntegerField()
    grade_12 = models.IntegerField()
    secondary_ungraded = models.IntegerField()
    non_resident = models.IntegerField()
    resident = models.IntegerField()
    total_secondary_enrollment = models.IntegerField()

    class Meta:
        unique_together = ('school', 'school_year')
        verbose_name = 'Private Non-Public Secondary Enrollment (Fully Public Paid)'
        verbose_name_plural = 'Private Non-Public Secondary Enrollment (Fully Public Paid)'

    def __str__(self):
        return f"Private Non-Public Secondary Enrollment (Fully Public Paid) for {self.school} in {self.school_year}"


class PrivateNonPublicOtherEnrollmentPrivatePaid(models.Model):
    school = models.ForeignKey(School, on_delete=models.CASCADE)
    school_year = models.IntegerField()
    nursery = models.IntegerField()
    special_ed_preschool_k5 = models.IntegerField()
    special_ed_preschool_nursery_age_3_4_5 = models.IntegerField()
    non_resident = models.IntegerField()
    resident = models.IntegerField()
    total_other_enrollment = models.IntegerField()

    class Meta:
        unique_together = ('school', 'school_year')
        verbose_name = 'Private Non-Public Other Enrollment (Private Paid)'
        verbose_name_plural = 'Private Non-Public Other Enrollment (Private Paid)'

    def __str__(self):
        return f"Private Non-Public Other Enrollment (Private Paid) for {self.school} in {self.school_year}"


class PrivateNonPublicOtherEnrollmentPublicPaid(models.Model):
    school = models.ForeignKey(School, on_delete=models.CASCADE)
    school_year = models.IntegerField()
    nursery = models.IntegerField()
    special_ed_preschool_k5 = models.IntegerField()
    special_ed_preschool_nursery_age_3_4_5 = models.IntegerField()
    non_resident = models.IntegerField()
    resident = models.IntegerField()
    total_other_enrollment = models.IntegerField()

    class Meta:
        unique_together = ('school', 'school_year')
        verbose_name = 'Private Non-Public Other Enrollment (Public Paid)'
        verbose_name_plural = 'Private Non-Public Other Enrollment (Public Paid)'

    def __str__(self):
        return f"Private Non-Public Other Enrollment (Public Paid) for {self.school} in {self.school_year}"


class PrivateNonPublicFullTimeEquivalentTeachers(models.Model):
    school = models.ForeignKey(School, on_delete=models.CASCADE)
    school_year = models.IntegerField()
    nursery_fte = models.FloatField()
    elementary_fte = models.FloatField()
    secondary_fte = models.FloatField()
    special_education_fte = models.FloatField()
    total_fte = models.FloatField()

    class Meta:
        unique_together = ('school', 'school_year')
        verbose_name = 'Private Non-Public Full-Time Equivalent Teachers'
        verbose_name_plural = 'Private Non-Public Full-Time Equivalent Teachers'

    def __str__(self):
        return f"Private Non-Public Full-Time Equivalent Teachers for {self.school} in {self.school_year}"


class PrivateNonPublicLowIncomeEnrollment(models.Model):
    school = models.ForeignKey(School, on_delete=models.CASCADE)
    school_year = models.IntegerField()
    percent_nursery_low_income = models.FloatField()
    percent_k12_low_income = models.FloatField()

    class Meta:
        unique_together = ('school', 'school_year')
        verbose_name = 'Private Non-Public Low Income Enrollment'
        verbose_name_plural = 'Private Non-Public Low Income Enrollment'

    def __str__(self):
        return f"Private Non-Public Low Income Enrollment for {self.school} in {self.school_year}"

class PrivateNonPublicTotal(models.Model):
    school = models.ForeignKey(School, on_delete=models.CASCADE)
    school_year = models.IntegerField()
    grand_total = models.IntegerField()

    class Meta:
        unique_together = ('school', 'school_year')
        verbose_name = 'Private Non-Public Total'
        verbose_name_plural = 'Private Non-Public Totals'

    def __str__(self):
        return f"Private Non-Public Total for {self.school} in {self.school_year}"


class PublicSchoolEnrollmentSchool(models.Model):
    school = models.ForeignKey(School, on_delete=models.CASCADE)
    school_year = models.IntegerField()
    pka = models.IntegerField()
    pkp = models.IntegerField()
    pkf = models.IntegerField()
    k4a = models.IntegerField()
    k4p = models.IntegerField()
    k4f = models.IntegerField()
    k5a = models.IntegerField()
    k5p = models.IntegerField()
    k5f = models.IntegerField()
    grade_1 = models.IntegerField()
    grade_2 = models.IntegerField()
    grade_3 = models.IntegerField()
    grade_4 = models.IntegerField()
    grade_5 = models.IntegerField()
    grade_6 = models.IntegerField()
    grade_7 = models.IntegerField()
    grade_8 = models.IntegerField()
    grade_9 = models.IntegerField()
    grade_10 = models.IntegerField()
    grade_11 = models.IntegerField()
    grade_12 = models.IntegerField()
    total = models.IntegerField()

    class Meta:
        unique_together = ('school', 'school_year')
        verbose_name = 'Public School Enrollment (School)'
        verbose_name_plural = 'Public School Enrollments (School)'

    def __str__(self):
        return f"Public School Enrollment for {self.school} in {self.school_year}"


class PublicSchoolEnrollmentDistrict(models.Model):
    district = models.ForeignKey(District, on_delete=models.CASCADE)
    school_year = models.IntegerField()
    pka = models.IntegerField()
    pkp = models.IntegerField()
    pkf = models.IntegerField()
    k4a = models.IntegerField()
    k4p = models.IntegerField()
    k4f = models.IntegerField()
    k5a = models.IntegerField()
    k5p = models.IntegerField()
    k5f = models.IntegerField()
    grade_1 = models.IntegerField()
    grade_2 = models.IntegerField()
    grade_3 = models.IntegerField()
    grade_4 = models.IntegerField()
    grade_5 = models.IntegerField()
    grade_6 = models.IntegerField()
    grade_7 = models.IntegerField()
    grade_8 = models.IntegerField()
    grade_9 = models.IntegerField()
    grade_10 = models.IntegerField()
    grade_11 = models.IntegerField()
    grade_12 = models.IntegerField()
    total = models.IntegerField()

    class Meta:
        unique_together = ('district', 'school_year')
        verbose_name = 'Public School Enrollment (District)'
        verbose_name_plural = 'Public School Enrollments (District)'

    def __str__(self):
        return f"Public School Enrollment for {self.district} in {self.school_year}"



